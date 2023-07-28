from typing import List


def find_three_word_lines(stroka: List[str]) -> List[str]:
    return [word for word in stroka if len(word) > 3]


if __name__ == '__main__':
    print(find_three_word_lines(input().split(' ')))
