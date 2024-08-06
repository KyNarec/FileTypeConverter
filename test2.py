
import customtkinter
from convert import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Audio Converter")
label.pack(pady=12, padx=10)

entry_input_file = customtkinter.CTkEntry(master=frame, placeholder_text="input file path")
entry_input_file.pack(pady=12, padx=10)

entry_output_file = customtkinter.CTkEntry(master=frame, placeholder_text="Output file name")
entry_output_file.pack(pady=12, padx=10)

filetype_menue = customtkinter.CTkOptionMenu(master=frame, variable=filetype, values=["mp3", "wav", "mp4"])
filetype_menue.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Convert", command=mp3_to_wav)
button.pack(pady=12, padx=10)

root.mainloop()
