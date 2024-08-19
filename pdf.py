#1 find a library that can process pdf.
import PyPDF2

with open('dummy.pdf','rb') as file: #rb = Read Binary (Binary in python)
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0) # get the first page and assign to "page"  
    page.rotateCounterClockwise(90) #rotate -90 in computer memory
    writer = PyPDF2.PdfFileWriter() #allow us to write a object
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file: # write in binary 
        writer.write(new_file)