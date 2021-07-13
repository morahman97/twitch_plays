# twitch_plays_souls

## Important Notes
Disclaimer 1: **Please be aware that other people will be simulating keyboard presses to your computer. 
While I will do my part to ensure that no harmful scenarios arise,
PLEASE make sure to remove any revealing info from your desktop screen or other running programs if technical difficulties arise when live**

Disclaimer 2: **I have no idea if fromsoft tracks speed of key presses so please take necessary precautions to prevent any possible bans**

## Prerequisites
- Have Windows Powershell on your computer (type 'powershell' in your search bar and see if it shows up)
- HIGHLY recommend Microsoft Visual Studio Code with the Python extension to simplify code changes and execution
- Something to open up ZIP files with, like 7-Zip or WinRAR
- Dark Souls: Prepare to Die Edition preferably, otherwise the cash grab known as "Remastered"
    - Make the character beforehand, chat will not have full access to the keyboard to write the character name, and they will probably get stuck in advanced settings

## Requirements
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

## Installation
- Download this script by clicking the green Code button on top, and 'Download as ZIP'
- Save the zip contents somewhere you can easily access it
- Open up `main.py` preferably with Microsoft VS Code, otherwise Notepad
- Paste the OAUTH Token from above in the line that starts with `token =`
- Replace `nickname` to your username
- Replace `channel` to your username but with a `#` in front and no space (i.e. `#mohomie`)
- Save your changes

## Preparing the game
- Boot up Dank Souls
- Go to the settings where you configure keybinds (we are NOT using a controller to keep this as simple as possible, but you can have it connected too)
- Change the controls to the following... TODO

## Execution
- If using Microsoft VS Code to make the replacements above:
    - press CTRL+` to open up a terminal at the bottom of your screen
    - In that terminal just type `python .\main.py`
    - You'll see some print messages but if the last couple of lines say NEW MESSAGE in them, it should be working.
    - Click into the window where DS1 is to focus onto the game
    - Go for it!

## TODO
[X] Perform stress testing by simulating a rowdy twitch chat and seeing how program holds up
    - Can handle random commands with cooldown of 1/100th of a second, possibly more
    - Does not execute all commands due to character being locked in animations

[X] Add some sort of failsafe command
    - **From another device**, type STOP **in all caps** into chat to terminate the program

[X] Validate that above readme works
    - Tested installation settings with downloading ZIP and installing pywin32 only, runs successfully

[X] Modify controls to use letter keys only
    - Already implemented
    
[ ] Provide control mapping in README
