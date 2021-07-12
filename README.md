# twitch_plays_souls

## Important Notes:
Disclaimer 1: PLEASE BE AWARE THAT OTHER PEOPLE WILL BE SIMULATING KEYBOARD PRESSES TO YOUR COMPUTER, 

WHILE I WILL DO MY PART TO ENSURE THAT NO HARMFUL SCENARIOS ARISE, 

PLEASE MAKE SURE TO REMOVE ANY REVEALING INFO FROM YOUR DESKTOP SCREEN OR OTHER RUNNING PROGRAMS IF TECHNICAL DIFFICULTIES ARISE WHEN LIVE

Disclaimer 2: I HAVE NO IDEA IF FROMSOFT TRACKS SPEED OF KEY PRESSES SO PLEASE TAKE NECESSARY PRECAUTIONS TO PREVENT ANY POSSIBLE BANS

## Prerequisites:
- Have Windows Powershell
- HIGHLY recommend Microsoft Visual Studio Code with the Python extension to simplify code changes and execution
- Something to open up ZIP files with, like 7-Zip or WinRAR
- Dark Souls: Prepare to Die Edition preferably, otherwise the cash grab known as "Remastered"
    - Make the character beforehand, chat will not have full access to the keyboard to write the character name, and they will probably get stuck in advanced settings

## Requirements:
- Install Python specifically 3.9.6. I am using it at this time on a Windows 10 64-bit computer. Can be found at Python website [here](https://www.python.org/downloads/)
    - After downloading, right click the installer to run it in administrator mode 
    - Choose the destination path to be in your main drive's Program Files(x86) path, for example: `C:\Program Files (x86)`
    - Make sure to choose to install 'pip', 'Documentation', 'tcl/tk and IDLE', and 'Python test suite' with the installer
    - In advanced settings of installer, select:
        - 'Install for all users'
        - 'Create shortcuts for installed applications'
        - 'Add Python to environment variables'
        - 'Precompile standard library'
- Install a Python library called 'pywin32'
    1. Open up Command Prompt (or Windows Powershell)
    2. Input the command below to install
    ```
    pip install pywin32
    ```
- Authentication token for Twitch connection
    - Generate an OAuth token with this website [here](https://twitchapps.com/tmi/)
    - KEEP THE TOKEN HANDY, YOU NEED TO EDIT A SCRIPT AND PASTE THE TOKEN

## Installation:
- Download this script by clicking the green Code button on top, and 'Download as ZIP'
- Save the zip contents somewhere you can easily access it
- Open up `main.py` preferably with Microsoft VS Code, otherwise Notepad
- Paste the OAUTH Token from above in the line that starts with `token =`
- Replace `nickname` to your username
- Replace `channel` to your username but with a `#` in front and no space (i.e. `#mohomie`)
- Save your changes

## Preparing the game:
- Boot up Dank Souls
- Go to the settings where you configure keybinds (we are NOT using a controller to keep this as simple as possible, but you can have it connected too)
- Change the controls to the following... TODO

## Execution:
- If using Microsoft VS Code to make the replacements above:
    - press CTRL+` to open up a terminal at the bottom of your screen
    - In that terminal just type `python .\main.py`
    - You'll see some print messages but if the last couple of lines say NEW MESSAGE in them, it should be working.
    - Click into the window where DS1 is to focus onto the game
    - Go for it!

## TODO:
[ ] Perform stress testing by simulating a rowdy twitch chat and seeing how program holds up
[ ] Add some sort of failsafe command
[ ] Validate that above readme works
[ ] Modify controls to use letter keys only
[ ] Provide control mapping in README