from colorama import Fore, Back, Style, init, Back

class Operations:
    def __init__(self):
        init()
    def search_dev(self):
        print(Back.CYAN + Fore.BLACK  + "..Searching MQTT devices..")
        # create progressbar

    def view_msgs(self):
        print(Back.CYAN + Fore.BLACK + "..Read messages..")
