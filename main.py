import customtkinter
import subprocess
import os
import tkinter as tk
from tkinter import messagebox

# Ensure the dark mode and theme settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Function to handle the conversion process
def convert_audio():
    audio_file = entry_input_file.get()
    output_file_prompt = entry_output_file.get()
    filetype = filetype_var.get()
    
    if not audio_file or not output_file_prompt or filetype not in ["mp3", "wav", "mp4"]:
        messagebox.showerror("Error", "Please fill out all fields correctly.")
        return

    # Expand the user path (e.g., ~) to the full path
    audio_file = os.path.expanduser(audio_file)
    if not os.path.isfile(audio_file):
        messagebox.showerror("Error", "The input file does not exist.")
        return

    output_file = f"{output_file_prompt}.{filetype}"
    print(f"Converting {audio_file} to {output_file}")
    command = ['ffmpeg', '-i', audio_file, output_file]
    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Converted {audio_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to convert file: {e}")

# Create the main window
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Audio Converter")

# Create and configure the frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Add a label
label = customtkinter.CTkLabel(master=frame, text="Audio Converter")
label.pack(pady=12, padx=10)

# Add entry fields
entry_input_file = customtkinter.CTkEntry(master=frame, placeholder_text="Input file path")
entry_input_file.pack(pady=12, padx=10)

entry_output_file = customtkinter.CTkEntry(master=frame, placeholder_text="Output file name")
entry_output_file.pack(pady=12, padx=10)

# Add a dropdown menu for file type selection
filetype_var = tk.StringVar(value="mp3")
filetype_menu = customtkinter.CTkOptionMenu(master=frame, variable=filetype_var, values=["mp3", "wav", "mp4"])
filetype_menu.pack(pady=12, padx=10)

# Add the convert button
button = customtkinter.CTkButton(master=frame, text="Convert", command=convert_audio)
button.pack(pady=12, padx=10)

# Start the main event loop
root.mainloop()