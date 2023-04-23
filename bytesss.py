a = "©©©©©©©".encode('latin-1')
c = a.hex().encode()

print(bytes.fromhex(c).decode('latin-1'))

print('\xc2\xa9\xc2\xa9\xc2\xa9\xc2\xa9\xc2\xa9\xc2\xa9\xc2\xa9')