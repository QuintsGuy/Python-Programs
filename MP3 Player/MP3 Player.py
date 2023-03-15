from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame
import time
from mutagen.mp3 import mp3

root = Tk()
root.title('Codemy.com MP3 Player')
root.iconbitmap('t:/gui/images/video.png')
root.geometry('500x300')

# Initialize Pygame Mixer
pygame.mixer.init()

# Grab song length & time information
def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    converted_time = time.strftime('%M:%S', time.gmtime(current_time))

    # Output time
    status_bar.configure(text=converted_time)

    # Update time
    status_bar.after(1000, play_time)

# Add Song Function
def add_song():
    song = filedialog.askopenfilename(initialdir='t:/gui/audio/', title='Choose A Song', filetypes=(("mp3 Files", "*.mp3"), )).lower()

    # Strip out directory and extension from song name
    song = song.replace('t:/gui/audio/', '')
    song = song.replace('.mp3', '')
    
    # Add song to list box
    song_box.insert(END, song)

# Add Multiple Songs Function
def add_multiple_songs():
    songs = filedialog.askopenfilenames(initialdir='t:/gui/audio/', title='Choose A Song', filetypes=(("mp3 Files", "*.mp3"), )).lower()

    # loop through song list and replace directory & extension from song names
    for song in songs:
        song = song.replace('t:/gui/audio/', '')
        song = song.replace('.mp3', '')

        # Add song to list box
        song_box.insert(END, song)

# Play Song Function
def play():
    song = song_box.get(ACTIVE)
    song = f't:/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call play_time function to get time

# Stop Song Function
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Pause Song Function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

# Play Next Song in Playlist Function
def next_song():
    # Get current selected song in song box
    next_one = song_box.curselection()
    # Add one to select the next song in playlist
    next_one = next_one[0]+1
    
    song = song_box.get(next_one)
    song = f't:/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Move Active Bar in Song Box
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

# Play Previous Song in Playlist Function
def previous_song():
    # Get current selected song in song box
    previous_one = song_box.curselection()
    # Add one to select the next song in playlist
    previous_one = previous_one[0]-1
    
    song = song_box.get(previous_one)
    song = f't:/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Move Active Bar in Song Box
    song_box.selection_clear(0, END)
    song_box.activate(previous_one)
    song_box.selection_set(previous_one, last=None)

# Delete a Song Function
def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

# Delete All Songs Function
def delete_all_songs():
    song_box.delete(0, END)
    pygame.mixer.music.stop()

# Global Pause Variable
global paused
paused = False

# Create Playlist Box
song_box = Listbox(root, bg="black", fg="white", width=60, selectbackground="grey", selectforeground="black")
song_box.pack(pady=20)

# Create Player Control Buttons
raw_back_btn = Image.open('t:/gui/images/back.png').resize((30,30))
back_btn_img = ImageTk.PhotoImage(raw_back_btn)

raw_fwd_btn = Image.open('t:/gui/images/next.png').resize((30,30))
fwd_btn_img = ImageTk.PhotoImage(raw_fwd_btn)

raw_play_btn = Image.open('t:/gui/images/play.png').resize((30,30))
play_btn_img = ImageTk.PhotoImage(raw_play_btn)

raw_pause_btn = Image.open('t:/gui/images/pause.png').resize((30,30))
pause_btn_img = ImageTk.PhotoImage(raw_pause_btn)

raw_stop_btn = Image.open('t:/gui/images/stop.png').resize((30,30))
stop_btn_img = ImageTk.PhotoImage(raw_stop_btn)

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

# Create Player Control Buttons
back_button     = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button  = Button(controls_frame, image=fwd_btn_img, borderwidth=0, command=next_song)
play_button     = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button    = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button     = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# Add Multiple Songs to Playlist
add_song_menu.add_command(label="Add Multiple Songs To Playlist", command=add_multiple_songs)

# Create Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song from Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs from Playlist", command=delete_all_songs)

# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

root.mainloop()