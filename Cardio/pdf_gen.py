from reportlab.pdfgen import canvas
import json
from PIL import Image
import numpy as np
from PyPDF2 import PdfFileWriter, PdfFileReader

def generate_pdf():
    c = canvas.Canvas("C:/Users/Administrator/Desktop/larkai/static/out.pdf")

    with open('info.json', 'r') as openfile:
        json_object = json.load(openfile)

    c.drawImage("C:/Users/Administrator/Desktop/larkai/static/img/larkai.png", 15, 790, width=180, preserveAspectRatio=True, mask='auto')
    c.rotate(270)

    img = Image.open('C:/Users/Administrator/Desktop/larkai/static/img/final.png')
    ary = np.array(img)

    # Split the three channels
    r, g, b, _ = np.split(ary, 4, axis=2)
    r = r.reshape(-1)
    g = r.reshape(-1)
    b = r.reshape(-1)

    # Standard RGB to grayscale
    bitmap = 0.299 * r + 0.587 * g + 0.114 * b
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float), 255)
    im = Image.fromarray(bitmap.astype(np.uint8))

    im.save('C:/Users/Administrator/Desktop/larkai/static/img/greyscale.bmp')

    c.drawImage("C:/Users/Administrator/Desktop/larkai/static/img/greyscale.bmp", -810, -332, width=400, preserveAspectRatio=True)

    c.setFont("Helvetica", 15)

    c.drawString(-405, 190, 'ECG Analysis')
    c.line(-405, 188, -310, 188)

    c.drawString(-280, 190, 'PCG Analysis')
    c.line(-280, 188, -185, 188)

    c.setFont("Helvetica", 12)

    c.drawString(-405, 170, 'BPM: ' + str(json_object['BPM']))
    c.drawString(-405, 150, 'PR Interval: ' + str(json_object['PR_Interval']))
    c.drawString(-405, 130, 'RR Interval: ' + str(json_object['RR_Interval']))
    c.drawString(-405, 110, 'QT Interval: ' + str(json_object['QT_Interval']))
    c.drawString(-405, 90, 'ST Segment: ' + str(json_object['ST_Segment']))
    c.drawString(-405, 70, 'QRS Complex: ' + str(json_object['QRS_Complex']))
    c.drawString(-405, 50, 'QTC: ' + str(json_object['QTC']))

    c.drawString(-280, 170, 'Avg. S1 Width: ' + str(json_object['S1_Width']))
    c.drawString(-280, 150, 'Avg. S2 Width: ' + str(json_object['S2_Width']))
    c.drawString(-280, 130, 'S1-S2 Avg. Interval: ' + str(json_object['S1-S2_Avg']))

    c.save()

    with open("C:/Users/Administrator/Desktop/larkai/static/out.pdf", "rb") as in_f:
        input1 = PdfFileReader(in_f)
        output = PdfFileWriter()

        page = input1.getPage(0)
        # print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.cropBox.lowerLeft = (0, 120)
        page.cropBox.upperRight = (210, 850)
        output.addPage(page)

        with open("C:/Users/Administrator/Desktop/larkai/static/report.pdf", "wb") as out_f:
            output.write(out_f)