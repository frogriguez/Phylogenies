
# Imports
import os
from os import path
from os.path import join
from Bio import Phylo
from tkinter import *
from tkinter import messagebox

def help():
	messagebox.showinfo("Help", "I cannot help you right now.\nPress 1 to speak to a representative.")

def get_filenames(path):
	#names = os.listdir(r'C:\Users\Zach\Google Drive\Coding\GitHub\Squamate DB\images')
	names = []
	for file in os.listdir(path):
		file = os.path.splitext(file)[0]
		file = file.title()
		names.append(file)
	names.sort()
	return names
	

def tree_gui():
	#create Widget Grid
	gui = Tk()	#names tkinter interface: 'gui'
	gui.title("Squamate Database") #grid title

	gui.geometry("300x75")  #Sets grid size

	Label(gui, text="Phylogeny:").grid(row=0, column=0)  #Labels entry1: "Tree"
	mtree = Menubutton(gui, text="Phylogeny", relief=RASIED).grid(row=0, column=1)
	
	
	Label(gui, text="Taxon:").grid(row=1,column=0)   #Lables entry2: "Taxon"

	#Makes buttons
	Button(gui, text='Help', command=help).grid(row=2, column=0, sticky=W, pady=4)  #creates a button for help
	Button(gui, text='Quit', command=gui.quit).grid(row=2, column=1, sticky=W, pady=4)  #Creates a quit button
	
	#info = PhotoImage(file="chameleon.gif")
	
	#creates figure frame
	info_frame=Frame(gui)
	info_frame.grid(row=3, columnspan=2)
	#f = plot(figsize=(6,5), dpi=100)

	#creates frame for tree
	info_frame=Frame(gui)
	info_frame.grid(row=1, column=2, columnspan=3)
	#f = plot(figsize=(6,5), dpi=100)
	
	
	#Plots figure (graph) into gui
	#c = Canvas(info,gui=info_frame)
	#c.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
	gui.mainloop( )

path = str(r"C:\Users\Zach\Google Drive\Coding\GitHub\Squamate DB\images")
print(get_filenames(path))
tree_gui()
