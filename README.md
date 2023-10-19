# Morse Code Converter

This is a simple Python program that allows you to convert text into Morse code and vice versa.

## Usage

To use the program, run the script `main.py` in your Python environment. You will be prompted to choose between converting text into Morse code or converting Morse code into text.

If you choose to convert text into Morse code, you will be asked to provide the text you want to convert. The program will then output the corresponding Morse code.

If you choose to convert Morse code into text, you will be asked to provide the Morse code you want to convert. The program will then output the corresponding text.

## Morse Code Dictionary

The program uses the following Morse code dictionary:

```python
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}
