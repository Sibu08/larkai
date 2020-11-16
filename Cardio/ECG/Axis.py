import numpy as np
import pywt
#import scipy.io.wavfile as wav
# Funtion for reconstruction of the signal
def reconstruction_plot(yyy, **kwargs):
    ym = np.median(yyy)
    k = yyy - ym
    return k

def create_axis(path):
    #fs, df = wav.read(path)
    df = np.genfromtxt(path, delimiter=',')
    fs = 500
    data = df.tolist()

    # Taking samples of data
    x = data[3000:6000]
    x = np.array(x)

    # Creating Wavelet(Symlet 5) Object
    w = pywt.Wavelet('sym5')

    # Defining no. of levels = 5
    nl = 5

    # Ordered list of coefficients arrays where nl denotes the level of decomposition.
    # The first element (cA_n) of the result is approximation coefficients array and
    # the following elements (cD_n - cD_1) are details coefficients arrays.
    coeffs = pywt.wavedec(x, w, level=nl)

    i = 1

    # reconstruction of the decomposed signal using approximation coefficients array and details coefficients arrays.
    normalised_valueInt = (reconstruction_plot(pywt.waverec(coeffs[:i + 2] + [None] * (nl - i - 1), w)))

    # Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
    normalised_valueInt = (normalised_valueInt / 1023) * 5

    # using Min-Max Scaler
    maximun_x = max(normalised_valueInt)
    minimum_x = min(normalised_valueInt)
    normalised_valueInt = (2 * ((normalised_valueInt - minimum_x) / (maximun_x - minimum_x))) - 1

    # No. of Samples in 1 sec.
    time_one_sample = 1 / fs

    # Changing into time domain
    c = 0
    time_axis = []

    # Determining the time axis
    for x in range(0, len(normalised_valueInt)):
        c = c + 1
        time_axis.append(c * time_one_sample)

    return time_axis, normalised_valueInt, time_one_sample