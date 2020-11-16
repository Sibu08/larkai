import numpy as np
from scipy.signal import butter,filtfilt,hilbert,find_peaks
import pywt
#import scipy.io.wavfile as wav

# Funtion for reconstruction of the signal
def reconstruction_plot(yyy, **kwargs):
    ym = np.median(yyy)
    k = yyy - ym
    l = np.linspace(0, 1., num=len(yyy))
    return k

def create_wavelet(path):
    # Reading data from audio file
    #fs, df = wav.read(path)
    df = np.genfromtxt(path, delimiter=',')
    fs = 4000
    # Normalisation of the data
    maximun_x = max(df)
    minimum_x = min(df)
    df = (2 * ((df - minimum_x) / (maximun_x - minimum_x))) - 1

    # Creating Wavelet(Symlet 5) Object
    w = pywt.Wavelet('db6')

    # Defining no. of levels = 5
    nl = 5

    # Ordered list of coefficients arrays where nl denotes the level of decomposition.
    # The first element (cA_n) of the result is approximation coefficients array and
    # the following elements (cD_n - cD_1) are details coefficients arrays.
    coeffs = pywt.wavedec(df, w, level=nl)

    i = 1

    # reconstruction of the decomposed signal using approximation coefficients array and details coefficients arrays.
    normalised_valueInt = (reconstruction_plot(pywt.waverec(coeffs[:i + 1] + [None] * (nl - i), w)))

    # Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    normalised_valueInt = (normalised_valueInt / 1023) * 5

    # Extracting small portion
    normalised = normalised_valueInt[20000:40000]

    # No. of Samples in 1 sec.
    time_one_sample = 1 / fs

    # Changing into time domain
    c = 0
    time_axis = []

    # Determining the time axis
    for x in range(0, len(normalised)):
        c = c + 1
        time_axis.append(c * time_one_sample)

    return  normalised, time_axis, time_one_sample

def butter_lowpass_filter(data):
    #Filter Requirements
    fs = 450.0  # sample rate, Hz
    cutoff = 2  # desired cutoff frequency of the filter, Hz slightly higher than actual 1.2 Hz
    order = 2  # sin wave can be approx represented as quadratic
    normal_cutoff = cutoff / (0.5 * fs)
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

def s_d_detection(normalised, time_one_sample):
    # Applying Hilbert transform to find the envelope of the signal
    analytic_signal = hilbert(normalised)
    amplitude_envelope = np.abs(analytic_signal)

    # Filtering out the hilbert transform to remove high frequency component
    envelope_filtered = butter_lowpass_filter(amplitude_envelope)

    # Detecting S1 Peaks
    peak_s1, _ = find_peaks(envelope_filtered, prominence=.0010, distance=1500)

    allpeaks, _ = find_peaks(envelope_filtered)

    peak_time_s1 = peak_s1 * time_one_sample

    st = set(peak_s1)
    index_of_s1 = [i for i, e in enumerate(allpeaks) if e in st]

    # Detecting S2 Peaks
    peak_s2 = []
    for i in range(len(index_of_s1) - 1):
        temp_s2 = allpeaks[index_of_s1[i] + 1: index_of_s1[i + 1]]
        temp_val_s2 = [(z, envelope_filtered[z]) for z in temp_s2]
        peak_s2.append(max(temp_val_s2, key=lambda x: x[1])[0])

    peak_time_s2 = [i * time_one_sample for i in peak_s2]

    return envelope_filtered, allpeaks, peak_time_s1, peak_s1, peak_time_s2, peak_s2

def s1_s2_widths(envelope_filtered, time_one_sample, allpeaks, peak_s1, peak_s2):
    s1 = set(peak_s1)
    index_of_s1 = [i for i, e in enumerate(allpeaks) if e in s1]
    s1_width = []
    for i in range(len(index_of_s1)):
        if index_of_s1[i] - 1 >= 0 and index_of_s1[i] + 1 < len(allpeaks):
            temp_data_left = envelope_filtered[allpeaks[index_of_s1[i] - 1]: allpeaks[index_of_s1[i]]]
            temp_data_right = envelope_filtered[allpeaks[index_of_s1[i]]: allpeaks[index_of_s1[i] + 1]]
            min_left = min(temp_data_left)
            min_right = min(temp_data_right)
            index_of_minimum_left = np.where(envelope_filtered == min_left)
            index_of_minimum_right = np.where(envelope_filtered == min_right)
            s1_width.extend([x[0] for x in index_of_minimum_left])
            s1_width.extend([x[0] for x in index_of_minimum_right])
    s1_width_time = [i * time_one_sample for i in s1_width]

    s2 = set(peak_s2)
    index_of_s2 = [i for i, e in enumerate(allpeaks) if e in s2]

    s2_width = []
    for i in range(len(index_of_s2)):
        if index_of_s2[i] - 1 >= 0 and index_of_s2[i] + 1 < len(allpeaks):
            temp_data_left = envelope_filtered[allpeaks[index_of_s2[i] - 1]: allpeaks[index_of_s2[i]]]
            temp_data_right = envelope_filtered[allpeaks[index_of_s2[i]]: allpeaks[index_of_s2[i] + 1]]
            min_left = min(temp_data_left)
            min_right = min(temp_data_right)
            index_of_minimum_left = np.where(envelope_filtered == min_left)
            index_of_minimum_right = np.where(envelope_filtered == min_right)
            s2_width.extend([x[0] for x in index_of_minimum_left])
            s2_width.extend([x[0] for x in index_of_minimum_right])
    s2_width_time = [i * time_one_sample for i in s2_width]

    return s1_width_time, s2_width_time
