import PyPDF2

##1 crap/read wtr.pdf and super.pdf
template = PyPDF2.PdfFileReader(open('super.pdf','rb')) #read binary
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):# if 5 pages - loop 5 times
    page = template.getPage(i) # get each page
    page.mergePage(watermark.getPage(0)) # merge the only page in wtr
    output.addPage(page) #adding each page to "output" object

    with open('watermarked_output.pdf','wb') as file:
        output.write(file) #write output to a file


