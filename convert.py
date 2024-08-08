import subprocess
import os


audio_file = ""
output_file_prompt = ""
filetype = ""

def input_output():
    global audio_file
    audio_file = input("Enter audio file: ")
    audio_file = os.path.expanduser(audio_file)
    global output_file_prompt
    output_file_prompt = input("Output file name: ")

def filetype_chooser():
    global filetype
    filetype = input("Please enter the filetype you want to convert to (mp3, wav, mp4): ")

    if filetype != "mp3" and filetype != "wav" and filetype != "mp4":
        print("Valid options are 'mp3' 'wav' 'mp4'")
        filetype_chooser()

def mp3_to_wav():
    output_file = f"{output_file_prompt}.{filetype}"
    # print(f"Converting {audio_file} to {output_file}")
    mp3ToWav = ['ffmpeg','-i',audio_file, output_file]
    subprocess.run(mp3ToWav)

input_output()
filetype_chooser()
mp3_to_wav()
