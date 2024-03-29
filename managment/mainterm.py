from colorama import Fore, init
from client.operationwrapper import Operations

class Terminal:
    def __init__(self):
        init()
        self.options = []
        self.func_operations = Operations()
        self.__update_options()

    def __update_options(self):
        self.options.append("Devices")
        self.options.append("Messages")
        self.options.append("Broker && topic settings")
        self.options.append("Networking")
        self.options.append("Security")
        self.options.append("Quit")

    def show_menu(self):
        for i, element in enumerate(self.options, start=1):
            print(Fore.GREEN + f'[{i}] { Fore.MAGENTA + element}')

        operation = int(input(Fore.RESET + "Number of operation: "))
        self.__switch_operation(operation)

    def __switch_operation(self, selectedNum):
        if selectedNum == 1:
            self.func_operations.search_dev()
        else:
            print("Operation not implemented yet.")

if __name__ == '__main__':
    term = Terminal()
    term.show_menu()