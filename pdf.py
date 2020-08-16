import PyPDF2 as pd
import glob
from natsort import natsorted

class PDF:

    def __init__(self):
        pass

    def p(self, folder, output_merge):
        pdfs = glob.glob(folder + '/*.pdf')
        new_merged_pdf = f'{output_merge}' + '/new_merged.pdf'

        merge_pdfs = pd.PdfFileMerger()

        for pdf in natsorted(pdfs):
            # 'rb' open for reading (default), binary mode
            merge_pdfs.append(open(pdf, 'rb'))

        # 'wb' open for writing, binary mode
        merge_pdfs.write(open(new_merged_pdf, 'wb'))

        # reading only text
        # extract text from pdf
        read_pdf = pd.PdfFileReader(open(f'{output_merge}/new_merged.pdf', 'rb'))
        # pages begin at zero
        pdf_get_page = read_pdf.getPage(0)
        pdf_get_page.extractText()