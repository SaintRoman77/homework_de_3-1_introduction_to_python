import csv


def read_csv_and_create_dict() -> dict:
    with open('test_csv.csv', 'r', encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter=',')
        result = {}
        for row in data:
            result[row['NAME']] = dict(
                zip(
                    ['GENDER', 'AGE', 'SALARY'],
                    [row['GENDER'], row['AGE'], row['SALARY']]
                )
            )
        return result


if __name__ == '__main__':
    print(read_csv_and_create_dict())




