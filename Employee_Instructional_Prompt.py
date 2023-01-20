import curses
import random
from time import sleep
screen = curses.initscr()
curses.echo()
curses.cbreak()
curses.curs_set(0)
curses.start_color()
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
DEFAULT = curses.color_pair(2)

def title():
	title_text = f">-Employee #{number} Instructional Prompt"
	screen.addstr(0, 0, title_text, DEFAULT + curses.A_STANDOUT)
	screen.addstr(0, len(title_text), " " * (curses.COLS - len(title_text) - 11), DEFAULT + curses.A_STANDOUT)
	screen.addstr(0, curses.COLS - 11, "v. 1.81.7+", DEFAULT + curses.A_STANDOUT)
def center_text(text):
	screen.addstr(curses.LINES // 2, curses.COLS // 2 - len(text) // 2, text, DEFAULT)
def slightly_off_center_text(text):
	screen.addstr(curses.LINES // 2 + 1, curses.COLS // 2 - len(text) // 2, text, DEFAULT)

center_text("Employee ID: ")
number = screen.getstr().decode('ascii')
slightly_off_center_text("Password: ")
curses.noecho()
password_length = len(screen.getstr())
screen.addstr("*" * password_length)
screen.refresh()
sleep(1)
screen.clear()
center_text(f"Welcome Employee #{number}.")
screen.refresh()
sleep(2)

curses.noecho()
y = 1 
list_of_keys = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","\
1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ";", "'", "[", "]", "=", "-", "/", ".", ",", "`")
while True:
	if y == 1:
		screen.clear()
		title()
	screen.addstr(y, 0, "> ", DEFAULT)
	screen.refresh()
	sleep(random.uniform(0,3))
	key = random.choice(list_of_keys)
	time = random.randint(2,100)
	screen.addstr(y, 0, f"> Please PRESS '{key}' on your KEYBOARD for {time}ms.", DEFAULT)
	screen.refresh()
	c = 0
	while chr(c) != chr(ord(key.lower()[0])):
		c = screen.getch()
		if c == 27:
			screen.addstr(y, 0, f"> Your SHIFT is not OVER yet, Employee #{number}.   ", DEFAULT)
			screen.refresh()
			sleep(1)
			screen.addstr(y, 0, f"> Please PRESS '{key}' on your KEYBOARD for {time}ms.", DEFAULT)
			screen.refresh()
	screen.addstr(y+1, 0, "_ _ _", DEFAULT)
	y = y + 2 if y < curses.LINES - 3 else 1
	

	