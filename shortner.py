# Tyler Earps
# July 10, 2023
# URL shortner that cuts off the first part of a URL to practice using TKInter for gui development

#TKInter Library used for GUI
from tkinter import *

# Functions:

# Shortens the URL
def shortenURL(URL):
    URL = URL.replace('Please enter the URL you want shortened: ', '')
    URL = URL.replace('https://', '')
    URL = URL.replace('http://', '')
    URL = URL.replace('www.', '')

    return URL

# Starts the shorting process
def shorten():
    URL = textInput.get(1.0, "end-1c")

    URL = shortenURL(URL)

    textFinal.config(state=NORMAL)
    textFinal.delete(1.0, "end")
    textFinal.insert(1.0, URL)
    textFinal.config(state=DISABLED)


# Main

# Sets up basic GUI window for program to function with 2 text boxes, one for input, one for output
root = Tk()
root.title("URL Shortner")

label1 = Label(root, text="Please enter the URL you want shortened: ")
label1.pack()

textInput = Text(root, height=3)
textInput.pack()

label2 = Label(root, text="Shortened URL:")
label2.pack()

textFinal = Text(root, height=3)
textFinal.pack()

button = Button(root, text="Shorten", command=shorten)
button.pack()

root.mainloop()