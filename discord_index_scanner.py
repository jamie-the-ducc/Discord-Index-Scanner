# ---------------------------------- #
#    Discord-Index-Scanner v1.0.0    #
#   Coded with <3 by Jam!3 & Fa00j   #
#     Last updated 13/04/2022        #
# ---------------------------------- #

# DESCRIPTION:
# Scans Discord's "index.js" files for
# any signs of malicious code injection, 
# as it is a commomn method for token grabbers
# and Discord malware, which a lot of people
# aren't aware of or are unable to check.

# CHANGELOG:
# 13/04/22 - Added to Startup directory
# 12/04/22 - Initial Project

# TODO: 
# - fix functionality for Discord-PTB
# - cleaner code
# - other forms of protection
# - add executable version

# VULNERABILITIES:
# - doesn't work with Discord-PTB
# - malicious code can be injected into the Startup file

# ---------------------------------- #

import os
from shutil import copyfile
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
        self.startup_dir = Path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        self.startup_file = Path.join(self.startup_dir, "discord_index_scanner.pyw") # hidden to not disturb on startup
        self.clients = ["Discord", "DiscordPTB", "DiscordCanary", "DiscordDevelopment"] # PTB doesn't work for whatever reason
        self.index_dir = Path.join("app-*", "modules", "discord_desktop_core-*", "discord_desktop_core", "index.js")
        self.index_code = "module.exports = require('./core.asar');"

    # Not bug tested yet lol
    def check_startup(self):
        # Verifies to make sure the Startup file wasn't
        # tampered with & is up to date
        with open(self.startup_file, 'r') as f:
            check = f.read()
        with open(__file__, 'r') as f:
            expected = f.read()
        if check != expected:
            print(f"{Fore.RED}[!] Startup script is outdated or compromised.{Fore.WHITE}")
            with open(self.startup_file, 'w') as f:
                f.write(expected)
                print(f"{Fore.GREEN}[+] Updated Startup script!")

    # Not bug tested yet lol
    def create_startup(self):
        # Copies the file to the Startup directory
        # where it can scan Discord automatically
        if os.path.isdir(self.startup_dir) and not Path.isfile(self.startup_file):
            copyfile(__file__, self.startup_file)
            print(f"{Fore.GREEN}[+] Added script to Startup folder{Fore.WHITE}")
            
        if __file__.lower() != self.startup_file.lower():
            self.check_startup() # ensures that nobody compromised the startup file
        

    def get_valid_paths(self) -> list:
        # Returns valid Discord directories (except PTB)
        paths = []
        for client in self.clients:
            path = Path.join(os.getenv("LOCALAPPDATA"), client)
            if Path.isdir(path):
                path = glob(Path.join(path, self.index_dir))
                if path:
                    paths.append((client, path[0]))
        return paths

    def clean_index(self, path:tuple) -> None:
        # Overwrites index.js with a clean version of the code
        print(f"{Fore.GREEN}[+] Cleaning '{path[0]}' {Fore.WHITE}")
        with open(path[1], "w") as f:
            f.write(self.index_code)

    def check_index(self, client:str, path:str) -> str:
        # Checks if index.js has been altered at all
        with open(path, "r") as f:
            index = f.read()
            if index != self.index_code:
                print(f"{Fore.RED}[!] Client '{client}' may be injected with malicious code.{Fore.WHITE}")
                return client, path

    def index_results(self, client:tuple) -> None:
        # Prints the Discord directories that have been scanned
        print(f"{Fore.BLUE}[#] {client[0]} is safe.")

    # defining vars like that probably isn't the best practice, but hey, it works!
    def scan_index(self, x=0, y=0) -> None:
        # manages the different directories being scanned 
        for path in [self.check_index(p[0], p[1]) for p in self.get_valid_paths()] :
            if path:
                y += 1
                self.clean_index(path)
        if y == x:
            print(f"{Fore.GREEN}[+] No malicious code found!{Fore.WHITE}")
        for client in self.get_valid_paths():
            self.index_results(client)

    def main(self) -> None:
        # main function that does the things
        if os.name == 'nt':
            self.create_startup()
        print(f"{Fore.YELLOW}[~] Scanning Discord directories for index.js injection...{Fore.WHITE}")
        self.scan_index()

if __name__ == "__main__":
    scanner = DiscordIndexScanner()
    scanner.main()
