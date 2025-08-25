"""
CoreCommands.py       — The core commands into one file

This file contains all the core commands like `clr`, `exit`,
`goto` and more. This file is a module so you can test this as
you want.

Used modules:
    - os
    - typing
"""

import os
from typing import Literal

AUTHOR = "TwellEvans"  # Hey that's me
VERSION = 1.0
COMMANDS = ["clr", "exit", "goto", "ttc", "credits", "repo"]
TTC_NAMES = ["TheTwellyTracker", "TheTwellyEngine", "TheTwellySequencer"]


def ClearScreen():
    """
    This function clears the terminal buffer
    """
    os.system("cls")


def Exit(Code: int):
    """
    Exit()       —— Exit from The Twelly Terminal

    This function makes the program to exit and if it is possible,
    with a code error.

    Arguments: `Code`       —— The output code
    Returns: `NoReturn`
    """
    exit(Code)


def TTCCommand(
    Action: str,
    Program: Literal["TheTwellyTracker", "TheTwellyEngine", "TheTwellySequencer"],
) -> str:
    """
    TTCCommand()       —— Play with The Twelly Creations

    With this function, you can use any of The Twelly Creations. This
    function needs arguments, so you have to specify the arguments.

    Arguments:
        `Action` — The action to do (e.g. `"launch"`, `"info"`, `"authors"`, `changelog`, etc.)
        `Program` — The TTC program to do what the action says
    Returns: `None`
    """
    if Action.lower() not in ["launch", "info", "authors", "changelog"]:
        print("That action does not exist. ")

    STATEMENTS = {
        "launch": {
            "TheTwellyTracker": "Executing The Twelly Tracker...",
            "TheTwellyEngine": "Executing The Twelly Engine...",
            "TheTwellySequencer": "Executing The Twelly Sequencer...",
        },
        "info": {
            "TheTwellyTracker": "Executing The Twelly Tracker Page...",
            "TheTwellyEngine": "Executing The Twelly Engine Page...",
            "TheTwellySequencer": "Executing The Twelly Sequencer Page...",
        },
        "authors": {
            "TheTwellyTracker": "Two2Fall",
            "TheTwellyEngine": "Two2Fall, with some inspirations of the MaxMaxMax engine",
            "TheTwellySequencer": "Two2Fall",
        },
        "changelog": {
            "TheTwellyTracker": "Executing the changelog of The Twelly Tracker Page",
            "TheTwellyEngine": "Executing the changelog of The Twelly Engine Page...",
            "TheTwellySequencer": "Executing the changelog of The Twelly Sequencer Page...",
        },
    }
    return STATEMENTS[Action.lower()][Program]
