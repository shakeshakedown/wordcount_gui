import stop
import tkinter as tk
from tkinter import *
from tkinter import font

class Intro(tk.Tk):
    def __init__(self):
        super().__init__()

        # Attributes
        self.title("Word Frequency")
        self.stop_words = stop.stop_word
        self.punc_to_remove = stop.stop_punc

        # Frames
        self.main_frame = tk.Frame()
        self.main_frame.grid()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.punc_frame = tk.Frame()
        self.punc_frame.grid()

        # Methods
        self.header()
        self.remove_words()

    def header(self):
        frame = self.main_frame
        self.display = tk.Label(frame, text="Word Frequency", font=font.Font(size=30))
        self.display.grid(row=0, column=0, columnspan=3)

    def remove_words(self):
        frame=self.punc_frame
        tk.Label(frame, text="Words to Ignore").grid(row=1)
        row = 2
        curr_column = -1
        for num, word in enumerate(self.stop_words):
            curr_column += 1
            if curr_column >= 8:
                curr_column = 0
                row += 1
            checkbox = Checkbutton(frame, variable=num, text=word)
            checkbox.grid(row=row, column=curr_column, sticky="w")
            checkbox.select()
            

def main():
    launch = Intro()
    launch.mainloop()

if __name__ == "__main__":
    main()