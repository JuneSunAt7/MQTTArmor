from colorama import Fore, init
from devices.finder import finder

class Device:
    def __init__(self):
        init()
        self.options = []
        self.__update_options()

    def __update_options(self):
        self.options.append("Find all devs")
        self.options.append("Add device")
        self.options.append("Show all devices")
        self.options.append("Get info")
        self.options.append("Quit")

    def show_menu(self):
        for i, element in enumerate(self.options, start=1):
            print(Fore.GREEN + f'[{i}] {Fore.MAGENTA + element}')

        operation = int(input(Fore.RESET + "Number of operation: "))
        self.__switch_operation(operation)

    def __switch_operation(self, selectedNum):
        if selectedNum == 1:
            finder()
        else:
            print("Operation not implemented yet.")
