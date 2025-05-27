#!/usr/bin/env python

from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askokcancel
import tkinter.messagebox
import m2secret
import codecs
import platform
import base64
import os, sys


class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text="Quit", command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def quit(self):
        ans = askokcancel("Verify exit", "Really quit?")
        if ans:
            Frame.quit(self)


class ScrolledText(Frame):
    def __init__(self, parent=None, text="", file=None, k=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text, file, k)

    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def settext(self, text="", file=None, k=None):
        if file and k:
            f = open(file, "r")
            self.text.delete("1.0", END)
            self.text.insert("1.0", text)
            serialized = f.read()
            f.close()
            try:
                # print(k)
                password = k
                secret = m2secret.Secret()
                secret.deserialize(serialized)
                data = secret.decrypt(password)
                self.text.delete("1.0", END)
                self.text.insert(INSERT, data)
                tk.wm_title("CT - Cryptext - " + file)
            except:
                # tkMessageBox.showinfo("Wrong Crypt Key", "Wrong Crypt Key")
                print("Wrong Crypt Key")

        # self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def gettext(self):
        return self.text.get("1.0", END + "-1c")


class SimpleEditor(ScrolledText):
    def __init__(self, parent=None, file=None, k=None):
        self.filename = ""
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text="Open", command=self.onOpen).pack(side=LEFT)
        Button(frm, text="Save", command=self.onSave).pack(side=LEFT)
        Button(frm, text="Cut", command=self.onCut).pack(side=LEFT)
        Button(frm, text="Copy", command=self.onCopy).pack(side=LEFT)
        Button(frm, text="Paste", command=self.onPaste).pack(side=LEFT)
        Button(frm, text="Find", command=self.onFind).pack(side=LEFT)
        self.password = StringVar()
        self.entry = Entry(frm, text="", textvariable=self.password).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        if k:
            self.password.set(k)
        ScrolledText.__init__(self, parent, file=file, k=k)
        self.text.config(font=("courier", 9, "normal"))

    def onOpen(self):
        filename = askopenfilename(
            filetypes=[("Cryptext", "*.ct")], initialfile=self.filename
        )
        if filename:
            f = open(filename, "r")
            serialized = f.read()
            f.close()
            try:
                password = self.password.get()
                secret = m2secret.Secret()
                secret.deserialize(serialized)
                # print("xxxxxxxxxxxxxx")
                # print(password)
                # print("xxxxxxxxxxxxxx")
                data = secret.decrypt(password)

                self.text.delete("1.0", END)
                self.text.insert(INSERT, data)
                self.filename = filename
                tk.wm_title("CT - Cryptext - " + filename)

            except:
                # tkMessageBox.showinfo("Wrong Crypt Key", "Wrong Crypt Key")
                print("Wrong Crypt Key")

    def onSave(self):
        filename = asksaveasfilename(
            filetypes=[("Cryptext", "*.ct")], initialfile=self.filename
        )
        if filename:
            alltext = str(self.gettext())
            secret = m2secret.Secret()
            secret.encrypt(alltext, self.password.get())
            serialized = secret.serialize()
            filename = filename.replace(".ct", "")
            filename = filename + ".ct"
            self.filename = filename
            open(filename, "wb").write(serialized)

    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)
        self.text.delete(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(text)

    def onCopy(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(text)

    def onPaste(self):
        try:
            text = self.selection_get(selection="CLIPBOARD")
            self.text.insert(INSERT, text)
        except TclError:
            pass

    def onFind(self):
        target = askstring("CT-Cryptext", "Search String?")
        if target:
            where = self.text.search(target, INSERT, END)
            if where:
                print(where)
                pastit = where + ("+%dc" % len(target))
                # self.text.tag_remove(SEL, '1.0', END)
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()


def displayText():
    k = entryWidget.get().strip()
    entryWidget.destroy()
    button.destroy()
    entryLabel.destroy()
    textFrame.destroy()
    SimpleEditor(file=sys.argv[1], k=k).mainloop()


if __name__ == "__main__":
    tk = Tk()
    tk.wm_title("CT - Cryptext")
    if platform.system() == "Windows":
        icon = """AAABAAEAICAQAAEABADoAgAAFgAAACgAAAAgAAAAQAAAAAEABAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAIiIiAAAzZgBEREQAZmZmADNmmQCIiIgAZpnMAKqqqgDMzMwA////AAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAJVVXAAAAAAAAAAAlUgAAACVVcAAAAAAAAAAiVVVSAAJVVwAA
        AAAAAAAAJSIlVSAlUlcAAAAAAAAAAFIKAlVQIlVwAAAAAAAAAAJQAAAlUgJVcAAAAAAAAAAFIKM6
        AlUgJXAAAAAAAAAAIpMQATYlUhIAAAAAAAAAAlESVVIQBVUhAAEAAAAAAAIlVVEVVVFVUgACAAAA
        AAAlVVVRVVVVVVUgEAAAEAAAJVV3IVJXd3UlUSAAACAAACV3EREgEREndVIAAAFwAAdXEBEBIAgR
        ASdVAAACAAAHcQGAAiEAQQARdQAAJwAAB1EEAAJRAAAAASUgEgAAAAcQAAASUhAAAAAVUAAAAAAF
        EAAAJVUhAAAAFVAAAAAAAgAAASVVUhAAAAVRAAAAAAIAABJVVVUhAAAFUgAAAAAAEBIlVVJVUiEA
        BVIAAAAAACIlVVVRJVVSIhVVAAAAAAB3VVJVVVVVVVUlVQAAACAAB3VRJVVVVVVVVVIAACJwAAB3
        VVVVJVVSVVVSEiV3AAAAd1UlVRJVUSVVUSVwAAAAAAd3VVVVVVVVVVAAAAAAAAAAB3dSVVJVVVUA
        AAAAAAAAAAAHd3VVVVdxAAAAAAAAAAAAAAB3d3cAF1IAAAAAAAAAAAAAAAAAAAAHdSAAAAAAAAAA
        AAAAAAAAAAAAAAD/D4B//AOA//gBAf/4AAH/+AADf/AAA3/wAAJ74AAGe8AABHPAAARzgAAA44AA
        AOOAAAHDAAABxwAAAQcAAAAPAAAAPwAAAP8AAAB+AAAAfoAAAHyAAAB8gAAAcMAAAADgAAAB4AAA
        A/AAAB/4AAH//gAA//+AAB//8DAH///+AQ==
        """
        icondata = base64.b64decode(icon)

        tempFile = "icon.ico"
        iconfile = open(tempFile, "wb")
        iconfile.write(icondata)
        iconfile.close()
        tk.wm_iconbitmap(tempFile)
        os.remove(tempFile)

    try:
        if sys.argv[1]:
            frame = Frame(tk)
            tk.title("CT-Cryptext")
            textFrame = Frame(tk)
            entryLabel = Label(textFrame)
            entryLabel["text"] = "Enter Key:"
            entryLabel.pack(side=LEFT)
            entryWidget = Entry(textFrame)
            entryWidget["width"] = 50
            entryWidget.pack(side=LEFT)
            textFrame.pack()
            button = Button(tk, text="Submit", command=displayText)
            button.pack()
            tk.mainloop()

    except IndexError:
        SimpleEditor().mainloop()
