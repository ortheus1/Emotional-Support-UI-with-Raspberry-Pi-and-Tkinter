import os

# Get the full path to the script file
script_path = os.path.abspath(__file__)

# Extract the directory containing the script
script_dir = os.path.dirname(script_path)

# Construct a path to the GIF file in the same directory as the script
gif_path = os.path.join(script_dir, "your_animation.gif")