import os
from tkinter import filedialog
from tkinter import *

from ppt import Ex
from pdf import PDF


root = Tk()
root.title = 'Merger'
root.geometry('200x200')
root.withdraw()


def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)
    return tempdir

file_path_variable = search_for_file_path()
print("\nfile_path_variable = ", file_path_variable)
# finds path of files




# making an output directory for pdf merged
output_merge = file_path_variable + '/output_merged'
if not os.path.exists(output_merge):
    os.mkdir(output_merge)




for subdir, dirs, files in os.walk(file_path_variable):
    for filename in files:
        filepath = subdir + os.sep + filename
        print(filepath)

        ppt = Ex()

        if filepath.endswith(".ppt"):
            folder = filepath.replace('/', '\\')
            ppt.ppt_convert(folder)

        if filepath.endswith(".pptx"):
            folder = filepath.replace('/', '\\')
            ppt.ppt_convert(folder)

        if filepath.endswith(".pptm"):
            folder = filepath.replace('/', '\\')
            ppt.ppt_convert(folder)

pdf = PDF()
pdf.p(file_path_variable, output_merge.replace('/', '\\'))

root.mainloop()
