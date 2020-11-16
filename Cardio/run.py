from ECG import R_Peaks, P_Peaks, Q_Peaks, S_Peaks, T_Peaks, Axis, Information
import plotting, pdf_gen
from PCG import S_D
import threading

def main():
    path_ecg = "C:/Users/Administrator/Desktop/larkai/ecg_sibam.csv"
    path_pcg = "C:/Users/Administrator/Desktop/larkai/pcg_sibam.csv"

    #ECG
    time_axis_ecg, normalised_valueInt, time_one_sample = Axis.create_axis(path_ecg)
    r_peaks, r_peaks_time, all_peaks, index_of_r_values, show_r = R_Peaks.r_peaks_detection(normalised_valueInt, time_one_sample)
    t_time, t_values, show_t, index_of_t_values = T_Peaks.t_peaks_detection(normalised_valueInt, time_one_sample, index_of_r_values, all_peaks)
    p_time, p_values, show_p = P_Peaks.p_peaks_detection(normalised_valueInt, time_one_sample, index_of_r_values,all_peaks)
    t_end_time, t_end_values, show_t_end = T_Peaks.t_end_peaks_detection(normalised_valueInt, time_one_sample, all_peaks, t_values, index_of_t_values)
    Q_time, Q_values, show_q = Q_Peaks.q_peaks_detection(normalised_valueInt, time_one_sample, p_values, r_peaks)
    S_time, S_values, show_s = S_Peaks.s_peaks_detection(normalised_valueInt, time_one_sample, t_values, r_peaks)
    t_start_time, t_start_values, show_t_start = T_Peaks.t_start_peaks_detection(normalised_valueInt, time_one_sample, all_peaks, t_values, index_of_t_values, r_peaks, S_values)
    p_start_time, p_start_values, show_p_start = P_Peaks.p_start_peaks_detection(normalised_valueInt, time_one_sample, all_peaks, p_values, t_values)
    #PCG
    normalised, time_axis_pcg, time_one_sample = S_D.create_wavelet(path_pcg)
    envelope_filtered, allpeaks, peak_time_s1, peak_s1, peak_time_s2, peak_s2 = S_D.s_d_detection(normalised, time_one_sample)
    s1_width_time, s2_width_time = S_D.s1_s2_widths(envelope_filtered, time_one_sample, allpeaks, peak_s1, peak_s2)

    # Information.information(normalised_valueInt, r_peaks_time, p_time, Q_time, S_time, t_time, t_start_time, t_end_time, p_start_time, r_peaks, p_values, Q_values, S_values, t_values, peak_time_s1, peak_time_s2, s1_width_time, s2_width_time)

    # plotting.plotting(time_axis_ecg, normalised_valueInt, normalised, r_peaks_time, r_peaks, p_time, p_values, t_time, t_values,
    #                   t_end_time, t_end_values, t_start_time, t_start_values, Q_time, Q_values, S_time, S_values,
    #                   show_r, show_p, show_q, show_t, show_s, time_axis_pcg, envelope_filtered, peak_time_s1,
    #                   peak_s1, peak_time_s2, peak_s2, s1_width_time, s2_width_time)

    information_thread = threading.Thread(target=Information.information(normalised_valueInt, r_peaks_time, p_time, Q_time, S_time, t_time, t_start_time, t_end_time, p_start_time, r_peaks, p_values, Q_values, S_values, t_values, peak_time_s1, peak_time_s2, s1_width_time, s2_width_time))
    plotting_thread = threading.Thread(target=plotting.plotting(time_axis_ecg, normalised_valueInt, normalised, r_peaks_time, r_peaks, p_time, p_values, t_time, t_values,
                      t_end_time, t_end_values, t_start_time, t_start_values, Q_time, Q_values, S_time, S_values,
                      show_r, show_p, show_q, show_t, show_s, time_axis_pcg, envelope_filtered, peak_time_s1,
                      peak_s1, peak_time_s2, peak_s2, s1_width_time, s2_width_time))
    
    information_thread.start()
    plotting_thread.start()
    information_thread.join()
    plotting_thread.join()

    pdf_gen.generate_pdf()
main()



