from typing import List


def remove_even_elements(lst: List) -> List:
    lst = [value for index, value in enumerate(lst) if index % 2 != 0]
    return lst


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    print(remove_even_elements(lst))
