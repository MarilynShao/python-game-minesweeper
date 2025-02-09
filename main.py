from tkinter import *
import settings
import utils
from cell import Cell

# Assign new Tk() to root
root = Tk()

#Override the settings of the window
root.configure(
    bg="black",
    cursor="cross",
    )
# Change window size
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
# Change window title
root.title('Minesweeper Game')
# False when not allowing user to change size of the window manually
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(25)
    )

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(x=utils.width_prct(25), y=0)

left_frame = Frame(
    root,
    bg="black", 
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x=0, y=utils.height_prct(25))

centre_frame = Frame(
    root,
    bg="black", 
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

centre_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
    )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
# Call the label from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,y=0
)
Cell.randomise_mines()

# Keep the window root open until manually closed, run
root.mainloop()