from tkinter import*
import webbrowser

main = Tk()
main.title("Browser")
main.geometry("800x600")

def google():
    webbrowser.open("www.google.com")
def linkdin():
    webbrowser.open("www.linkedin.com")
def youtube():
    webbrowser.open("www.youtube.com")
def instagram():
    webbrowser.open("www.instagram.com")

opengoogle = Button(text="Open google", command=google).pack(pady=10)
openlinkdin = Button(text="Open Linkdin", command=linkdin).pack(pady=10)
openyoutube = Button(text="Open Youtube", command=youtube).pack(pady=10)
openinstagram = Button(text="Open Instagram", command=instagram).pack(pady=10)

main.mainloop()

