import random
import curses  # mouse

screen = curses.initscr()  # inizliaze the curses library to return our screen
curses.curs_set(0)  # hide the curse
screen_height, screen_width = screen.getmaxyx()  # return tuple with heighst avaliable heigh and width
window = curses.newwin(screen_height, screen_width, 0, 0)  # start from Top left corner
window.keypad(1)  # 1 represent true , keypad allow the window to recive input from the user
window.timeout(125)  # delay of update screen
snk_x = screen_width // 4
snk_y = screen_height // 2
# coordinates of head of snake
snake = [
    [snk_y, snk_x]
    , [snk_y - 1, snk_x],
    [snk_y - 2, snk_x]
]
food = [screen_height // 2, screen_width // 2]  # define the coordinates
window.addch(food[0], food[1], curses.ACS_DIAMOND)  # set the food
key = curses.KEY_RIGHT
while True:
    next_key = window.getch()  # next action
    key = key if next_key == -1 else next_key
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    snake.insert(0, new_head)
    if snake[0] == food:
        food = None
        while food == None:
            new_food = [
                random.randint(1, screen_height - 1), random.randint(1, screen_width - 1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)








