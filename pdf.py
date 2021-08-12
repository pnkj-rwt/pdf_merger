import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)

base = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(base.getNumPages()):
    page = base.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('marked.pdf', 'wb') as file:
    output.write(file)