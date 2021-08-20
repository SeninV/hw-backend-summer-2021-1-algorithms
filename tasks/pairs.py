from typing import Any

__all__ = (
    'corresponding_pairs',
)

 # ([1, 2, 5, 6], [3, 4], [(1, 3), (2, 4)])


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    dlina = min(len(arr1), len(arr2))
    slov = []
    for i in range(dlina):
        slov.append(tuple([arr1[i], arr2[i]]))

    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
     """
    return slov

print(corresponding_pairs([1, 2, 3], [3, 4]))
