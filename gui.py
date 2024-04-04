import tkinter as tk
from image import picture
from real_time import realTime
from tkinter import PhotoImage

# Create a main window
root = tk.Tk()
root.title("Face Detection")

render = PhotoImage(file='home.png')

new_width = 100
new_height = 100
render = render.subsample(int(render.width() / new_width), int(render.height() / new_height))

img = tk.Label(root, image=render)
img.image = render

label = tk.Label(root, text="Face Recognition System")

button1 = tk.Button(root, text="Detect in Photo", command=lambda: picture('images/beautiful_women.jpg'))
button2 = tk.Button(root, text="Detect an object", command=lambda: picture('images/bottle1.jpg'))
button3 = tk.Button(root, text="Detect in Group Pic", command=lambda: picture('images/group_pic.jpg'))
button4 = tk.Button(root, text="Detect in Real Time", command=lambda: realTime())

img.grid(row=0, column=0, columnspan=3, pady=20)  # Center the image
label.grid(row=1, column=0, columnspan=3, pady=10)
button1.grid(row=2, column=0, padx=10, pady=10)
button2.grid(row=2, column=1, padx=10, pady=10)
button3.grid(row=2, column=2, padx=10, pady=10)
button4.grid(row=3, column=0, padx=20, pady=10, columnspan=3)


root.mainloop()