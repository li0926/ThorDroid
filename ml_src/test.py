from reader import read_constant


def main():
    data = read_constant()
    global KFCV
    KFCV = data['KFCV']


def demo():
    print(KFCV)


if __name__ == '__main__':
    main()
    demo()
