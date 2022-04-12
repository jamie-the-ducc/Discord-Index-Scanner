# ---------------------------------- #
#    Discord-Index-Scanner v1.0.0    #
#   Coded with <3 by Jam!3 & Fa00j   #
#     Last updated 12/04/2022        #
# ---------------------------------- #

# Functionality:
# Checks Discord's "index.js" files for
# any signs of tampering, as it is a
# commomn method of token grabbing and
# Discord malware, which a lot of people
# aren't even aware of.

# TODO: 
# - fix functionality for Discord-PTB
# - cleaner code
# - other forms of protection
# - add executable version

import os
from glob import glob
from os import path as Path

try:
    from colorama import Fore, Style, init
except ImportError:
    os.system("python -m pip install colorama")
    from colorama import Fore, Style, init

init()
print(Style.BRIGHT, end="")


class DiscordIndexScanner:
    def __init__(self) -> None:
        # self.user = Path.expanduser("~")
        self.local = os.getenv("LOCALAPPDATA")
        # PTB doesn't work?
        self.clients = ["Discord", "DiscordPTB", "DiscordCanary", "DiscordDevelopment"]
        self.index_dir = Path.join("app-*", "modules", "discord_desktop_core-*", "discord_desktop_core", "index.js")
        self.index_code = "module.exports = require('./core.asar');"

    def get_valid_paths(self) -> list:
        # Returns valid Discord directories (expect PTB)
        paths = []
        for client in self.clients:
            path = Path.join(self.local, client)
            if Path.isdir(path):
                path = glob(Path.join(path, self.index_dir))
                if path:
                    paths.append((client, path[0]))
        return paths

    def clean_index(self, path:str) -> None:
        # Overwrites index.js with a clean version of the code
        print(f"{Fore.GREEN}[+] Cleaning '{path}{Fore.WHITE}'")
        with open(path, "w") as f:
            f.write(self.index_code)

    def check_index(self, client:str, path:str) -> str:
        # Checks if index.js has been altered at all
        with open(path, "r") as f:
            index = f.read()
            if index != self.index_code:
                print(f"{Fore.RED}[!] Client '{client}' may be infected with malware.{Fore.WHITE}")
                return path

    def index_results(self, client:tuple):
        # Prints the Discord directories that have been scanned
        print(f"{Fore.BLUE}[#] {client[0]} is safe.")

    def scan_index(self, detected:list=[]):
        # Main function that does the things
        for path in self.get_valid_paths():
            detected.append(self.check_index(path[0], path[1]))       
        for path in detected:
            if path:
                self.clean_index(path)
        if detected.count(None) == len(detected):
            print(f"{Fore.GREEN}[+] No malware found!{Fore.WHITE}\n")
        for client in self.get_valid_paths():
            self.index_results(client)\


if __name__ == "__main__":
    print(f"{Fore.YELLOW}[~] Scanning Discord directories for 'index.js' malware...{Fore.WHITE}")
    scanner = DiscordIndexScanner()
    scanner.scan_index()
