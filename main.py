import translator
import sound

print(
    'If you want convert text to morse code, type: Text to Morse(TtM)\n'
    'If you want convert Morse code to text, type: Morse to Text(MtT)\n'
    'If you want audio morse code, type: Morse to Audio(MtA)\n'
    'Enter /Q to quit'
)

while True:
    choice = input('What action: ')
    if choice == 'TtM' or choice == 'Text to Morse':
        minput = input('Put the text you want to convert into Morse code: ')
        if minput == '/Q':
            quit(0)
        translator.TtM(minput)
    elif choice == 'MtT' or choice == 'Morse to Text':
        minput = input('Put the Morse code you want to convert into text: ')
        if minput == '/Q':
            quit(0)
        translator.MtT(minput)
    elif choice == 'MtA' or choice == 'Morse to Audio':
        minput = input('Put the Morse code you want to convert to audio: ')
        if minput == '/Q':
            quit(0)
        sound.sound_morse(minput)
    elif choice == '/Q':
        quit(0)
    else:
        print('Your action in invalid')