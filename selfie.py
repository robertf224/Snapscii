import curses, subprocess
from itoa import itoa


subprocess.call(['./isightcapture', 'selfie.jpg'])

def main(screen):
	curses.curs_set(0)
	screen.keypad(1) # let curses watch for arrow keys
	#screen.timeout(0)

	string = itoa('selfie.jpg', curses.COLS, curses.LINES)
	array = string.split('\n')

	for y in xrange(len(array)-1):
		for x in xrange(len(array[y])-1):
			screen.addch(y, x, array[y][x])

	screen.refresh()
	screen.getch()

curses.wrapper(main)




