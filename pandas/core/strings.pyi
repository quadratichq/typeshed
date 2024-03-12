from typing import List, Optional, Union
from .frame import DataFrame
from .series import Series

class StringMethods:
    def contains(
        self, pat: str, case: bool = ..., flags: int = ..., na: float = ..., regex: bool = ...
    ) -> Series[bool]: ...
    def count(self, pat: str, flags: int = ...) -> Series[int]: ...
    def endswith(self, pat: str, na: float = ...) -> Series[bool]: ...
    def find(self, sub: str, start: int, end: int) -> Series[int]: ...
    def findall(self, sub: str, flags: int = ...) -> Series[list]: ...
    def get(self, i: int) -> Series: ...
    def index(self, sub: str, start: int, end: int) -> Series: ...
    def join(self, sep: str) -> Series: ...
    def len(self) -> Series[int]: ...
    def ljust(self, width: int, fillchar: str) -> Series: ...
    def lower(self) -> Series[str]: ...
    def lstrip(self, to_strip: str = ...) -> Series: ...
    def match(self, pat: str, case: bool = ..., flag: int = ..., na: float = ...) -> Series: ...
    def pad(self, width: int, side: str = ..., fillchar: str = ...) -> Series: ...
    def repeat(self, repeats: Union[int, List[int]]) -> Series: ...
    def rfind(self, sub: str, start: int, end: int) -> Series[int]: ...
    def rindex(self, sub: str, start: int, end: int) -> Series: ...
    def rjust(self, width: int, fillchar: str) -> Series: ...
    def rstrip(self, to_strip: Optional[str] = ...) -> Series: ...
    def slice(self, start: Optional[int], stop: Optional[int], step: Optional[int]) -> Series: ...
    def slice_replace(
        self, start: Optional[int], stop: Optional[int], repl: Optional[str]
    ) -> Series: ...
    def split(self, pat: Optional[str], n: int = ..., expand: bool = ...) -> Series: ...
    def rsplit(self, pat: Optional[str], n: int = ..., expand: bool = ...) -> Series: ...
    def startswith(self, pat: str, na: float = ...) -> Series: ...
    def strip(self, to_strip: Optional[str] = ...) -> Series: ...
    def translate(self, table: dict) -> Series: ...
    def wrap(
        self,
        width: int,
        expand_tabs: Optional[bool],
        replace_whitespace: Optional[bool],
        drop_whitespace: Optional[bool],
        break_long_words: Optional[bool],
        break_on_hyphens: Optional[bool],
    ) -> Series: ...
    def zfill(self, width: int) -> Series: ...
    def get_dummies(self, sep: str = ...) -> DataFrame: ...