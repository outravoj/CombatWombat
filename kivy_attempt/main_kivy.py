from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import *
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

Builder.load_file("MainApp.kv")

class CustomDropdown(DropDown):
	pass

class MyFloatLayout(Widget):

	def change_ai_text(self):

class MainApp(App):
	def build(self):
		return MyFloatLayout()

MainApp().run()