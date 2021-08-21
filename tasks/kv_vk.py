from typing import TypeVar
import itertools

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:

    new_dict = {KT: KV for KV, KT in d.items()}
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.
    Например,
    flip_kv_vk({
        'tokyo': 'Токио',
        'moscow': 'Москва',
    }) == {
        'Токио': 'tokyo',
        'Москва': 'moscow',
    }
    """
    return new_dict



def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:

    new_dict = {k: [j for j, _ in list(v)] for k, v in itertools.groupby(d.items(), lambda x: x[1])}


    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - массив ключей конфликтующих
    значений.
    Например,
    flip_kv_vk({
        'Санкт-Петербург': '+3',
        'Москва': '+3',
    }) == {
        '+3':   ['Москва', 'Санкт-Петербург'],
    }
    """
    return new_dict





