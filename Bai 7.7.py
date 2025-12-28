# Câu 7.  Dương Văn Quỳnh - 24174600058 - Lớp DHKL18A1HN
import tkinter as tk

window = tk.Tk()
window.title("Tiêu đề cửa sổ")

var = tk.IntVar()

checkbutton = tk.Checkbutton(
    window,
    text="Chọn",
    variable=var,
    command=lambda: label.config(
        text="Trạng thái: Chọn" if var.get() == 1 else "Trạng thái: Không chọn"
    )
)
checkbutton.pack()

label = tk.Label(window, text="Trạng thái: Không chọn")
label.pack()

window.mainloop()
