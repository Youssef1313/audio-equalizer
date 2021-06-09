import tkinter as tk
import soundfile as sf
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

data, fs = sf.read(file_path)
