#This is the python GUI app
import PySimpleGUI as sg
from PIL import Image, ImageTk
import re

def input_topics(input_sentence: str):
	#The input topics are limited to 5.
	print("the inut sentence is: ",input_sentence)
	if not re.match("^[A-Za-z0-9 \.\?]*$", input_sentence):
		print("The sentence does not consist of just letters and numbers")
		raise ValueError
	topics = input_sentence.lower().split()[:5] # Lets to do 5 topics
	if len(topics) > 5:
		print("Topics deprecated. only 5 allowed")
	return topics

sg.theme("DarkTeal12")

layout = [[sg.Text('Enter your session\'s topics: '), sg.Input(key='-TOPICS-')],
          [sg.Text('Input your AHA moment: '), sg.Multiline(size=(40, 5), key='-AHA-', do_not_clear=True)],
			[sg.Button("Create the image")],
          [sg.Text('Your generated image: '), sg.Text(size=(12, 1), key='-OUTPUT-')],
          [sg.Image(key="the_image", size=(400,400))]]

window = sg.Window('NFT generator', layout, margins=(150,150),finalize=True)
size = (400, 400)
im = Image.open("ekackar.png")
im = im.resize(size, resample=Image.BICUBIC)
# Convert im to ImageTk.PhotoImage after window finalized

while True:  # Event Loop
	event, values = window.read()
	print(event, values)
	if event == "Create the image":
		try:
			topics = " ".join(input_topics(values["-TOPICS-"]))
		except ValueError:
			sg.popup("The Topics input has forbidden characters, please use only letters and numbers.")
			continue



		image = ImageTk.PhotoImage(im)
		window["the_image"].update(data = image)
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
window.close()