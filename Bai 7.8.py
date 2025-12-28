# Câu 8.  Dương Văn Quỳnh - 24174600058 - Lớp DHKL18A1HN
import tkinter as tk


def cac_uoc_cua_so_nguyen(n):
    uocs = []
    for i in range(1, n + 1):
        if n % i == 0:
            uocs.append(i)
    return uocs


def xuat_cac_uoc(n, entry_ketqua):
    uocs = cac_uoc_cua_so_nguyen(int(n))
    entry_ketqua.delete(0, tk.END)
    entry_ketqua.insert(0, " ".join(map(str, uocs)))


def main():
    root = tk.Tk()
    root.title("Liệt kê các ước của một số nguyên")

    label_n = tk.Label(root, text="Nhập giá trị của N:")
    entry_n = tk.Entry(root)
    label_n.grid(row=0, column=0)
    entry_n.grid(row=0, column=1)

    label_ketqua = tk.Label(root, text="Các ước của N là:")
    entry_ketqua = tk.Entry(root)
    label_ketqua.grid(row=2, column=0)
    entry_ketqua.grid(row=2, column=1)

    button_submit = tk.Button(
        root,
        text="Xác nhận",
        command=lambda: xuat_cac_uoc(entry_n.get(), entry_ketqua)
    )
    button_submit.grid(row=1, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
