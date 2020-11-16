import numpy as np

#T-Peak Detection
def t_peaks_detection(normalised_valueInt, time_one_sample, index_of_r_values, all_peaks):
    show_t = True
    try:
        t_values = []
        # Procedure - First divide the distance b/w two R peaks into two equal halves
        # Find the highest peak in the left half i.e., T-Peak
        for k in range(len(index_of_r_values) - 1):
            temp_peaks_t = all_peaks[index_of_r_values[k] + 1:(index_of_r_values[k + 1] + index_of_r_values[k]) // 2 + 1]
            temp_peaks_val_t = [(z, normalised_valueInt[z]) for z in temp_peaks_t]
            t_values.append(max(temp_peaks_val_t, key=lambda x: x[1])[0])

        t_time = [i * time_one_sample for i in t_values]

        tt = set(t_values)
        index_of_t_values = [i for i, e in enumerate(all_peaks) if e in tt]
    except:
        show_t = False

    return t_time, t_values, show_t, index_of_t_values

# End of T-Peak
def t_end_peaks_detection(normalised_valueInt, time_one_sample, all_peaks, t_values, index_of_t_values):
    show_t_end = True
    try:
        t_end_values = []

        for i in range(len(index_of_t_values)):
            temp_end = normalised_valueInt[t_values[i]: all_peaks[index_of_t_values[i] + 1]]
            t_end_min = min(temp_end)
            index_of_minimum = np.where(normalised_valueInt == t_end_min)
            for x in index_of_minimum:
                t_end_values.append(x[0])

        t_end_time = [i * time_one_sample for i in t_end_values]
    except:
        show_t_end = False
    return t_end_time, t_end_values, show_t_end

# Start of T-Peak
def t_start_peaks_detection(normalised_valueInt, time_one_sample, all_peaks, t_values, index_of_t_values, r_peaks, S_values):
    show_t_start = True
    try:
        t_start_values = []

        for i in range(len(index_of_t_values)):
            if all_peaks[index_of_t_values[i] - 2] not in r_peaks and all_peaks[index_of_t_values[i] - 2] > S_values[i]:
                temp_start = normalised_valueInt[all_peaks[index_of_t_values[i] - 2]: t_values[i]]
            else:
                temp_start = normalised_valueInt[all_peaks[index_of_t_values[i] - 1]: t_values[i]]
            t_start_min = min(temp_start)
            index_of_minimum = np.where(normalised_valueInt == t_start_min)
            for x in index_of_minimum:
                t_start_values.append(x[0])

        t_start_time = [i * time_one_sample for i in t_start_values]
    except:
        show_t_start = False

    return t_start_time, t_start_values, show_t_start