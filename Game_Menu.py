import subprocess
from tkinter import *


MENU_WIDTH = 1000
MENU_HEIGHT = 800
MENU_COLOUR = 'black'

class Menu:

    def __init__(self):
      self.menu_texts=['SELECT GAME:']
      self.menu_objects =[]

      for idx, text in enumerate(self.menu_texts):
        menu_item = canvas.create_text(MENU_WIDTH /2, 100 + idx * 100, text = text, font=('calibri', 70), 
                                       fill='white', tag='menu')
        self.menu_objects.append(menu_item)

        for idx, text in enumerate(self.menu_texts):
            menu_item = canvas.create_text(
                MENU_WIDTH / 2, 100 + idx * 100, text=text,
                font=('calibri', 70), fill='white', tag='menu'
            )
            self.menu_objects.append(menu_item)

        self.optionMenu_texts = ['Snake', 'Hangman', 'Exit']
        self.menu_options = []

        for idx, text in enumerate(self.optionMenu_texts):
            menu_choice = canvas.create_text(
                MENU_WIDTH / 2, 300 + idx * 100, text=text,
                font=('calibri', 50), fill='white', tag='menu'
            )
            self.menu_options.append(menu_choice)

window = Tk()
window.title('Game Menu')
window.resizable(False, False)

label = Label(window, text='Game Menu', font=('calibri', 40))
label.pack()

canvas = Canvas(window, bg=MENU_COLOUR, height=MENU_HEIGHT, width=MENU_WIDTH)
canvas.pack()

def menu_click(event):
   item = event.widget.find_withtag(CURRENT)
   print('Clicked:', canvas.itemcget(item, 'text'))

menu = Menu()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')



def left_click(event):
    def revert_colour():
        event.widget.itemconfigure(item, fill='white')

    item = event.widget.find_closest(event.x, event.y)
    item_text = event.widget.itemcget(item, 'text')
   
    if item_text == 'Snake':
        event.widget.itemconfigure(item, fill='green')
        event.widget.after(500, revert_colour)
        subprocess.Popen(['python', 'C:/Users/alich/OneDrive/Documents/Programming/snake_game.py'])

    if item_text == 'Hangman':
       event.widget.itemconfigure(item, fill='green')
       event.widget.after(500, revert_colour)
       subprocess.Popen(['python', "C:/Users/alich/OneDrive/Documents/Programming/Hangman.py"])        

    if item_text == 'Exit':
      event.widget.itemconfigure(item, fill='red')
      window.after(100, lambda: window.destroy())
    
   
window.bind('<Button-1>',left_click)

menu = Menu()

window.mainloop()
 