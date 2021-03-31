import random
from tkinter import *

def button_action():
	rolled_value = random.randint(1,6)
	roll_label.config(text=rolled_value)




 # Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("Any dice you want")


change_button = Button(fenster, text="I roll", command=button_action)

roll_label = Label(fenster, text="Here you call roll.")

roll_label.pack()
change_button.pack()








# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()

