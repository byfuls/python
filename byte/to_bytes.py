
a = 16909060

print(a.to_bytes(4, "big"))
print(a.to_bytes(4, "little"))

b = 1

#print(b.to_bytes(1))		ERR
print(b.to_bytes(1, "big"))
print(b.to_bytes(1, "little"))
