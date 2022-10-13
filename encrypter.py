from dictionaries import text_to_morse


def encode(unit_time, message):
    encoded = ''
    for i in message:
        if i == ' ':
            encoded = encoded + '#'
        elif i in text_to_morse.keys():
            encoded = encoded + text_to_morse[i] + ' '
        else:
            print('ERROR')
    morse = ''
    for i in encoded:
        if i == '.':
            morse = morse + unit_time*'1' + unit_time*'0'
        elif i == '-':
            morse = morse + unit_time*'111' + unit_time*'0'
        elif i == ' ':
            morse = morse + unit_time*'000'
        elif i == '#':
            morse = morse + unit_time*'0000000'
    return morse.strip('0')


def start():
    result = encode(int(input("Enter unit time: ")), input("Enter message: ").upper())
    print(f'Encrypted message: {result}')
    return result
