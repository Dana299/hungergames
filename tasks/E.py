import re
from collections import Counter

from tasks.F import log_exec_time


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text

    @log_exec_time
    def get_longest(self):
        """Print the longest word from the text."""
        clean_text = self._get_clean_text()
        longest = max(clean_text.split(), key=len)
        print("Longest word: ", longest)

    @log_exec_time
    def get_most_common(self):
        """Print the most common word from the text."""
        clean_text = self._get_clean_text()
        counter = Counter(word.lower() for word in clean_text.split())
        print("Most common word: ", counter.most_common(1)[0][0])

    @log_exec_time
    def get_special_symbols_number(self):
        """Print the number of special symbols in the text."""
        special_symbols = "!@#$%^&*()-_+=~`[]{}|\\:;\"'<>?,./"
        num = len([sym for sym in self.text if sym in special_symbols])
        print("Number of special symbols: ", num)

    @staticmethod
    def _is_palyndrom(word) -> bool:
        """Return True if a given word is palyndrom."""
        return word == word[::-1]

    def _get_clean_text(self) -> str:
        """Return text without special symbols."""
        clean_text = re.sub(r'[^\w\s]', '', self.text)
        return clean_text

    @log_exec_time
    def get_palyndromes(self):
        """Print all palindromes from the text."""
        clean_text = self._get_clean_text()
        palyndromes_set = set(
            filter(TextAnalyzer._is_palyndrom, (word.lower() for word in clean_text.split()))
        )
        print("Palyndromes: ", ', '.join(palyndromes_set))
