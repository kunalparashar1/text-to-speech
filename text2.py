import tkinter as tk
import pyttsx3

engine = pyttsx3.init('sapi5')

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('TTS')
        self.root.resizable(1, 1)
        self.label1 = tk.Label(self.root, text='What do you want me to speak?')
        self.label1.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text='Speak!', command=self.clicked)
        self.button.pack()
        self.root.mainloop()

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

if __name__ == '__main__':
    widget = Widget()