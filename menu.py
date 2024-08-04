import tkinter as tk
import pygame
import cv2
from PIL import Image, ImageTk

class FullScreenGIFLabel(tk.Label):
    """A label that displays a full-screen GIF."""
    def __init__(self, master, gif_path, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.image = tk.PhotoImage(file=gif_path)
        self.configure(image=self.image)

class AnimatedGIFLabel(tk.Label):
    """A label that displays an animated GIF."""
    def __init__(self, master, gif_path, target_width=200, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.frames = []
        self.load_gif(gif_path, target_width)

    def load_gif(self, gif_path, target_width):
        gif = tk.PhotoImage(file=gif_path)
        aspect_ratio = gif.height() / gif.width()
        target_height = int(target_width * aspect_ratio)
        subsample_x = max(1, gif.width() // target_width)
        subsample_y = max(1, gif.height() // target_height)

        try:
            for i in range(100):  # Assuming the GIF has fewer than 100 frames
                frame = tk.PhotoImage(file=gif_path, format=f"gif -index {i}")
                self.frames.append(frame.subsample(subsample_x, subsample_y))
        except tk.TclError:
            pass  # End of frames

        self.current_frame = 0
        self.show_frame()

    def show_frame(self):
        frame = self.frames[self.current_frame]
        self.configure(image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(100, self.show_frame)

class WelcomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=640, height=480)
        self.pack_propagate(False)

        # Load and display the still GIF as a background
        still_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\sdad.gif"
        self.background_label = FullScreenGIFLabel(self, still_gif_path)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title Label
        title = tk.Label(self, text="Pauline's Emotional Support Device", font=("Arial", 20), bg='white')
        title.place(x=320, y=100, anchor="center")

        # Start Button
        start_button = tk.Button(self, text="Start", command=lambda: master.show_frame("PaginatedMenu"))
        start_button.place(x=220, y=210, width=200, height=60)

        # Animated GIF
        animated_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\dragon-raja.gif"
        self.animated_gif_label = AnimatedGIFLabel(self, animated_gif_path, target_width=200)
        self.place_animated_gif() 

    def place_animated_gif(self):
        # Calculate placement based on desired width and maintaining aspect ratio
        original_width = 498  # Original width of the GIF
        original_height = 497  # Original height of the GIF
        target_width = 200
        aspect_ratio = original_height / original_width
        target_height = int(target_width * aspect_ratio)

        # Positioning the GIF 20 pixels from the right and 20 pixels from the bottom
        gif_x = 640 - target_width - 20  # Frame width - target width - 20 pixels from the right
        gif_y = 480 - target_height - 20  # Frame height - target height - 20 pixels from the bottom
        self.animated_gif_label.place(x=gif_x, y=gif_y, width=target_width, height=target_height)

class PlayStopButtons(tk.Frame):
    """Frame containing play and stop buttons, centered horizontally and vertically."""
    def __init__(self, master, play_command, stop_command, **kwargs):
        super().__init__(master, **kwargs)

        # Dimensions for the buttons
        button_width = 80
        button_height = 40
        gap = 20  # Gap between buttons

        # Assuming the frame's width is enough to hold both buttons and the gap
        frame_width = 2 * button_width + gap
        frame_height = button_height + 20  # Extra padding vertically
        self.configure(width=frame_width, height=frame_height)

        # Calculate the starting x position for the play button to center both buttons
        start_x = (frame_width - (2 * button_width + gap)) / 2

        # Initialize and place the play button
        self.play_button = tk.Button(self, text="Play", command=play_command)
        self.play_button.place(x=start_x, y=(frame_height - button_height) / 2, width=button_width, height=button_height)

        # Initialize and place the stop button to the right of the play button
        self.stop_button = tk.Button(self, text="Stop", command=stop_command)
        self.stop_button.place(x=start_x + button_width + gap, y=(frame_height - button_height) / 2, width=button_width, height=button_height)

class SubSubMenuBase(tk.Frame):
    def __init__(self, master, recording_path, title):
        super().__init__(master)
        self.configure(width=640, height=480)
        self.pack_propagate(False)
        self.recording_path = recording_path

        # Load and display the still GIF as a background
        still_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\sdad.gif"
        self.background_label = FullScreenGIFLabel(self, still_gif_path)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title label
        self.title_label = tk.Label(self, text=title, bg='white', font=('Arial', 16))
        self.title_label.pack(pady=(20, 10))  # Adjust padding as needed

        # Play and Stop buttons
        self.play_stop_buttons = PlayStopButtons(self, self.play_voice_recording, self.stop_voice_recording)
        # Adjust placement for PlayStopButtons to ensure visibility
        self.play_stop_buttons.pack(side="bottom", pady=(10, 20))  # Place it at the bottom with some padding

        # Return button
        self.return_button = tk.Button(self, text="Return to 'You Want to Hear Me Sing' Menu", command=self.return_to_sing_menu)
        self.return_button.pack(side="bottom", pady=(5, 10))  # Additional padding for separation

    def play_voice_recording(self):
        """Stops any current playback and starts playing the selected recording."""
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.recording_path)
        pygame.mixer.music.play()

    def stop_voice_recording(self):
        """Stops the playback of the recording."""
        pygame.mixer.music.stop()

    def return_to_sing_menu(self):
        """Stops any playback and returns to the singing menu."""
        pygame.mixer.music.stop()
        self.master.show_frame("you want to hear me sing")

class SubSubMenu6a(SubSubMenuBase):
    def __init__(self, master, recording_path):
        super().__init__(master, recording_path, "Well Done Again My Friend")


class SubSubMenu6b(SubSubMenuBase):
    def __init__(self, master, recording_path):
        super().__init__(master, recording_path, "Can't Take My Eyes Off You")


class SubSubMenu6c(SubSubMenuBase):
    def __init__(self, master, recording_path):
        super().__init__(master, recording_path, "Tonight")


class SubSubMenu6d(SubSubMenuBase):
    def __init__(self, master, recording_path):
        super().__init__(master, recording_path, "I Loved You")
# Definitions for GenericSubMenu
class GenericSubMenu(tk.Frame):
    def __init__(self, master, title, recording_path=None):
        super().__init__(master)
        self.configure(width=640, height=480)
        self.pack_propagate(False)

        # Background setup...
        still_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\sdad.gif"
        self.background_label = FullScreenGIFLabel(self, still_gif_path)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text=title, bg='white')
        label.pack(pady=10)

        # Adjusted to ensure it appears at the bottom of the frame
        self.return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_main_menu)
        # Place the return button before initializing PlayStopButtons to ensure layout order
        self.return_button.pack(side="bottom", pady=(5, 10))

        if recording_path:
            self.recording_path = recording_path
            # Initialize PlayStopButtons below the title label
            self.play_stop_buttons = PlayStopButtons(self, self.play_voice_recording, self.stop_voice_recording)
            self.play_stop_buttons.pack(side="bottom", pady=(5, 0))

    def play_voice_recording(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.recording_path)
        pygame.mixer.music.play()

    def stop_voice_recording(self):
        pygame.mixer.music.stop()

    def return_to_main_menu(self):
        self.master.show_frame("PaginatedMenu")
        self.stop_voice_recording()

class SubMenu6(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=640, height=480)
        self.pack_propagate(False)

        # Load and display the still GIF as a background
        still_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\sdad.gif"
        self.background_label = FullScreenGIFLabel(self, still_gif_path)
        self.background_label.place(x=0, y=0, width=640, height=480)

        # Assuming a vertical layout where buttons are stacked, calculate the starting y position
        button_width = 200
        button_height = 60
        space_between_buttons = 10  # Space between buttons

        # Calculate vertical positions based on the new number of buttons
        options = [
            ("Well Done Again My Friend", "well done again my friend"),
            ("Can't Take My Eyes Off You", "cant take my eyes off you"),
            ("Tonight", "tonight"), 
            ("I Loved You", "i loved you"),
            ("Return to Main Menu", "PaginatedMenu")
        ]
        total_buttons_height = len(options) * button_height + (len(options) - 1) * space_between_buttons

        start_y = (480 - total_buttons_height) // 2

        # Label with a background set to improve visibility over the GIF
        label = tk.Label(self, text="'You Want to Hear Me Sing'", bg='white')  # Ensuring label visibility over the GIF
        label.pack(pady=10)

        # Buttons
        for index, (button_text, frame_key) in enumerate(options, start=1):
            button_y = start_y + (index - 1) * (button_height + space_between_buttons)
            button = tk.Button(self, text=button_text, command=lambda key=frame_key: master.show_frame(key))
            button.place(x=(640 - button_width) // 2, y=button_y, width=button_width, height=button_height)

class PaginatedMenu(tk.Frame):
    """The paginated menu displaying various options."""
    def __init__(self, master, options, options_per_page=4, command=None):
        super().__init__(master)
        self.configure(width=640, height=480)
        self.pack_propagate(False)

        self.options = options
        self.options_per_page = options_per_page
        self.current_page = 0
        self.command = command

        self.button_width_px = 200
        self.button_height_px = 60
        self.button_padding = 10

        still_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\sdad.gif"
        self.still_gif_label = FullScreenGIFLabel(self, still_gif_path)
        self.still_gif_label.place(x=0, y=0, width=640, height=480)

        animated_gif_path = "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\icegif-1171.gif"
        self.animated_gif_label = AnimatedGIFLabel(self, animated_gif_path, target_width=200)
        self.place_gif()

        self.display_options()
        self.setup_navigation_buttons()

    def place_gif(self):
        gif_x = 20  # 20 pixels from the left edge
        self.after(100, lambda: self.adjust_gif_placement(gif_x))

    def adjust_gif_placement(self, gif_x):
        gif_y = (480 - self.animated_gif_label.winfo_height()) // 2
        self.animated_gif_label.place(x=gif_x, y=gif_y)

    def setup_navigation_buttons(self):
        prev_button_x = 20
        next_button_x = 640 - self.button_width_px - 20
        nav_button_y = 480 - self.button_height_px - 20

        self.prev_button = tk.Button(self, text="Previous", command=self.previous_page)
        self.prev_button.place(x=prev_button_x, y=nav_button_y, width=self.button_width_px, height=self.button_height_px)

        self.next_button = tk.Button(self, text="Next", command=self.next_page)
        self.next_button.place(x=next_button_x, y=nav_button_y, width=self.button_width_px, height=self.button_height_px)

        # Back button to WelcomeScreen
        self.back_button = tk.Button(self, text="<-", command=lambda: self.master.show_frame("WelcomeScreen"))
        self.back_button.place(x=20, y=20, width=50, height=50)

    def display_options(self):
        # Remove existing option buttons before displaying new ones
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget not in [self.prev_button, self.next_button, self.back_button]:
                widget.destroy()

        start = self.current_page * self.options_per_page
        end = min(start + self.options_per_page, len(self.options))
        buttons_to_display = end - start
        total_buttons_height = (self.button_height_px + self.button_padding) * buttons_to_display
        start_y = (480 - total_buttons_height) // 2 - self.button_height_px

        for index, option in enumerate(self.options[start:end], start=1):
            button_y = start_y + (index - 1) * (self.button_height_px + self.button_padding)
            button = tk.Button(self, text=option, command=lambda o=option: self.command(o))
            button.place(x=320 - self.button_width_px // 2, y=button_y, width=self.button_width_px, height=self.button_height_px)

    def go_back(self):
        self.master.show_frame("WelcomeScreen")
        pygame.mixer.music.stop()

    def next_page(self):
        if self.current_page < (len(self.options) // self.options_per_page):
            self.current_page += 1
            self.display_options()

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_options()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()  # Initialize Pygame mixer
        self.title("Emotional Support Device")
        self.geometry("640x480")

        self.frames = {}
        # Update this dictionary with the correct paths to your audio files
        self.voice_recordings = {
            "you feel happy": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\happy.wav",
            "you need reassurance": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\reassurance.wav",
            "you feel lonely": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\lonely.wav",
            "you can't sleep": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\sleep.wav",
            "you feel overwhelmed": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\overwhelmed.wav",
            "you feel sick": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\sick.wav",
            "you feel upset": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\upset.wav",
            "something i said hurt you": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\i hurt.wav",
            "you think you were mean to me": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\hurt me.wav",
            "well done again my friend": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\well done.wav",
            "cant take my eyes off you": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\cant take my eyes off of you.wav",
            "tonight": "C:\\Users\\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\tonight.wav",
            "i loved you": "C:\\Users\longp\\OneDrive\\Desktop\\emotional support device\\audio files\\i loved you.wav",
        }

        self.initialize_frames()  # Assuming this method initializes your frames as before
        self.show_frame("WelcomeScreen")

    def initialize_frames(self):
        """Initialize all frames and submenus, ensuring PaginatedMenu only shows main options."""
        self.frames["WelcomeScreen"] = WelcomeScreen(self)
        
        # Initialize SubMenu6 separately with its special logic
        self.frames["you want to hear me sing"] = SubMenu6(self)

        # Define the main options that should appear in PaginatedMenu
        main_options = [
            "you feel happy", 
            "you need reassurance", 
            "you feel lonely",
            "you can't sleep", 
            "you feel overwhelmed",
            "you want to hear me sing",  # This leads to SubMenu6 which contains subsubmenu options
            "you feel sick", 
            "you feel upset", 
            "something i said hurt you", 
            "you think you were mean to me"
        ]

        # Initialize PaginatedMenu with main options
        self.frames["PaginatedMenu"] = PaginatedMenu(self, main_options, command=self.on_option_selected)

        # Initialize GenericSubMenus for each main option
        for name in main_options:
            if name in self.voice_recordings:  # Check if there's a corresponding recording path
                self.frames[name] = GenericSubMenu(self, name, recording_path=self.voice_recordings[name])

        # Initialize specific SubSubMenus for 'You Want to Hear Me Sing'
        self.frames["well done again my friend"] = SubSubMenu6a(self, self.voice_recordings["well done again my friend"])
        self.frames["cant take my eyes off you"] = SubSubMenu6b(self, self.voice_recordings["cant take my eyes off you"])
        self.frames["tonight"] = SubSubMenu6c(self, self.voice_recordings["tonight"])
        self.frames["i loved you"] = SubSubMenu6d(self, self.voice_recordings["i loved you"])

        # Grid placement for all frames
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_key):
        """Brings the specified frame to the front."""
        frame = self.frames.get(frame_key)
        if frame:
            frame.tkraise()

    def on_option_selected(self, option_name):
        """Handles submenu selection and initiates playback if applicable."""
        self.show_frame(option_name)

if __name__ == "__main__":
    app = App()
    app.mainloop()
