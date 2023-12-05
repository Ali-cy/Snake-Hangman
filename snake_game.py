from tkinter import *
import random 
 

GAME_WIDTH = 1000
GAME_HEIGHT = 800
SPEED = 70
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = '#6600ff'
BACKGROUND_COLOUR = 'black'
FOOD_COLOUR = '#66ff99'


class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range (0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag='snake')
            self.squares.append(square)



class Food:
   
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        
        

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag='food')

    

def nextTurn(snake, food):
    x, y = snake.coordinates[0]

    if direction =='up':
        y -=SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE     

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)

    snake.squares.insert(0, square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score 

        score += 1

        label.config(text='Score:{}'.format(score))

        canvas.delete('food')

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, nextTurn, snake, food)

def change_directions(new_direction):
    global direction

    
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print('GAME OVER')
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print('GAME OVER')
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print('GAME OVER')
            return True
    return False

    if x < 0 or x >= GAME_WIDTH:
        print('Exit')
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print('Exit')
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print('Exit')
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font= ('calibri', 70), 
                       text='GAME OVER', fill='red', tag='gameover')

window = Tk()
window.title('Snake game')
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text='Score{}'.format(score), font=('calibri', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=(GAME_WIDTH))
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda event: change_directions('left'))
window.bind('<Right>', lambda event: change_directions('right'))
window.bind('<Up>', lambda event: change_directions('up'))
window.bind('<Down>', lambda event: change_directions('down'))

snake = Snake()
food = Food()

nextTurn(snake, food)

window.mainloop()