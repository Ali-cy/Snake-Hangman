import random as r
import tkinter as tk



words = ['north', 'south', 'east', 'west', 'python', 'example', 'difficult', 'frighten', 'instrument',
         'advertise', 'environmental', 'frozen', 'fax', 'authority', 'revolutionary', 'genuine',
         'disappointment', 'jazz', 'hostility', 'guerrilla', 'software', 'island',
         'abruptly', 'rickshaw', 'avenue', 'hyphen', 'zigzag', 'zipper', 'queue', 'swivel', 'sphinx']

hangman_drawing = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

def word_generator():
    return r.choice(words)

def update_hangman(mistake):
    hangman_label.config(text=hangman_drawing[mistake])


def check_guess():
    guess = guess_entry.get()
    if guess.isalpha() and len(guess) == 1:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    global word_with_blanks
                    word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
            word_label.config(text=word_with_blanks)
            if '_' not in word_with_blanks:
                end_game('You WIN!')
        else:
            global mistakes
            mistakes += 1
            update_hangman(mistakes)
            if mistakes == len(hangman_drawing) - 1:
                end_game(f'You lose! The word is {word}')
    guess_entry.delete(0, tk.END)

def end_game(result):
    guess_entry.config(state='disabled')
    guess_button.config(state='disabled')
    result_label.config(text=result)

window = tk.Tk()
window.title('Hangman')
window.resizable(False, False)

window_width = 400
window_height = 415

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


hangman_label = tk.Label(window, font=('calibri', 16))
hangman_label.grid(row=0, column=0, columnspan=2)

word = word_generator()
word_with_blanks = '_' * len(word)
word_label = tk.Label(window, text=word_with_blanks, font=('calibri', 25))
word_label.grid(row=1, column=0, columnspan=2)

guess_entry = tk.Entry(window, font=('calibri', 24))
guess_entry.grid(row=2, column=0)
guess_button = tk.Button(window, text='Guess', command=check_guess)
guess_button.grid(row=2, column=1)

result_label = tk.Label(window, font=('calibri', 24))
result_label.grid(row=3, column=0, columnspan=2)

mistakes = 0
update_hangman(mistakes)

window.mainloop()

