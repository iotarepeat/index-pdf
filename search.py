import os
from tkinter import *
import PyPDF2
import pickle
import time
import re


def indexFile(fileName):
    '''
    Using PyPDF2 it creares a list of text in all pages
    We create a dictionary of sets, in which keys are words
    EG:
    If word apple occurs on page, 5,7 and 8:
    dict = {'apple':(5,7,8)}

    '''
    f = open(fileName, 'rb')
    document = PyPDF2.PdfFileReader(f)
    index = {}
    for i in range(document.getNumPages()):
        text = document.getPage(i).extractText()
        words = pattern.findall(text)
        for w in words:
            try:
                index[w].add(i)
            except KeyError:
                index[w] = set()
                index[w].add(i)
    f.close()
    return index


def writeIndex(fileName, index):
    ''''
                    Simply saves the index variable to fileName
    '''
    with open(fileName+".index", 'wb') as f:
        pickle.dump(index, f)


def loadIndex(fileName):
    '''
    Returns index if it exists,
    else indexes the pdf, saves the index and then returns
    '''
    try:
        f = open(fileName+'.index', 'rb')
        index = pickle.load(f)
    except FileNotFoundError:
        console.insert(END, "Indexing %s...." % (fileName)+"\n")
        start = time.time()
        index = indexFile(fileName)
        console.insert(END, "Done Indexing.... in %0.4f\n" %
                       (time.time()-start))
        writeIndex(fileName, index)
    return index


def search(term, file):
    ''''
                    Uses linear search on the list: index
                    It matches substring, i.e Hell matches with HELL, Hello, chell, CHELLO
    '''
    index = loadIndex(file)
    term = term.upper().split(" ")
    pages = index[term[0]]
    for i in term[1:]:
        pages.intersection_update(index[i])
    for i in pages:
        console.insert(END, "Page {} in {}\n".format(i+1, file))


def pdfFiles():
    '''
     Return a list of files ending with .pdf
    '''
    pdfs = []
    for i in os.listdir():
        if i[-4:] == ".pdf":
            pdfs.append(i)
    return pdfs


def multisearch():
    '''
                    Search in all selected pdf's
    '''
    docs = [lb.get(i) for i in lb.curselection()]
    term = e.get()
    console.delete('1.0', END)
    for d in docs:
        search(term, d)


pattern = re.compile(r'[A-Z]\w+')  # To match wverything use \w+
# GUI
root = Tk()
root.title("Index a pdf file")
lb = Listbox(selectmode=MULTIPLE)
for val in pdfFiles():
    lb.insert(END, val)
f = Frame(root)
Label(f, text="Query: ").pack(side=LEFT)
e = Entry(f)
e.pack(side=RIGHT)
f.pack()
lb.pack()
console = Text(height=10, width=30)
console.pack()
Button(text="Search", command=multisearch).pack()
root.mainloop()
