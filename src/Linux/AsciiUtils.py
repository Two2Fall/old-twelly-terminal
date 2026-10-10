"""
AsciiUtils.py           — A python file to create text sections and better ascii documents

This is a python file to create paragraphs and ascii documents better. This
file includes the `TextSection()` class and the pages.
Used modules:
    - rich
    - typing
"""

from rich.console import Console
from typing import Union, Literal

AUTHOR = "TwellEvans"  # Do not change this
VERSION = 1.0


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

        This method appends a paragraph into the text section, it can have style, so
        you can personalize the text as you want.

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
    Returns: `Document()`
    """

    def __init__(self, DocumentName: str, DocumentAuthor: str) -> None:
        self.Name = DocumentName
        self.Author = DocumentAuthor
        self.Filename = f"{self.Name}_{"".join(self.Author.split(" "))}.asciidoc"
        self.Data = {}
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
            `DocumentName`: This parameter denotes the ascii document name
            `DocumentAuthor`: This parameter denotes the author of the ascii document
        Returns: `None`
        """
        self.Data["Header"] = {
            "Text": Text,
            "Subtitle": Subtitle,
            "Style": {
                "Text Color": TextStyle.get("Color", "#FFFFFF"),
                # It also could be a gradient like this
                # `Gradient(ColorA, ColorB)`
                "Text Weight": TextStyle.get("Text Weight", "Normal"),
                "Text Align": TextStyle.get("Align", "Center"),
                "Text Font": TextStyle.get("Font", "Title"),
                "Subtitle Color": SubtitleStyle.get("Color", "#FFFFFF"),
                "Subtitle Weight": SubtitleStyle.get("Weight", "Normal"),
                "Subtitle Align": SubtitleStyle.get("Align", "Center"),
            },
        }
