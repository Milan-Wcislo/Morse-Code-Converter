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


def encrypt():
    txt_to_encrypt = input("Provide Text to Change It into MORSE CODE: ").upper().strip().split(" ")
    morse_code = ""

    for word in txt_to_encrypt:
        for letter in word:
            try:
                morse_code += MORSE_CODE_DICT[letter] + " "
            except KeyError:
                return "Error: You provided the wrong key! Try again!"
        morse_code += " "

    return morse_code


def decrypt():
    txt_to_decrypt = input("Provide Morse Code to Change It into Text: ").strip()
    normal_text = ""

    if " " in txt_to_decrypt:
        txt_to_decrypt = txt_to_decrypt.split(" ")
    elif "_" in txt_to_decrypt:
        txt_to_decrypt = txt_to_decrypt.split("_")
    elif "." not in txt_to_decrypt or "-" not in txt_to_decrypt:
        return "Error: Please Provide Valid Morse Code Including Commas and Dashes!"
    else:
        return "Error: Can't encrypted. Please Check If you Provide Spaces or Underlines!"

    for symbol in txt_to_decrypt:
        for string, morse in MORSE_CODE_DICT.items():
            if morse == symbol:
                normal_text += string

    return normal_text


while True:
    encrypt_or_decrypt = input(
        "Type 'morse' if you want to convert Text into Morse Code \n"
        "Type 'text' if you want to convert Morse Code into Text \n"
    )
    if encrypt_or_decrypt == "morse":
        print(encrypt())
    else:
        print(decrypt())
    end_program = input("\nIf You Want To Repeat Program, Type 'Yes', Else Type 'No' ").lower()
    if end_program != "yes":
        break
