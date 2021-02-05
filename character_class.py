"""Gives an object for the Mandarin Chinese characters."""

class Character:
    """A Chinese character with complimenting symbol, pinyin, definition, and example (overtime)."""
    symbol: str
    pinyin: str
    definition: str
    # example: str

    def __repr__(self, symbol: str, pinyin: str, definition: str) -> str:
        """Constructor for Character Object."""
        self.symbol = symbol
        self.pinyin = pinyin
        self.definition = definition

cat: str = "bob"