import matplotlib.pyplot as plt
import numpy as np

def plotting(time_axis_ecg, normalised_valueInt, normalised, r_peaks_time, r_peaks, p_time, p_values, t_time, t_values, t_end_time, t_end_values, t_start_time, t_start_values, Q_time, Q_values, S_time, S_values, show_r, show_p, show_q, show_t, show_s, time_axis_pcg, envelope_filtered, peak_time_s1, peak_s1, peak_time_s2, peak_s2, s1_width_time, s2_width_time):
    # To increase the size of the figure plot
    from pylab import rcParams
    rcParams['figure.figsize'] = 20, 10
    fig, (ax1, ax2) = plt.subplots(2, 1)

    plt.setp(ax1.spines.values(), linewidth=5)
    plt.setp(ax2.spines.values(), linewidth=5)

    ax1.set_xticks(np.arange(0, 20, 0.4))

    
    # Plotting the Data
    ax1.plot(time_axis_ecg, normalised_valueInt)

    
    ax1.set_ylabel("ECG", fontsize=18)

    ax2.plot(time_axis_pcg, normalised)

    ax2.set_xlabel("Time (in secs.)", fontsize=18)
    ax2.set_ylabel("PCG", fontsize=18)

    plt.subplots_adjust(hspace=.0)
    plt.savefig("C:/Users/Administrator/Desktop/larkai/static/img/final.png", bbox_inches = 'tight', pad_inches = 0.2, orientation = 'landscape')
