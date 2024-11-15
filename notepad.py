import tkinter as tk
from tkinter.filedialog import *

def save_file():
    file_location = asksaveasfilename(
        defaultextension= "txt",
        filetypes= [("Text files", "*.txt"),("All files", "*.*")]
        )
    if not file_location:
        return
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"My Daily Notes - {file_location}")

def opening_file():
    file_location = askopenfilename(
        filetypes= [("Text files", "*.txt"),("All files", "*.*")]
    )
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"My Daily Notes - {file_location}")

root = tk.Tk()
root.title("Simple Daily Notepad")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=1000)

text_edit = tk.Text(root)
text_edit.grid(row=0, column= 1, sticky="NSEW")

frame_button = tk.Frame(root, relief= tk.RAISED, bd= 3, bg="cyan", border="2")
frame_button.grid(row=0, column=0, sticky="nsew")

open_button = tk.Button(frame_button, text= "Oen File", command= opening_file)
open_button.grid(row=0, column=0, padx=5, pady= 5)

save_button = tk.Button(frame_button, text="Save As", command=save_file)
save_button.grid(row=1, column=0, padx=5, pady= 5)



root.mainloop()

