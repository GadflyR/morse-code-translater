from Config import *


def text_to_morse(word):
    for i in word.lower():
        print(LETTER_TABLE.get(i), end=' ')
    print('')


def morse_to_text(morse):
    text = ''
    words = morse.split('  ')
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in MORSE_TABLE:
                text += MORSE_TABLE[char]
        text += ' '
    print(text.strip())


def main():
    while 1:
        word = input("input: ")
        text_to_morse(word)
        morse_to_text(word)


if __name__ == '__main__':
    main()
