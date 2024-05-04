import os
import sys

from pathlib import Path
from colorama import Fore, Back, Style

def scan_folder(path: Path, spaces=0):
    for element in path.iterdir():
        if element.is_file():
            print(Fore.YELLOW + " "*spaces + element.name)
        else:
            print(Fore.BLUE + " "*spaces + element.name + "/")
            scan_folder(element, spaces+4)


def main():
    args = sys.argv
    if len(args) < 2 or not os.path.exists(args[1]) or os.path.isfile(args[1]):
        print("input path not correct")
        return
    path = Path(args[1])
    scan_folder(path)
    


main()
