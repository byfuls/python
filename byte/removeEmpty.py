
sample = b'\x00\x31\x32\x00'
print(sample)

# comprehension
ret1 = bytearray([v for v in sample if v])
print(ret1)

#ret2 = list(filter(None, sample))
ret2 = bytearray((filter(None, sample)))
print(ret2)
