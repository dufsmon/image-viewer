from pillow_heif import register_heif_opener
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

register_heif_opener()

def open_heic_image():
    file_path = filedialog.askopenfilename(filetypes=[('HEIC Files', '*.heic')])
    if file_path:
        image = Image.open(file_path)
        display_image(image)

def display_image(image):
    image.thumbnail((800, 600))
    img_tk = ImageTk.PhotoImage(image)
    label.config(image=img_tk)
    label.image = img_tk

def create_gui():
    global label

    root = tk.Tk()
    root.title('HEIC Schimager')
    root.geometry('800x600')

    open_button = tk.Button(root, text='Open HEIC Image', command=open_heic_image)
    open_button.pack()

    label = tk.Label(root)
    label.pack(expand=True)

    root.mainloop()

if __name__ == '__main__':
    create_gui()
