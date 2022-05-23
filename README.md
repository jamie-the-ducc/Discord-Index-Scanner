# Discord Index Scanner (DIS) v1.0.0
!["Title"](https://i.imgur.com/zyoo5rd.png)
## Coded with 💜 by [Jam!3](https://github.com/jamie-the-ducc) & Fa00j 
### Last updated 17/04/2022 - DM me @ `boxhead#4466` (`604855154365300753`)
**Discord Index Scanner** scans Discord's `index.js` files for any signs of malicious code injection, as it's a main method for token grabbers and Discord malware, which a lot of people are unaware of or are unable to check. This script will do it for you!

### What is index.js injection?
Index.js injection is when a hacker injects malicious code into your Discord client. Every time you open the client, the hacker's code will be ran on your PC - usually consisting of token grabbers, password grabber, IP loggers, and the like.

## DOESN'T WORK WITH DISCORD-PTB FOR SOME REASON
Example:

!["DiscordIndexScanner"](https://i.imgur.com/EWE3Tu7.png)

HOW TO RUN:
```bash
git clone "https://github.com/jamie-the-ducc/Discord-Index-Scanner"
cd ./Discord-Index-Scanner
python -m pip install -r requirements.txt
python discord_index_scanner.py
# enjoy :>
```

TODO:
 - add functionality to Discord-PTB
 - cleaner code
 - other forms of protection
 - add executable version

CHANGELOG:
- `17/04/22` - Cleaned up code (a bit)
- `13/04/22` - Added to Startup directory
- `12/04/22` - Initial Project

ISSUES:
- doesn't work with Discord-PTB
- malicious code may be injected into the Startup file
