import json

def information(normalised_valueInt, r_peaks_time, p_time, Q_time, S_time, t_time, t_start_time, t_end_time, p_start_time, r_peaks, p_values, Q_values, S_values, t_values, peak_time_s1, peak_time_s2, s1_width_time, s2_width_time):
    #ECG
    rr_interval = [y - x for x, y in zip(r_peaks_time[:-1], r_peaks_time[1:])]
    bpm = round(60 / (sum(rr_interval) / len(rr_interval)), 0)

    QT_interval = sum([t_end_time[i + 1] - Q_time[i] for i in range(len(Q_time) - 1)]) / (len(Q_time) - 1)
    QT_interval = round(QT_interval * 1000, 1)

    ST_segment = [t_start_time[i] - S_time[i] for i in range(len(S_time)) if t_start_time[i] - S_time[i] != 0]
    if len(ST_segment) != 0:
        ST_segment = round(sum(ST_segment) * 1000/ len(ST_segment), 1)
    else:
        ST_segment = 0

    details_p = [(p_time[i], round(normalised_valueInt[p_values[i]], 4)) for i in range(len(p_values))]
    details_q = [(Q_time[i], round(normalised_valueInt[Q_values[i]], 4)) for i in range(len(Q_values))]
    details_r = [(r_peaks_time[i], round(normalised_valueInt[r_peaks[i]], 4)) for i in range(len(r_peaks))]
    details_s = [(S_time[i], round(normalised_valueInt[S_values[i]], 4)) for i in range(len(S_values))]
    details_t = [(t_time[i], round(normalised_valueInt[t_values[i]], 4)) for i in range(len(t_values))]

    rr_interval = round(sum(rr_interval) * 1000 / len(rr_interval), 1)

    QRS_complex = sum([S_time[i + 1] - Q_time[i] for i in range(len(Q_time) - 1)]) / (len(Q_time) - 1)
    QRS_complex = round(QRS_complex * 1000, 1)

    QTC = QT_interval / rr_interval
    QTC = round(QTC * 1000, 1)

    PR_interval = sum([Q_time[i] - p_start_time[i] for i in range(len(p_start_time))]) / len(p_start_time)
    PR_interval = round(PR_interval * 1000, 1)

    #PCG
    s1_s2_interval = sum([peak_time_s2[i] - peak_time_s1[i] for i in range(len(peak_time_s2))]) / len(peak_time_s2)
    s1_s2_interval = round(s1_s2_interval* 1000, 1)

    s1_avg_width = [s1_width_time[i + 1] - s1_width_time[i] for i in range(0, len(s1_width_time) - 1, 2)]
    s1_avg_width = round(sum(s1_avg_width) * 1000 / len(s1_avg_width), 1)

    s2_avg_width = [s2_width_time[i + 1] - s2_width_time[i] for i in range(0, len(s2_width_time) - 1, 2)]
    s2_avg_width = round(sum(s2_avg_width) * 1000/ len(s2_avg_width), 1)

    # print('ECG Analysis')
    # print('BPM - ', bpm)
    # print('PR Interval - ', PR_interval, 'ms')
    # print('RR Interval - ', rr_interval, 'ms')
    # print('QT Interval - ', QT_interval, 'ms')
    # print('ST Segment - ', ST_segment, 'ms')
    # print('QRS Complex - ', QRS_complex, 'ms')
    # print('QT꜀ - ', QTC, 'ms')
    # '''
    # print('P Peaks - ', details_p)
    # print('Q Peaks - ', details_q)
    # print('R Peaks - ', details_r)
    # print('S Peaks - ', details_s)
    # print('T Peaks - ', details_t)
    # '''
    # print('PCG Analysis')
    # print('Avg. S1 Width - ', s1_avg_width, 'ms')
    # print('Avg. S2 Width - ', s2_avg_width, 'ms')
    # print('S1-S2 Avg. Interval - ', s1_s2_interval, 'ms')

    if bpm < 60:
        if 80 < QRS_complex < 120:
            print('Sinus Bradycardia')
    elif 100 < bpm < 200:
        if 120 < QRS_complex < 170:
            print('Sinus Tachycardia')
        if 80 < QRS_complex < 100:
            print('Atrial Fibrillation')
    elif bpm > 200:
        if QRS_complex < 120:
            print('Ventricular Tachycardia')

    dictionary = {'BPM' : bpm, 'PR_Interval' : PR_interval, 'RR_Interval' : rr_interval, 'QT_Interval' : QT_interval, 'ST_Segment' : ST_segment,
                  'QRS_Complex' : QRS_complex, 'QTC' : QTC, 'S1_Width' : s1_avg_width, 'S2_Width' : s2_avg_width, 'S1-S2_Avg' : s1_s2_interval}

    json_object = json.dumps(dictionary)

    with open("C:/Users/Administrator/Desktop/larkai/Cardio/info.json", "w") as outfile:
        outfile.write(json_object)