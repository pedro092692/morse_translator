from translator import Translator
from art import logo


def translate():
    print(logo)
    program_run = True

    while program_run:

        string = input('Please type a text to translate to morse code or type + to exit\n')
        if string == '+':
            print('Good Bye')
            return

        translator = Translator(string=string)
        print(f'Your translate text in morse is: \n {translator.translator()}')


translate()
