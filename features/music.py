from tkinter import GROOVE
import playsound
import os
import random

def play_song_pc():
    try:
        music_dir = "C:/Users/ruben/Documents/Projetos/Faculdade/LAMEC/voice_ai/features/music_example"
        songs = os.listdir(music_dir)   
        os.system('start ' + os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))
        results = True
    except Exception as e:
        print(e)
        results = False
    return results

def stop_song_pc():
    try:
        os.system('taskkill /f /im  Music.UI.exe')
        results = True
    except Exception as e:
        print(e)
        results = False
    return results

