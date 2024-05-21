from tokenizer import tokenize
import json
from tkinter import *
import tkinter.scrolledtext as st
import re
import tkinter as tk
from tkinter import ttk
from poland2 import reverse
def write_txt(data):
    with open('data/R.txt','w') as file:
        file.write(data)

def clicked():
    write_txt(codetxt.get("1.0", "end"))

    tokenstext.delete("1.0", END)
    Wtext.delete("1.0", END)
    Rtext.delete("1.0", END)
    Otext.delete("1.0", END)
    Ntext.delete("1.0", END)
    Itext.delete("1.0", END)
    Ctext.delete("1.0", END)

    tokenize()

    fw = open('data/W.json', 'r')
    textw = fw.read()
    textw = textw.replace("    ", "")
    textw = textw.replace('"', "")
    textw = textw.replace(',', "")
    textw = textw[2:-1]
    Wtext.insert("1.0", textw)
    fw.close()

    fr = open('data/R.json', 'r')
    textr = fr.read()
    textr = textr.replace("    ", "")
    textr = textr.replace('"', "")
    regex = r'(?<!,),(?!,)'
    textr = re.sub(regex, '', textr)
    textr = textr[2:-1]
    Rtext.insert("1.0", textr)
    fr.close()

    fo = open('data/O.json', 'r')
    texto = fo.read()
    texto = texto.replace("    ", "")
    texto = texto.replace('"', "")
    texto = texto.replace(',', "")
    texto = texto[2:-1]
    Otext.insert("1.0", texto)
    fo.close()

    fn = open('data/N.json', 'r')
    textn = fn.read()
    textn = textn.replace("    ", "")
    textn = textn.replace('"', "")
    textn = textn.replace(',', "")
    textn = textn[2:-1]
    Ntext.insert("1.0", textn)
    fn.close()

    fi = open('data/I.json', 'r')
    texti = fi.read()
    texti = texti.replace("    ", "")
    texti = texti.replace('"', "")
    texti = texti.replace(',', "")
    texti = texti[2:-1]
    Itext.insert("1.0", texti)
    fi.close()

    fc = open('data/C.json', 'r')
    textc = fc.read()
    textc = textc.replace("    ", "")
    textc = textc.replace('"', "")
    textc = textc.replace(',', "")
    textc = textc.replace("\\", "")
    textc = textc[2:-1]
    Ctext.insert("1.0", textc)
    fc.close()

    f4 = open('data/tokens.txt', 'r')
    text = f4.read()
    tokenstext.insert("1.0", text)
    f4.close()



def reversed():
    write_txt(code2txt.get("1.0", "end"))

    polandtext.delete("1.0", END)
    f5 = open('reverse_polish_entry.txt', 'r')
    text = f5.read()
    polandtext.insert("1.0", text)
    f5.close()



WIDTH = 1480
HEIGHT = 720
PADDING = 40
NWIDTH = WIDTH - PADDING * 2
NHEIGHT = HEIGHT - PADDING * 2

LWINDOWHEIGHT = 300
LWINDOWWIDTH = 600

SWINDOWHEIGHT = 200
SWINDOWWIDTH = 200


BUTTONPADDING = 40

BUTTONWIDTH = 120
BUTTONHEIGHT = 80



window = Tk()
window.title("LR1")
window.geometry(f'{WIDTH}x{HEIGHT}')

notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

# Создаем две вкладки
LR1 = ttk.Frame(notebook)
LR2 = ttk.Frame(notebook)

notebook.add(LR1, text='Токенизация')
notebook.add(LR2, text='Обратная польская нотация')


codetxt = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
codetxt.place(x=PADDING, y=PADDING,
              width=LWINDOWWIDTH, height=LWINDOWHEIGHT)

tokenstext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
tokenstext.place(x=PADDING + BUTTONPADDING * 2 + LWINDOWWIDTH + BUTTONWIDTH, y=PADDING,
                 width=LWINDOWWIDTH, height=LWINDOWHEIGHT)

Wlb = Label(LR1, text="Лексемы служебных слов:", font=("Cascadia Code", 12))
Wlb.place(x=PADDING, y=LWINDOWHEIGHT + PADDING * 2)
Wtext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
Wtext.place(x=PADDING, y=LWINDOWHEIGHT + PADDING * 3,
            width=SWINDOWWIDTH, height=SWINDOWHEIGHT)

Rlb = Label(LR1, text="Лексемы разделителей:", font=("Cascadia Code", 12))
Rlb.place(x=PADDING * 2 + SWINDOWWIDTH, y=LWINDOWHEIGHT + PADDING * 2)
Rtext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
Rtext.place(x=PADDING * 2 + SWINDOWWIDTH, y=LWINDOWHEIGHT + PADDING * 3,
            width=SWINDOWWIDTH, height=SWINDOWHEIGHT)

Olb = Label(LR1, text="Лексемы операций:", font=("Cascadia Code", 12))
Olb.place(x=PADDING * 3 + SWINDOWWIDTH * 2, y=LWINDOWHEIGHT + PADDING * 2)
Otext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
Otext.place(x=PADDING * 3 + SWINDOWWIDTH * 2, y=LWINDOWHEIGHT + PADDING * 3,
            width=SWINDOWWIDTH, height=SWINDOWHEIGHT)

Nlb = Label(LR1, text="Лексемы числовых констант:", font=("Cascadia Code", 12))
Nlb.place(x=PADDING * 4 + SWINDOWWIDTH * 3, y=LWINDOWHEIGHT + PADDING * 2)
Ntext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
Ntext.place(x=PADDING * 4 + SWINDOWWIDTH * 3, y=LWINDOWHEIGHT + PADDING * 3,
            width=SWINDOWWIDTH, height=SWINDOWHEIGHT)

Ilb = Label(LR1, text="Лексемы идентификаторов:", font=("Cascadia Code", 12))
Ilb.place(x=PADDING * 5 + SWINDOWWIDTH * 4, y=LWINDOWHEIGHT + PADDING * 2)
Itext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
Itext.place(x=PADDING * 5 + SWINDOWWIDTH * 4, y=LWINDOWHEIGHT + PADDING * 3,
            width=SWINDOWWIDTH, height=SWINDOWHEIGHT)

Clb = Label(LR1, text="Лексемы символьных констант:", font=("Cascadia Code", 12))
Clb.place(x=PADDING * 6 + SWINDOWWIDTH * 5, y=LWINDOWHEIGHT + PADDING * 2)
Ctext = st.ScrolledText(LR1, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
Ctext.place(x=PADDING * 6 + SWINDOWWIDTH * 5, y=LWINDOWHEIGHT + PADDING * 3,
            width=SWINDOWWIDTH, height=SWINDOWHEIGHT)

btngo = Button(LR1, text="Выполнить \n преобразование", command=clicked, font=("Cascadia Code", 9), relief="solid", borderwidth=2)
btngo.place(x=PADDING * 2 + LWINDOWWIDTH, y=PADDING * 3, width=BUTTONWIDTH, height=BUTTONHEIGHT)

code2txt = st.ScrolledText(LR2, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
code2txt.place(x=PADDING, y=PADDING,
              width=LWINDOWWIDTH, height=LWINDOWHEIGHT)

polandtext = st.ScrolledText(LR2, relief="solid", borderwidth=2, font=("Cascadia Code", 12))
polandtext.place(x=PADDING + BUTTONPADDING * 2 + LWINDOWWIDTH + BUTTONWIDTH, y=PADDING,
                 width=LWINDOWWIDTH, height=LWINDOWHEIGHT)

btnpol = Button(LR2, text="Выполнить \n преобразование", command=reversed(), font=("Cascadia Code", 9), relief="solid", borderwidth=2)
btnpol.place(x=PADDING * 2 + LWINDOWWIDTH, y=PADDING * 3, width=BUTTONWIDTH, height=BUTTONHEIGHT)


window.mainloop()


