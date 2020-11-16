import numpy as np

#P-Peak Detection
def p_peaks_detection(normalised_valueInt, time_one_sample, index_of_r_values, all_peaks):
    show_p = True
    try:
        p_values = []
        # Procedure - First divide the distance b/w two R peaks into two equal halves
        # Find the highest peak in the right half i.e., P-Peak
        for k in range(len(index_of_r_values) - 1):
            temp_peaks_p = all_peaks[(index_of_r_values[k + 1] + index_of_r_values[k]) // 2 + 1: index_of_r_values[k + 1]]
            temp_peaks_val_p = [(z, normalised_valueInt[z]) for z in temp_peaks_p]
            p_values.append(max(temp_peaks_val_p, key=lambda x: x[1])[0])

        p_time = [i * time_one_sample for i in p_values]
    except:
        show_p = False
    return p_time, p_values, show_p

def p_start_peaks_detection(normalised_valueInt, time_one_sample, all_peaks, p_values, t_values):
    # Start of P-Peak
    show_p_start = True
    try:
        pp = set(p_values)
        index_of_p_values = [i for i, e in enumerate(all_peaks) if e in pp]

        p_start_values = []

        for i in range(len(index_of_p_values)):
            if all_peaks[index_of_p_values[i] - 2] not in t_values:
                temp_start = normalised_valueInt[all_peaks[index_of_p_values[i] - 2]: p_values[i]]
            else:
                temp_start = normalised_valueInt[all_peaks[index_of_p_values[i] - 1]: p_values[i]]
            p_start_min = min(temp_start)
            index_of_minimum = np.where(normalised_valueInt == p_start_min)
            for x in index_of_minimum:
                p_start_values.append(x[0])

        p_start_time = [i * time_one_sample for i in p_start_values]
    except:
        show_p_start = False

    return p_start_time, p_start_values, show_p_start