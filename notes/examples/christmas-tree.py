def tree(height: int) -> None:
    start = int((height + 2) * 0.5)
    for i in range(height - 1):
        print(*((start - i) * ' '), *((i + i + 1) * ['*']))
    print(*((height + 2) * ['*']))


def tree2(n):
    for i in range(n):
        print(' ' * (n - (i + 1)), '*' * (i + i + 1))


if __name__ == "__main__":
    tree(3)
    tree2(5)

    for i in range(1, 20, 2):
        print(('*' * i).center(20))

    for leg in range(3):
        print(('||').center(20))

    print(('\====/').center(20))
