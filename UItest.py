import tkinter as tk

def show_frame(frame):
    frame.tkraise()

def open_letter_menu(option):
    label_letter.config(text=f"Voice recording for when {option}.")
    show_frame(frame_letter)

def open_song_menu():
    show_frame(frame_songs)

def create_grid(frame):
    for i in range(10):
        for j in range(10):
            label = tk.Label(frame, text=f"{i},{j}", bg='grey', fg='white', font=('Helvetica', 8))
            label.grid(row=i, column=j, sticky='news')

# Create the main window
app = tk.Tk()
app.title("Open When...")
app.geometry("480x320")  # Set the window resolution to 480x320
app.configure(bg='black')  # Set background color

# Create frames
frame_main = tk.Frame(app, bg='black')
frame_letter = tk.Frame(app, bg='black')
frame_songs = tk.Frame(app, bg='black')

for frame in (frame_main, frame_letter, frame_songs):
    frame.grid(row=0, column=0, sticky='news')

# Create grid for layout approximation in the main frame
create_grid(frame_main)

# Main Menu Options
options = [
    "you feel happy", "you need reassurance", "you feel lonely", "you can't sleep",
    "you feel overwhelmed", "you want to hear me sing", "you feel sick",
    "you feel small", "something I said hurt you", "you think you were mean to me"
]

button_font = ('Helvetica', 14)  # Font for the buttons
button_height = 2  # Height of buttons
button_width = 20  # Width of buttons

for option in options:
    command = open_song_menu if option == "you want to hear me sing" else lambda opt=option: open_letter_menu(opt)
    button = tk.Button(frame_main, text=option, command=command, bg='black', fg='white', font=button_font, height=button_height, width=button_width)
    # Adjust the placement of buttons based on the grid layout
    button.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

# Letter Menu
label_letter = tk.Label(frame_letter, text="", bg='black', fg='white', font=button_font)
label_letter.pack(pady=10)
tk.Button(frame_letter, text="Back to Main Menu", command=lambda: show_frame(frame_main), bg='black', fg='white', font=button_font).pack()

# Songs Menu
tk.Button(frame_songs, text="Well done again my friend", command=lambda: open_letter_menu("you want to hear 'Well done again my friend'"), bg='black', fg='white', font=button_font).pack(pady=5)
tk.Button(frame_songs, text="Can't take my eyes off you", command=lambda: open_letter_menu("you want to hear 'Can't take my eyes off you'"), bg='black', fg='white', font=button_font).pack(pady=5)
tk.Button(frame_songs, text="Back to Main Menu", command=lambda: show_frame(frame_main), bg='black', fg='white', font=button_font).pack(pady=10)

# Show the main frame initially
show_frame(frame_main)

# Run the application
app.mainloop()
