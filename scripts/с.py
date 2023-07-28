from typing import List


def find_second_max_value(lst: List[int]) -> int:
    lst.sort(reverse=True)
    return lst[1]


if __name__ == '__main__':
    lst = [3, 1, 2, 4, 7, 0, 8]
    print(find_second_max_value(lst))
