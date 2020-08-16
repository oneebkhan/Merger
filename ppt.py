import win32com.client
import os


class Ex:

    def __init__(self):
        pass

    def ppt_convert(self, folder):
        in_file = folder
        out_file = os.path.splitext(folder)[0]
        powerpoint = win32com.client.Dispatch('Powerpoint.Application')
        pdf = powerpoint.Presentations.Open(in_file, WithWindow=False)
        pdf.SaveAs(out_file, 32)
        pdf.close()
        powerpoint.Quit()
