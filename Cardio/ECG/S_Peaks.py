import numpy as np

#S-Peak Detection
def s_peaks_detection(normalised_valueInt, time_one_sample, t_values, r_peaks):
    show_s = True
    try:
        S_values = []
        # Procedure - The lowest point between each consecutive R-Peak and T-Peak i.e., S-Peak
        for i in range(len(t_values)):
            temp_data_s = normalised_valueInt[r_peaks[i]:t_values[i]]
            Smin = min(temp_data_s)
            index_of_minimum_s = np.where(normalised_valueInt == Smin)
            for x in index_of_minimum_s:
                S_values.append(x[0])

        S_time = [i * time_one_sample for i in S_values]
    except:
        show_s = False

    return S_time, S_values, show_s