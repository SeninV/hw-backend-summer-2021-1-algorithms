from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    try:
        longest = max(text.split(), key = len)
        shortest = min(text.split(), key = len)
    except:
        longest = None
        shortest = None

    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    return tuple([shortest, longest])
