class Translator:
    def __init__(self, string: str):
        self.string = string.lower()

        self.morse_code = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----',
            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            ' ': '/'
        }

    def clean_str(self):
        clean_string = self.string
        clean_string = ' '.join(clean_string.split())
        return clean_string

    def translator(self):
        string = self.clean_str()
        morse_code = [self.morse_code[character] for character in string if character in list(self.morse_code.keys())]
        morse_string = ' '.join(morse_code)

        return morse_string

