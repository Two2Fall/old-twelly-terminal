"""
TheTwellyUtil.py       — A util for terminals created by Twell Evans

The Twelly Util is a util created by me that helps Two2Fall (Also known as Twell Evans)
to be able to program better with an stylized terminal written in python. This does not
need commands and dependencies so I hope you like this!

Used modules:
    - rich
    - time
    - subprocess
    - os
    - random
    - sys
    - signal
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.color import Color
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from rich.progress import track
import os
import random
import time
import subprocess
import sys
import signal

# Important constants
# These are the most important constants because
# without them, this program could have an error

HOME_DIR = os.path.expanduser("~")
CONF_DIR = os.path.join(HOME_DIR, "AppData", "Local", "The_Twelly_Terminal")
DATA_PATH = os.path.join(CONF_DIR, "data.txt")
TERMINAL_NAME = "Twelly Terminal"
AUTHOR = "TwellEvans"


def SigHan(sig, frame):
    """
    SigHan()        -- A function that handles the SIGINT (Exit) CTRL-C signal.
    """
    sys.exit(0)


signal.signal(signal.SIGINT, SigHan)


def DataRet():
    os.makedirs(CONF_DIR, exist_ok=True)

    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as file:
            lines = file.readlines()
            USERNAME = lines[0].strip()
            DEVICE = lines[1].strip()
    else:
        USERNAME = input("Enter your prefer<red username: ")
        DEVICE = input("Enter your preferred hostname/device name: ")

    with open(DATA_PATH, "w") as file:
        file.write(f"{USERNAME}\n{DEVICE}\n")

    return USERNAME, DEVICE


USERNAME, DEVICE = DataRet()
TT_ASCII_ART = R""" _____ _            _____              _ _         _____                   _             _ 
|_   _| |__   ___  |_   _|_      _____| | |_   _  |_   _|__ _ __ _ __ ___ (_)_ __   __ _| |
  | | | '_ \ / _ \   | | \ \ /\ / / _ \ | | | | |   | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
  | | | | | |  __/   | |  \ V  V /  __/ | | |_| |   | |  __/ |  | | | | | | | | | | (_| | |
  |_| |_| |_|\___|   |_|   \_/\_/ \___|_|_|\__, |   |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|
                                           |___/                                           """

TwellyConsole = Console()

SPLASHTEXTS = [
    "I'mma twellify you with this one!",
    "SophianPVM was inspired by MSDOS and UNIX!",
    'Go use my tracker called "The Twelly Tracker"',
    "Uh insert text here",
    "The Twellideus are going to eat temporal files again",
    "CMD is an absolutely trash, instead, try this shit because why not",
    "Bash ain't bad, but it's so POSIX, try this shit because why not",
    "Evanic Twell is twelve years old",
    "use PascalCase instead of that boring snake_case in Python!",
    "Insert another text here",
    "HelloWorld(print)",
    "[object Object]",
    "r/DontTypeLikeThis",
    "ByteBeat is the best music genre in the universe",
    "Including chiptune",
    "POSIX compliance is just a social construct",
    "I compiled this shit in my head, don't try this if you're a POSIXer",
    "DdDdDdDdDdDdDddDdDddDdDdDdD",
    "Chasyxx is the goat",
]


def RunCommand(Command: str) -> None:
    """
    RunCommand(Command: str) -> None        -- A function that runs commands from the ./commands/ directory.
    """

    Parts = Command.split(" ", 1)
    FileName = Parts[0]
    Args = Parts[1].split() if len(Parts) > 1 else []

    FilePath = os.path.join("./commands", FileName + ".py")

    if not os.path.exists(FilePath):
        print(" " * 19, "Error: Command not found or no command provided.")
        return

    CommandToRun = ["python", FilePath] + Args

    process = subprocess.Popen(CommandToRun)
    process.wait()


def Gradient(InputText: str, StartColor: str, EndColor: str):
    """
    Gradient()         —— A function that creates a gradient to make texts more beautiful

    This function creates a gradient to make texts more beautiful, you can put any
    `Renderable()` type object (like `str`, `Panel`, `Text` ...) so this may be
    flexible and too much good if you want to stylize your text

    Arguments:
        `InputText` — The text or `Renderable()`-like object to stylize
        `StartColor` — The first gradient color (this must be a hexadecimal color code)
        `EndColor` — The end gradient color (this also must be a hexadecimal color code)
    Returns: `Text`
    """
    Result = Text()

    DecodedStartColor = Color.parse(StartColor).triplet
    DecodedEndColor = Color.parse(EndColor).triplet
    Length = len(InputText)

    for Index, Char in enumerate(InputText):
        R = int(
            DecodedStartColor[0]  # type: ignore
            + (DecodedEndColor[0] - DecodedStartColor[0]) * Index / (Length - 1)  # type: ignore
        )
        G = int(
            DecodedStartColor[1]  # type: ignore
            + (DecodedEndColor[1] - DecodedStartColor[1]) * Index / (Length - 1)  # type: ignore
        )
        B = int(
            DecodedStartColor[2]  # type: ignore
            + (DecodedEndColor[2] - DecodedStartColor[2]) * Index / (Length - 1)  # type: ignore
        )
        Result.append(Char, style=f"rgb({R},{G},{B})")

    return Result


def ClearScreen():
    """
    This function clears the screen
    """
    os.system("clear")


def RenderGreatTitle(
    AsciiArt: str,
    GradientColors: tuple[str, str],
    SubtitleText: str,
    SubtitleTextStyle: str,
):
    """
    RenderGreatTitle()       —— A function that creates a title as an ascii document title

    This function creates a large text title with subtitle and a line, this could be useful to make
    ascii documents better, do not use this on a section of the document that is not the title. This
    is only created to style

    Arguments:
        `AsciiArt` — This function needs an ascii art to make the title greater
        `GradientColors` — The gradient colors to stylize the title
        `SubtitleText` — This is the subtitle text to put in the title, it must be not too long
        `SubtitleTextStyle` — The subtitle style

    Returns: `None`
    """
    InputText = Gradient(AsciiArt, GradientColors[0], GradientColors[1])
    TwellyConsole.print(Align(InputText, "center"))
    TwellyConsole.print(
        Align("\n" + SubtitleText, "center"), style=SubtitleTextStyle.lower()
    )
    Char = "─" * 128
    TwellyConsole.print(Align.center(Char), style="white bold")


def RenderParagraph(Lines: list[str], Indentation: str):
    """
    RenderParagraph()      —— A function that renders a paragraph in the ascii document

    This function creates a paragraph to put it in the ascii document, this needs style
    in the words, like `[red bold]this is a text in red bold[/red bold]`. You can use this only
    on ascii documents, not as a normal stylized text.

    Arguments:
        `Lines` — The paragraph lines are here, so you need to put the paragraphs here
        `Indentation`: — The paragraph needs indentation lines to make this document more readable

    Returns: `None`
    """
    for Line in Lines:
        TwellyConsole.print(Indentation + Line)

ClearScreen()
RenderGreatTitle(
    TT_ASCII_ART,
    ("#220092", "#FF00BB"),
    random.choice(SPLASHTEXTS),
    "Green Italic",
)
Paragraphs = [
    "Welcome to the [bold]Twelly Terminal![/bold]\n",
    "This terminal is an util for Two2Fall because he needed to create an good terminal because CMD is so bad for him and Bash was so",
    "POSIX. so he created this for himself and obviously, you can use it without [green bold]ANY PROBLEM![/green bold], you will see the [italic]Two2Fall[/italic] stuff here",
    "like: ",
    " " * 4 + "- [italic]ByteBeat[/italic] music",
    " " * 4 + "- [cyan bold underline]Ultrabox and Beepbox[/cyan bold underline] music",
    " " * 4 + "- [blue bold]The Twellideus[/blue bold] (That's a cool stuff)",
    " " * 4 + "- [magenta bold]SophianPVM[/magenta bold] (Project)",
    " " * 4 + "- And [green bold]MORE STUFF![/green bold]",
    f"I know you are using this program on [green bold]{"windows" if os.name == "nt" else "a posix system"}[/green bold], that wasn't important but well. This is the index",
    "of the ascii document, so, in what page you wanna go?",
    "Pages written by the author:\n",
    " " * 4 + "- About Two2Fall",
    " " * 8 + "- [green italic]Who he is[/green italic]",
    " " * 8 + "- [red bold]The complete history of Two2Fall (Long)[/red bold]",
    " " * 8 + "- [cyan bold]Systhema Digitalis I[/cyan bold]",
    " " * 4 + "- ByteBeat Related",
    " " * 8 + "- [green italic]Songs created by him using ByteBeat[/green italic]",
    " " * 8 + "- [green italic]Bytebattle[/green italic]",
    " " * 8 + "- [cyan bold]The Twelly Creations[/cyan bold]",
    " " * 12 + "- [cyan bold]The Twelly Tracker[/cyan bold]",
    " " * 12 + "- [cyan bold]The Twelly Sequencer[/cyan bold]",
    " " * 12 + "- [cyan bold]The Twelly Engine[/cyan bold]",
    " " * 12 + "- [cyan bold]The Twelly Terminal[/cyan bold]",
    " " * 8
    + "- [green italic]Cover of BeepBox songs created by him using ByteBeat[/green italic]",
    " " * 8 + "- [red bold]Most remixed Two2Fall's song ever (long list)[/red bold]",
    "Well, there are more stuff and I want to show us about them. Just read",
    " " * 4 + "- [green bold]ByteBeat tools[/green bold]",
    " " * 4
    + "- Use any tool of the [italic]Twelly Creations[/italic] online in this terminal",
]
RenderParagraph(Paragraphs, " " * 19)
try:
    while True:
        Selector = Prompt.ask(
            " " * 19
            + f"[italic green]{USERNAME}[/italic green][cyan]@{DEVICE}[/cyan] ~$"
        )
        RunCommand(Selector)
except KeyboardInterrupt:
    pass
