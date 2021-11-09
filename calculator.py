from tkinter import * 

# ! NOTE!! ROOT FOR THE WINDOW
window = Tk()

# ! NOTE!! FUNCTIONS FOR THE CLICK
def press (num):
    global DISPLAY_TEXT, DISPLAY_LABEL

    DISPLAY_TEXT = DISPLAY_TEXT + str(num)
    DISPLAY_LABEL.set(DISPLAY_TEXT)

def equals ():
    global DISPLAY_LABEL, DISPLAY_TEXT


    try:
        RESULT = str(eval(DISPLAY_TEXT))
        DISPLAY_LABEL.set(RESULT)

        DISPLAY_TEXT = RESULT

    except ZeroDivisionError:
        ERROR_TEXT = "Can't divide by '0'"
        DISPLAY_TEXT = ERROR_TEXT
        DISPLAY_LABEL.set(DISPLAY_TEXT)

    except SyntaxError:
        ERROR_TEXT = "Invalid syntax!"
        DISPLAY_TEXT = ERROR_TEXT
        DISPLAY_LABEL.set(DISPLAY_TEXT)

def clear ():
    global DISPLAY_LABEL, DISPLAY_TEXT

    DISPLAY_TEXT = ""
    DISPLAY_LABEL.set(DISPLAY_TEXT)

DISPLAY_TEXT = ""
DISPLAY_LABEL = StringVar()

# ! NOTE!! LABEL FOR THE OUTPUT
EQN_LABEL = Label(
window, 
textvariable=DISPLAY_LABEL, 
font=('roboto', 20), 
bg="white",
width=30,
height=3,
)
EQN_LABEL.pack()

DISPLAY_FRAME = Frame(window)
DISPLAY_FRAME.pack()

# ! ALL OF THE BUTTONS


BUTTON1 = Button(
    DISPLAY_FRAME,
    text=1,
    height=4,
    width=9,
    font=35,
    command= lambda: press(1)
)
BUTTON1.grid(row=0,column=0)

BUTTON2 = Button(
    DISPLAY_FRAME,
    text=2,
    height=4,
    width=9,
    font=35,
    command= lambda: press(2)
)
BUTTON2.grid(row=0,column=1)

BUTTON3 = Button(
    DISPLAY_FRAME,
    text=3,
    height=4,
    width=9,
    font=35,
    command= lambda: press(3)
)
BUTTON3.grid(row=0,column=2)

BUTTON4 = Button(
    DISPLAY_FRAME,
    text=4,
    height=4,
    width=9,
    font=35,
    command= lambda: press(4)
)
BUTTON4.grid(row=1,column=0)

BUTTON5 = Button(
    DISPLAY_FRAME,
    text=5,
    height=4,
    width=9,
    font=35,
    command= lambda: press(5)
)
BUTTON5.grid(row=1,column=1)

BUTTON6 = Button(
    DISPLAY_FRAME,
    text=6,
    height=4,
    width=9,
    font=35,
    command= lambda: press(6)
)
BUTTON6.grid(row=1,column=2)

BUTTON7 = Button(
    DISPLAY_FRAME,
    text=7,
    height=4,
    width=9,
    font=35,
    command= lambda: press(7)
)
BUTTON7.grid(row=2,column=0)

BUTTON8 = Button(
    DISPLAY_FRAME,
    text=8,
    height=4,
    width=9,
    font=35,
    command= lambda: press(8)
)
BUTTON8.grid(row=2,column=1)

BUTTON9 = Button(
    DISPLAY_FRAME,
    text=9,
    height=4,
    width=9,
    font=35,
    command= lambda: press(9)
)
BUTTON9.grid(row=2,column=2)

BUTTON0 = Button(
    DISPLAY_FRAME,
    text=0,
    height=4,
    width=9,
    font=35,
    command= lambda: press(0)
)
BUTTON0.grid(row=3,column=1)

BUTTON00 = Button(
    DISPLAY_FRAME,
    text='00',
    height=4,
    width=9,
    font=35,
    command= lambda: press('00')
)
BUTTON00.grid(row=3,column=0)

# ! FUNCTIONAL BUTTONS (OR) OPERATORS

PLUS_BUTTON = Button (
    DISPLAY_FRAME,
    text='+',
    height=4,
    width=9,
    font=35,
    command= lambda: press ('+')
)
PLUS_BUTTON.grid(row=0,column=3)

MINUS_BUTTON = Button (
    DISPLAY_FRAME,
    text='-',
    height=4,
    width=9,
    font=35,
    command= lambda: press ('-')
)
MINUS_BUTTON.grid(row=1,column=3)

MULTIPLY_BUTTON = Button (
    DISPLAY_FRAME,
    text='*',
    height=4,
    width=9,
    font=35,
    command= lambda: press ('*')
)
MULTIPLY_BUTTON.grid(row=2,column=3)

DIVIDE_BUTTON = Button (
    DISPLAY_FRAME,
    text='/',
    height=4,
    width=9,
    font=35,
    command= lambda: press ('/')
)
DIVIDE_BUTTON.grid(row=3,column=3)

EQUAL_BUTTON = Button (
    DISPLAY_FRAME,
    text='=',
    height=4,
    width=9,
    font=35,
    command= equals,
)
EQUAL_BUTTON.grid(row=3,column=2)

POINT_BUTTON = Button (
    DISPLAY_FRAME,
    text='.',
    height=4,
    width=9,
    font=35,
    command= lambda: press('.'),
)
POINT_BUTTON.grid(row=1,column=4)

CLEAR_ALL = Button (
    DISPLAY_FRAME,
    text='CLEAR',
    height=4,
    width=9,
    font=35,
    command=clear,
)
CLEAR_ALL.grid(row=0,column=4)



window.title("Calculator")
window.geometry("500x500")
window.mainloop()



# !bruh