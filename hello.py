import sys


def slovak():
    print("ahoj")


def default():
    print("hello")


def main():
    if sys.argv[1] == "sk":
        slovak()
    else:
        default()


if __name__ == "__main__":
    # toto je komentar
    main()
