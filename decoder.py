from dictionaries import morse_to_text

# message = '11001100110011000000110000001111110011001111110011111100000000000000110' \
#           '01111110011111100111111000000110011001111110000001111110011001100000011'


def decode_bits(bits_to_decode):
    unit_time = 0
    while True:
        unit_time += 1
        if '1'+unit_time*'0'+'1' in bits_to_decode:
            break
    normalised = bits_to_decode.replace(unit_time*'0', '0').replace(unit_time*'1', '1')\
        .replace('0000000', ' # ').replace('000', ' ')
    morse_message = ''
    while normalised != '':
        if normalised[0:3] == '111':
            morse_message = morse_message + '-'
            normalised = normalised[3:]
        elif normalised[0] == '1' and normalised[0:2] != '111':
            morse_message = morse_message + '.'
            normalised = normalised[1:]
        elif normalised[0] == '0':
            normalised = normalised[1:]
        elif normalised[0] == ' ' or normalised[0] == '#':
            morse_message = morse_message + normalised[0]
            normalised = normalised[1:]
        else:
            print('ERROR')
            normalised = normalised[1:]
    return morse_message


def decode_morse(morse_to_decode):
    letters = morse_to_decode.split(' ')
    text_message = ''
    for morse in letters:
        if morse == '#':
            text_message = text_message + ' '
        elif morse in morse_to_text.keys():
            text_message = text_message + morse_to_text[morse]
    return text_message


def start():
    result = decode_morse(decode_bits(input("Code received: ")))
    print(f'Decoded text: {result}')
    return result
