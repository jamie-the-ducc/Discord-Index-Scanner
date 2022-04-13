# Discord Index Scanner v1.0.0
### Coded with 💜 by Jam!3 & Fa00j 
#### Last updated 13/04/2022 - DM me @ `[Jam!3]#4466`
**Discord Index Scanner** scans Discord's `index.js` files for any signs of malicious code injection, as it is a commomn method for token grabbers and Discord malware. A lot of people aren't aware of this issue or are unable to check, so this script will do it for you!

#### What is index.js injection?
Index.js injection is when a hacker injects malicious code into your Discord client. Every time you open the client, the hacker's code will be ran on your PC - usually consisting of token grabbers, password grabber, IP loggers, and the like.

## DOESN'T WORK WITH DISCORD-PTB FOR SOME REASON

!["DiscordIndexScanner"](https://i.imgur.com/ERuc4aV.png)

HOW TO RUN:
```
git clone https://github.com/jamie-the-ducc/Discord-Index-Scanner
cd ./Discord-Index-Scanner
python discord_index_scanner.py
```

TODO:
 - fix functionality for Discord-PTB
 - cleaner code
 - other forms of protection
 - add executable version

CHANGELOG:
- `13/04/22` - Added to Startup directory
- `12/04/22` - Initial Project

VULNERABILITIES:
- doesn't work with Discord-PTB
- malicious code may be injected into the Startup file
