#! /usr/bin/python3

import sys
import dbus

ALLOWED_ACTIONS = ("+","-")

def main(action:str):
	bus = dbus.SessionBus()
	proxy = bus.get_object("org.kde.KWin", "/KWin")

	actions = {
		"+" : proxy.nextDesktop,
		"-" : proxy.previousDesktop
	}

	func = actions[action]
	func()

if __name__ == "__main__":
	if not len(sys.argv) >= 2:
		sys.stderr.write("Missing arguments\n")
		exit()

	action = sys.argv[1]

	if action not in ALLOWED_ACTIONS:
		sys.stderr.write("Invalid action\n")
		exit()

	main(action)