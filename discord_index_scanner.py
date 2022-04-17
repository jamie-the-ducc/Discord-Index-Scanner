# ---------------------------------- #
#             DIS v1.0.0             #
#        Discord Index Scanner       #
#   Coded with <3 by Jam!3 & Fa00j   #
#      Last updated 17/04/2022       #
# ---------------------------------- #
#      DM [Jam!3]#4466 for help      #
#     Suport server in progress      #
# ---------------------------------- #
#            DESCRIPTION             #
#  Scans Discord's "index.js" files  #
#  for any signs of malicious code   #
#  injection, as it's a main method  #
#   for token grabbers and Discord   #
# malware, which a lot of people are #
# unaware of or are unable to check. #
# ---------------------------------- #
#             CHANGELOG              #
# 17/04/22 - Cleaned up code (a bit) #
# 13/04/22 - Added Startup directory #
# 12/04/22 - Initial Project         #
# ---------------------------------- #
#                TODO                #
# - add functionality to Discord-PTB #
# - cleaner code                     #
# - other forms of protection        #
# - add executable version           #
# ---------------------------------- #
#               ISSUES               #
# - doesn't work with Discord-PTB    #
# - malicious code can be injected   #
#   into the Startup file            #
# ---------------------------------- #

import os
from glob import glob
from os import path as Path
from shutil import copyfile

from colorama import Fore, Style, init

init()
print(Style.BRIGHT, end="")


class DiscordIndexScanner:
    def __init__(self) -> None:
        # Startup Directory - the script will be
        # automatically ran on startup from there
        self.startup_dir = Path.join(
            os.getenv("APPDATA"),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs",
            "Startup",
        )
        # The file that will be saved to Startup
        self.startup_file = Path.join(
            self.startup_dir,
            "discord_index_scanner.pyw"
            # hidden with .pyw to not disturb on startup
        )
        # A list of clients that the program will check
        # Feel free to add more if nessecary
        self.clients = [
            "Discord",
            "DiscordPTB", # PTB doesn't work for whatever reason
            "DiscordCanary",
            "DiscordDevelopment",
        ]
        # Path to index.js from discord appdata
        self.index_dir = Path.join(
            "app-*",
            "modules",
            "discord_desktop_core-*",
            "discord_desktop_core",
            "index.js",
        )
        # The original unaltered index.js code
        self.index_code = "module.exports = require('./core.asar');"

    # Still needs to be bug tested
    def check_startup(self) -> None:
        # Verifies to make sure the Startup file wasn't
        # tampered with & is up to date
        with open(self.startup_file, "r") as f:
            check = f.read()
        with open(__file__, "r") as f:
            expected = f.read()
        if check != expected:
            print(
                f"{Fore.RED}[!] Startup script is outdated or compromised.{Fore.WHITE}"
            )
            with open(self.startup_file, "w") as f:
                f.write(expected)
                print(f"{Fore.GREEN}[+] Updated Startup script!")

    # Still needs to be bug tested
    def create_startup(self):
        # Copies the file to the Startup directory
        # where it can scan Discord automatically
        if os.path.isdir(self.startup_dir) and not Path.isfile(self.startup_file):
            copyfile(__file__, self.startup_file)
            print(f"{Fore.GREEN}[+] Added script to Startup folder{Fore.WHITE}")

        if __file__.lower() != self.startup_file.lower():
            self.check_startup()  # ensures that nobody compromised the startup file

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

    def clean_index(self, path: tuple) -> None:
        # Overwrites index.js with a clean version of the code
        print(f"{Fore.GREEN}[+] Cleaning '{path[0]}' {Fore.WHITE}")
        with open(path[1], "w") as f:
            f.write(self.index_code)

    def check_index(self, client: str, path: str) -> tuple:
        # Checks if index.js has been altered at all
        with open(path, "r") as f:
            index = f.read()
            if index != self.index_code:
                print(
                    f"{Fore.RED}[!] Client '{client}' may be injected with malicious code.{Fore.WHITE}"
                )
                return client, path

    def index_results(self, client: str) -> None:
        # Prints the Discord directories that have been scanned
        print(f"{Fore.BLUE}[#] {client} is safe.")

    # defining vars like that probably isn't the best practice, but hey, it works!
    def scan_index(self, found_malware: bool = False) -> None:
        # manages the different directories being scanned
        for path in [self.check_index(p[0], p[1]) for p in self.get_valid_paths()]:
            if path:
                found_malware = True
                self.clean_index(path)
        if not found_malware:
            print(f"{Fore.GREEN}[+] No malicious code found!{Fore.WHITE}")
        for client in self.get_valid_paths():
            self.index_results(client[0])

    def main(self) -> None:
        # main function that does the things
        if os.name == "nt":
            self.create_startup()
        print(
            f"{Fore.YELLOW}[~] Scanning Discord directories for index.js injection...{Fore.WHITE}"
        )
        self.scan_index()


if __name__ == "__main__":
    scanner = DiscordIndexScanner()
    scanner.main()
    input(f"{Style.BRIGHT}{Fore.YELLOW} < Press {Fore.WHITE}ENTER{Fore.YELLOW} to close the program >{Fore.YELLOW}")
