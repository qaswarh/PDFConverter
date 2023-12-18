mport pyttsx3
import pdfplumber


def ch_text(f, n, m):
    print(n)
    print(m)
    with pdfplumber.open(f) as pdf:
        text = ''
        for i in range(n, m):
            page = pdf.pages[i]
            text += page.extract_text()
        return text


print('This Python program will convert number of pages from pdf file into MP3 file')
acf = input("Please enter file name with .pdf extension: ")
mp3 = input("Please enter output file name with .mp3 extension: ")
sp = input("Please enter start page number: ")
s = int(sp)-1
ep = input("Please enter end page number: ")
e = int(ep)
chapter = ch_text(acf, s, e)
# print(chapter)
engine = pyttsx3.init()
engine.save_to_file(chapter, mp3)
engine.runAndWait()
