#pip install pyttsx3 pdfplumber PyPdf2

#get the file name and location of the file
import PyPDF2
import pdfplumber
import pyttsx3


file = "HiWorld.pdf"
#create a pdf file object
pdfFileObj = open(file,'rb')  #rb meant for opening file in binary format
#create a pdf file reader object
PdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#get the number of pages
pages = PdfReader.numPages
#create a pdfplumber object and loop through the number of pages in the pdf file
with pdfplumber.open(file) as pdf:
    #loop through the number of pages
    for i in range(0,pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
    speaker = pyttsx3.init()  #pyttsx3 is python text speech package
    speaker.say(text)
    speaker.runAndWait()
