import tkinter as tk
from tkinter import *
import webbrowser

#Parent window class inherits from tkinter "Frame" class
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #creates button to create the Default HTML page and places it on the grid
        self.btn_default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2, column=3, padx=(10,10) , pady=(10,10))
        #creates button to create HTML page with custom user input text
        self.btn_custom = Button(self.master, text="Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.btn_custom.grid(row=2, column=2, padx=(10,10),pady=(10,10))

        #this is for input box and label
        self.lbl_userText = tk.Label(self.master,text='Enter Custom text or click Default HTML page button.')
        self.lbl_userText.grid(row=0, column=0,padx=(10,0),pady=(10,0),sticky=N+W)
        self.txt_userText = tk.Entry(self.master,text='')
        self.txt_userText.grid(row=1, column=0, columnspan=4,padx=(10,10),pady=(10,0),sticky=N+E+W)
        
    #defines the function that allows the btn_default button to create an html file and open it.  
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #defines a funciton that allows the btn_custom button to create an html file using user entered text and open it.
    def customHTML(self):
        var_customText = self.txt_userText.get()    #creates a variable by returning the text entered into txt_userText
        customFile = open("index.html", "w")
        customContent = "<html>\n<body>\n<h1>" + var_customText + "</h1>\n</body>\n</html>"
        customFile.write(customContent)
        customFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
