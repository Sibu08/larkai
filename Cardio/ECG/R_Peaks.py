from scipy.signal import find_peaks

#R-Peak Detection with prominence .75
def r_peaks_detection(normalised_valueInt, time_one_sample):
    show_r = True
    try:
        r_peaks, _ = find_peaks(normalised_valueInt, prominence=.75, distance = 100)
        r_peaks_time = r_peaks * time_one_sample

        all_peaks = []

        # find all peaks in the dataset
        peaks1, _ = find_peaks(normalised_valueInt)
        all_peaks = peaks1.tolist()

        rr = set(r_peaks)
        index_of_r_values = [i for i, e in enumerate(all_peaks) if e in rr]
    except:
        show_r = False
    return r_peaks, r_peaks_time, all_peaks, index_of_r_values, show_r