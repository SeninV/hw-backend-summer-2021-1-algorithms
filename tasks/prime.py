__all__ = (
    'is_prime',
)
def is_prime(number: int) -> bool:
    k = 0
    if number > 1 :

        for i in range(2, number // 2 + 1):
            if (number % i == 0):
                k = k + 1
        if (k <= 0):
            Flag = True
        else:
            Flag = False
    else:
        Flag = False

    """
    Функция должна вернуть True если число является простым, иначе - False
    """

    return Flag

