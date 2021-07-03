import re
from typing import *


class MarkDownContent:
    def __init__(self, header: str):
        self.header = header
        self.content: str = ''
        self.markdowncontents: List[MarkDownContent] = []

    def add_content(self, line: str) -> None:
        self.content = self.content + line

    def add_markdowncontents(self, markdowncontents) -> None:
        self.markdowncontents = markdowncontents

    def __str__(self)->str:
        output: str = self.header+self.content
        for markdowncontent in self.markdowncontents:
            output += markdowncontent.__str__()
        return output

    def __lt__(self, other) -> bool:
        return "".join(re.findall("[a-zA-Z\d\S]+", self.header)) < "".join(re.findall("[a-zA-Z\d\S]+", other.header))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return self.header == other.header
        else:
            return False

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)


# test
assert MarkDownContent("##123") < MarkDownContent("##124")
assert MarkDownContent("##125") > MarkDownContent("##124")
assert MarkDownContent("##123") != MarkDownContent("##124")
assert MarkDownContent("##123") == MarkDownContent("##123")
