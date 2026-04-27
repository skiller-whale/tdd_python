import sys

from src.wordle_app import WordleApp


def main() -> None:
    for line in WordleApp().run(sys.argv[1:]):
        print(line)


if __name__ == "__main__":
    main()
