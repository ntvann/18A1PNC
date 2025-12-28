# Câu 5.  Dương Văn Quỳnh - 24174600058 - Lớp DHKL18A1HN
import tkinter as tk
from PIL import Image, ImageTk


window = tk.Tk()
window.title("Chương trình xem ảnh")

image = Image.open("oto.png")


new_size = (400, 400)
image = image.resize(new_size, Image.Resampling.LANCZOS)


img = ImageTk.PhotoImage(image)

label = tk.Label(window, image=img)
label.image = img   
label.pack()

window.mainloop()
