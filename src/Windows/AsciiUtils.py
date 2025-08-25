"""
AsciiUtils.py           — A python file to create text sections and better ascii documents

This is a python file to create paragraphs and ascii documents better. This
file includes the `TextSection()` class and the pages.
Used modules:
    - rich
    - typing
    - pyfiglet
"""

from rich.console import Console
from rich.text import Text
from rich.color import Color
from rich.align import Align
from typing import Union, Literal
import pyfiglet as pf

AUTHOR = "TwellEvans"  # Do not change this
VERSION = 1.0


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


class TextSection:
    """
    TextSection()         —— A class for text sections

    This class provides methods for text sections in the document, this text
    can be stylized without any problem, because this class use the rich module

    Arguments:
        `Indentation` — The indentation symbol and amount of this document,
        `Console`: — To be better compatible, this class needs a console to render the text section
    Returns: `TextSection()`
    """

    def __init__(self, TabAmount: tuple[str, int], Console: Console) -> None:
        self.Paragraphs = []
        self.TabAmount = TabAmount
        self.Console = Console

    def AppendParagraph(self, Paragraph: str):
        """
        `TextSection().AppendParagraph()`         —— A method to append paragraphs

        This method appends a paragraph into the text section.

        Arguments:
            `Paragraph` — The paragraph to append
        Returns: `None`
        """
        self.Paragraphs.append(Paragraph)

    def RenderAll(self):
        """
        `TextSection().RenderAll()`         —— A method to render the text section

        This method renders the entire text section.

        Arguments: `None`
        Returns: `None`
        """
        for Paragraph in self.Paragraphs:
            self.Console.print(self.TabAmount + Paragraph)

    def GetParagraph(self, ParagraphIndex: int | tuple[int, int]):
        """
        `TextSection().GetParagraph()`      —— A method to get a paragraph by index

        If you need to get a paragraph by index
        use this method.

        Arguments:
            `ParagraphIndex` — The paragraph index
        Returns: `str` or `list`
        """
        if isinstance(ParagraphIndex, tuple):
            return self.Paragraphs[ParagraphIndex[0] : ParagraphIndex[1]]
        elif (
            isinstance(ParagraphIndex, int)
            and ParagraphIndex >= 0
            and ParagraphIndex < len(self.Paragraphs)
        ):
            return self.Paragraphs[ParagraphIndex]

    def RenderPart(self, Indexes: tuple[int, int]):
        """
        `TextSection().RenderPart()`      —— A method to render paragraphs by indexes

        This method is to render a part of the ascii document. This is good if you want to
        import quotes or any important text instead of importing all document

        Arguments:
            `Indexes` — This parameter is for the extracted text document (line by line)
        Returns: `list`
        """
        return self.Paragraphs[Indexes[0] : Indexes[1]]


# Alright, so if I finished the TextSection() class
# The next step, is the ascii document class


class Document:
    """
    Document()         —— A class for an entire ascii document

    This class is created for ascii documents, with title, header, contents,
    indentation, sections, and more. This can import, export and render `asciidoc` files.

    Arguments:
        `DocumentName`: This parameter denotes the ascii document name
        `DocumentAuthor`: This parameter denotes the author of the ascii document
        `Console`: This class needs a console class to render the document, so it needs this
    Returns: `Document()`
    """

    def __init__(
        self, DocumentName: str, DocumentAuthor: str, Console: Console
    ) -> None:
        self.Name = DocumentName
        self.Author = DocumentAuthor
        self.Filename = f"{self.Name}_{"".join(self.Author.split(" "))}.asciidoc"
        self.Data = {}
        self.Console = Console
        # The structure in this attribute (self.Data) will
        # look like this
        """
        {
            "DocumentName": "ExampleDocument",
            "DocumentAuthor": ["Ameen272"],
            "CreationDate": "10-8-2025 13:13 (GMT-4)",
            "Data": {
                "Header": {
                    "Text": "Example Document",
                    "Subtitle": "Example Subtitle",
                    "Style": {
                        "Color": "Gradient(#000000, #FFFFFF)",
                        "TextWeight": "Bold",
                        "TextAlign": "Center",
                        "Font": "Title Font"
                    },
                ...
                }
            }
        }
        """

    def ImportHeader(
        self,
        Text: str,
        Subtitle: str,
        TextStyle: dict[str, Union[str, int]],
        SubtitleStyle: dict[str, Union[str, int]],
    ):
        """
        Document.ImportHeader()         —— A method to import a header in this class

        This method imports and creates a header in the document. This method has so many
        arguments, because this includes style and color, and more stuff.

        Arguments:
            `Text`: This parameter denotes the header text
            `Subtitle`: This parameter denotes the subtitle text
            `TextStyle`: This parameter denotes the header text style
            `SubtitleStyle`: This parameter denotes the subtitle text style
        Returns: `None`
        """
        self.Data["Header"] = {
            "Text": Text,
            "Subtitle": Subtitle,
            "Style": {
                "Text Color": TextStyle.get("Color", "Gradient(#FFFFFF,#FFFFFF)"),
                # It must be a gradient
                "Text Weight": TextStyle.get("Weight", "Normal"),
                "Text Align": TextStyle.get("Align", "Center"),
                "Subtitle Color": SubtitleStyle.get("Color", "#FFFFFF"),
                "Subtitle Weight": SubtitleStyle.get("Weight", "Normal"),
                "Subtitle Align": SubtitleStyle.get("Align", "Center"),
            },
        }

    def ImportTextSection(self, Object: TextSection, TextSectionName: str):
        """
        Document.ImportTextSection()         —— A method to import a text section in this class

        This method imports and creates a text section the document. This text section must be
        be below the header, otherwise, it will return an error.

        Arguments:
            `Object`: This parameter denotes the `TextSection()` object to import
            `TextSectionName`: To identify this text section, this needs the text section name or ID
            `Style`: This parameter denotes the text style
        Returns: `None`
        """
        self.Data[f"Text Section #{TextSectionName}"] = {
            "Text": "\n".join(Object.Paragraphs),  # The text already has style
        }

    def RenderDocument(self):
        """
        Document.Render()        —— A method to render the document

        This method renders the entire document.

        Arguments: No arguments
        Returns: `None`
        """

        # First process - Render the header
        Header = self.Data["Header"]
        Style = Header["Style"]
        HeaderText = str(pf.figlet_format(text=Header["Text"]))
        TextColor = Style["Text Color"]
        StartColor, EndColor = TextColor[
            TextColor.index("(") + 1 : TextColor.index(")")
        ].split(",")
        StylizedHeader = Gradient(HeaderText, StartColor, EndColor)
        StylizedHeader = Align(StylizedHeader, Header["Text Align"])
        self.Console.print(StylizedHeader, Style["Text Weight"])

        # Second process - Render the subtitle
        SubtitleText = Header["Subtitle"]
        SubtitleColor = Style["Subtitle Color"]
        SubtitleWeight = SubtitleColor + Style["Subtitle Weight"]
        StylizedSubtitleText = Align(SubtitleText, Style["Text Align"])
        self.Console.print(StylizedSubtitleText, SubtitleWeight)
        Char = "─" * 128
        Char = Align.center(Char)
        self.Console.print(Char, style="white bold")


# lemme test  ts
DocumentExample = Document("Twellideus", "Twell Evans", Console())

DocumentExample.ImportHeader(
    Text="The Twellideus",
    Subtitle="",
    TextStyle={
        "Color": "Gradient(#6F00FF,#FFFFFF)",
        "Weight": "Bold",
        "Align": "Center",
    },
    SubtitleStyle={
        "Color": "#FFFFFF",
        "Weight": "Normal",
        "Align": "Center",
    },
)
DocumentExample.RenderDocument()
