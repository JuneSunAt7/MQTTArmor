from colorama import Fore, Back, Style, init
import datetime


class Logger:
    def __init__(self):
        print("Setup logger")
        init()

    def error(self, error):
        now = datetime.datetime.now()

        print(Fore.RED + str(error) + " ----- " + str(now))

    def succes(self, message):
        now = datetime.datetime.now()

        print(Fore.GREEN + 'Succes ' + str(message) + " ----- " + str(now))

    def warning(self, message):
        now = datetime.datetime.now()

        print(Fore.YELLOW + 'Warning ' + str(message) + " ----- " + str(now) )
    def printDefault(self, message):
        now = datetime.datetime.now()

        print(Fore.YELLOW + 'No warnings but no succes ' + str(message) + " ----- " + str(now) + "\n")