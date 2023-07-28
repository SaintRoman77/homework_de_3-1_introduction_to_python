from typing import List


def remove_not_unique_elements(lst: List) -> List:
    unique_lst = set()
    return [
        value for value in lst if value not in unique_lst
        and not unique_lst.add(value)
    ]


if __name__ == '__main__':
    lst = [3, 1, 2, 4, 7, 0, 8, 0, 1, 4, 2, 2]
    print(remove_not_unique_elements(lst))
