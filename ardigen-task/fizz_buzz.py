FIZZ = 'Fizz'
BUZZ = 'Buzz'


def fizz_buzz(begin: int, end: int) -> None:
    if 1 <= begin < end <= 10000:
        is_fizz = lambda num: num % 3 == 0
        is_buzz = lambda num: num % 5 == 0

        for num in range(begin, end + 1):
            if is_fizz(num) and is_buzz(num):
                print(f'{FIZZ}{BUZZ}')
            elif is_fizz(num):
                print(FIZZ)
            elif is_buzz(num):
                print(BUZZ)
            else:
                print(num)
    else:
        raise Exception('Error!')


if __name__ == "__main__":
    fizz_buzz(3, 16)
