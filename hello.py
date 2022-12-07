import sys


def test():
    pass

def french():
    print("bonjour")


def slovak():
    print("ahoj")


def default():
    print("hello")


def main():
    if sys.argv[1] == "fr":
        french()
    elif sys.argv[1] == "sk":
        slovak()
    else:
        default()


if __name__ == "__main__":
    # toto je komentar
    # toto je dalsi komentar
    main()
