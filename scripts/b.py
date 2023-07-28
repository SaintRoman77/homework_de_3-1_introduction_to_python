from typing import List


def count_lowels(word: str) -> int:
    lowels = set('аеёиоуыэюя')
    count = 0
    for letter in word.lower():
        if letter in lowels:
            count += 1
    return count


def find_three_lowels_in_words(lst: List[str]) -> List[str]:
    return [word for word in lst if count_lowels(word) > 3]


if __name__ == '__main__':
    result = find_three_lowels_in_words(input('Введите слова через пробел:').split())
    if len(result) > 0:
        print(result)
    else:
        print('Таких слов нет')
