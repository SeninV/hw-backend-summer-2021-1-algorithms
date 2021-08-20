__all__ = (
    'even_odd',
)

def even_odd(arr: list[int]) -> float:
    sum_even = 0
    sum_odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            sum_even += arr[i]
        else:
            sum_odd += arr[i]

    if sum_odd == 0:
        even_odd = 0
    else:
        even_odd = sum_even/sum_odd
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    return even_odd
