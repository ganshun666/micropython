try:
    import ubinascii as binascii
except ImportError:
    import binascii

print(binascii.unhexlify(b'0001020304050607'))
print(binascii.unhexlify(b'08090a0b0c0d0e0f'))
print(binascii.unhexlify(b'7f80ff'))
print(binascii.unhexlify(b'313233344142434461626364'))
