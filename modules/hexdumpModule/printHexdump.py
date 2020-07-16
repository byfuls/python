def print_hex_dump(buffer, start_offset=0):
    print('-' * 79)
 
    offset = 0
    while offset < len(buffer):
        # Offset
        print(' %08X : ' % (offset + start_offset), end='')
 
        if ((len(buffer) - offset) < 0x10) is True:
            data = buffer[offset:]
        else:
            data = buffer[offset:offset + 0x10]
 
        # Hex Dump
        for hex_dump in data:
            print("%02X" % hex_dump, end=' ')
 
        if ((len(buffer) - offset) < 0x10) is True:
            print(' ' * (3 * (0x10 - len(data))), end='')
 
        print('  ', end='')
 
        # Ascii
        for ascii_dump in data:
            if ((ascii_dump >= 0x20) is True) and ((ascii_dump <= 0x7E) is True):
                print(chr(ascii_dump), end='')
            else:
                print('.', end='')
 
        offset = offset + len(data)
        print('')
 
    print('-' * 79)

def return_hex_dump(buffer, titleMsg=None, start_offset=0):
    ret = '-' * 79
    ret += '\n'
    if titleMsg is not None:
        ret += titleMsg
        ret += '\n'

    offset = 0
    while offset < len(buffer):
        # Offset
        ret += (' %08X : ' % (offset + start_offset))

        if ((len(buffer) - offset) < 0x10) is True:
            data = buffer[offset:]
        else:
            data = buffer[offset:offset + 0x10]

        # Hex Dump
        for hex_dump in data:
            ret += ("%02X" % hex_dump)
            ret += ' '

        if ((len(buffer) - offset) < 0x10) is True:
            ret += (' ' * (3 * (0x10 - len(data))))

        ret += ('  ')

        # Ascii
        for ascii_dump in data:
            if ((ascii_dump >= 0x20) is True) and ((ascii_dump <= 0x7E) is True):
                ret += (chr(ascii_dump))
            else:
                ret += ('.')
        ret += '\n'

        offset = offset + len(data)
        ret += ('')

    ret += ('-' * 79)
    return ret

if __name__ == "__main__":
    sample = bytearray('12341234123412341234123400000000000000'.encode())
    print_hex_dump(sample)
    print(return_hex_dump(sample))
    print(return_hex_dump(sample, 'sample title message'))
