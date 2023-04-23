import os
import shutil
from tkinter import filedialog, messagebox, Tk, Listbox, Button, MULTIPLE, Checkbutton, IntVar, font, Frame, Label

# Function to move desktop files
def move_files(excluded_files, include_folders):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    new_folder = os.path.join(desktop_path, "Organized")
    os.makedirs(new_folder, exist_ok=True)

    for item in os.listdir(desktop_path):
        if item == "Organized":  # Skip the Organized folder
            continue

        item_path = os.path.join(desktop_path, item)
        is_file = os.path.isfile(item_path) or item.endswith(".lnk")
        is_folder = os.path.isdir(item_path)

        if include_folders and is_folder:
            is_file = True

        if item not in excluded_files and is_file and item != "desktop.ini":
            shutil.move(item_path, os.path.join(new_folder, item))

# Function to get selected exceptions
def get_selection():
    selection = listbox.curselection()
    selected_files = [listbox.get(i) for i in selection]
    include_folders = include_folders_var.get()

    move_files(selected_files, include_folders)
    messagebox.showinfo("Success", "Files moved successfully.")
    window.destroy()

# Function to update the listbox items based on the checkbox
def update_listbox():
    listbox.delete(0, "end")
    include_folders = include_folders_var.get()

    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)

        if (os.path.isfile(item_path) or item.endswith(".lnk")) and item != "desktop.ini":
            listbox.insert("end", item)

        if include_folders and os.path.isdir(item_path):
            listbox.insert("end", item)

# Create and configure the tkinter window
window = Tk()
window.title("Desktop Organizer")
window.geometry("300x450")
window.configure(bg="#1c1c1c")

custom_font = font.Font(family="Consolas", size=10)

header_frame = Frame(window, bg="#1c1c1c")
header_frame.pack(pady=10, padx=15)
header_label = Label(header_frame, text="desktop organizer", bg="#1c1c1c", fg="#f1c40f", font=custom_font)
header_label.pack()

separator = Frame(window, height=2, bg="#2a2a2a")
separator.pack(fill="x", padx=15)

listbox = Listbox(window, selectmode=MULTIPLE, bg="#2a2a2a", fg="#f1c40f", font=custom_font, highlightthickness=0)
listbox.pack(pady=15, padx=15)

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)

    if (os.path.isfile(item_path) or item.endswith(".lnk")) and item != "desktop.ini":
        listbox.insert("end", item)

include_folders_var = IntVar()
include_folders_checkbutton = Checkbutton(window, text="Include folders", variable=include_folders_var, command=update_listbox, bg="#1c1c1c", fg="#f1c40f", font=custom_font, selectcolor="#111111", activebackground="#1c1c1c", activeforeground="#f1c40f")
include_folders_checkbutton.pack(pady=10)

select_button = Button(window, text="Select Exceptions and Move Files", command=get_selection, bg="#34495e", fg="#f1c40f", font=custom_font, activebackground="#2c3e50", activeforeground="#f1c40f")
select_button.pack(pady=15)

window.mainloop()
