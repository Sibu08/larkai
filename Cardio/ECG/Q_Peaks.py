import numpy as np

#Q-Peak Detection
def q_peaks_detection(normalised_valueInt, time_one_sample, p_values, r_peaks):
    show_q = True
    try:
        Q_values = []
        # Procedure - The lowest point between each consecutive P-Peak and R-Peak i.e., Q-Peak
        for i in range(len(p_values)):
            sliced_data = normalised_valueInt[p_values[i]:r_peaks[i + 1]]
            Qmin = min(sliced_data)
            index_of_minimum = np.where(normalised_valueInt == Qmin)
            for x in index_of_minimum:
                Q_values.append(x[0])

        Q_time = [i * time_one_sample for i in Q_values]
    except:
        show_q = False

    return Q_time, Q_values, show_q