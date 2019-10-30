# Shubham Patel
# github.com/shubham-00
# Open to be hired
# Open for projects
# Open for startups* (contact first)


import tkinter as tk
from tkinter import filedialog, Text
import webbrowser
import os


apps = []
# List of all apps.


if os.path.isfile("save.txt"):
	with open("save.txt", "r") as f:
		tempApps = f.read()
		tempApps = tempApps.split(",")
		apps = tempApps


for app in apps:
	if app == "" or app == " ":
		apps.remove(app)


def addApp():
	for widget in frame.winfo_children():
		widget.destroy()
	# All the labels are removed
	filename = filedialog.askopenfilename(initialdir = "~/Desktop/", title = "Select a File", filetypes = (("executables", "*.exe"), ("All files", "*.*")))
	apps.append(filename)
	print(filename)


	for app in apps:
		label = tk.Label(frame, text = app, bg = "gray")
		label.pack()
		# All the labels are added again.


def runApps():
	for app in apps:
		#os.startfile(app)	# For windows
		webbrowser.open(app)	# For unix


# Shubham Patel
# github.com/shubham-00
# Open to be hired
# Open for projects
# Open for startups* (contact first)


root = tk.Tk()	# This is the main diaglog box. This do not contain any canvas.
# Only a diaglog box opens now.


canvas = tk.Canvas(root, height = 650, width = 700, bg = "#263D42")	# To create a canvas on a root element
# Canvas is created but is not attached.
canvas.pack()	# Canvas is atached to the 'root' element
# Dialog box has canvas now.
# On canvas, we can put other things like a button


frame = tk.Frame(root, bg="white")	# Creating a frame on a root element
# Frame is created but is not attached.
frame.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1)	# Frame is attached with the root element.
# We have added a frame at the center now.


openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg = "white", bg = "#263D24", command = addApp)	# Button is created on root element.
# "command" is used for applying actions on click. Now, when clicked on "Open File" button, it executes "addApp()".
# Button is created but not attached.
openFile.pack()	# Button is attached.
# We have added a button labeled 'Open File' at the bottom of the root element (because root element has no empty space).


runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "white", bg = "#263D24", command = runApps)	# Button is created on the root element.
# Button is created but not atached.
runApps.pack()	# Buton is attached.
# We have added a button labeled 'Run Apps' at the bottom of the root element.


for app in apps:
	label = tk.Label(frame, text = app)
	label.pack()


root.mainloop()	# To start the dialog box


with open("save.txt", "w") as f:
	for app in apps:
		f.write(app + ",")


# Shubham Patel
# github.com/shubham-00
# Open to be hired
# Open for projects
# Open for startups* (contact first)
