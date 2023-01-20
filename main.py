import tkinter as tk
import tkinter.filedialog as filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
            ]
    )
    if not file_path:
        window.title("无标题 - 记事本")
        return
    txt_edit.delete("1.0", tk.END)
    with open(
        file_path,
        mode="r",
        encoding="utf-8") as input_file:
        txt_edit.insert(
            tk.END,
            input_file.read()
            )
    window.title(f"{file_path} - 记事本")

def save_as_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
            ]
    )
    if not file_path:
        return
    with open(
        file_path,
        mode="w",
        encoding="utf-8") as output_file:
        output_file.write(txt_edit.get("1.0", tk.END))
    window.title(f"{file_path} - 记事本")

window = tk.Tk()
window.title("记事本")

window.rowconfigure(
    0,
    minsize=100,
    weight=1
    )
window.columnconfigure(
    1,
    minsize=100,
    weight=1
    )

btn_frame = tk.Frame(
    master=window,
    bd=2
    )
btn_open = tk.Button(
    master=btn_frame,
    text="打开",
    command=open_file
    )
btn_save_as = tk.Button(
    master=btn_frame,
    text="另存",
    command=save_as_file
    )

btn_open.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
    )
btn_save_as.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=5
    )
btn_frame.grid(
    row=0,
    column=0,
    sticky="ns"
    )

txt_edit = tk.Text(master=window)
txt_edit.grid(
    row=0,
    column=1,
    sticky="nsew"
    )

window.mainloop()