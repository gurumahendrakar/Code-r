# a = "©©©©©©©".encode('latin-1')
# c = a.hex().encode()

# print(bytes.fromhex(c).decode('latin-1'))
# 330a4d243fcbc5444bdaf082f3e2bf25fea46907f0821591ce4114b83eaafdf2
# M���1�*��iy©��


vl = b"Guru"

print(vl.hex())


print(vl.fromhex(vl.hex()))
