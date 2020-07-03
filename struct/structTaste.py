import struct

##############################################################################
ret = struct.pack('BBBB', 1,2,3,4)
print(ret)

##############################################################################
ret = struct.pack('hhl', 1,2,3)
print(ret)


##############################################################################
record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)
print(f'name:{name}, serialnum:{serialnum}, school:{school}, gradelevel:{gradelevel}')

from collections import namedtuple
Student = namedtuple('Student', 'name serialnum school gradelevel')
ret = Student._make(struct.unpack('<10sHHb', record))
print(f'Student:{ret}')
print(f'Student.name:{ret.name}')
print(f"Student.name:{getattr(ret, 'name')}")
print(f'Student.school:{ret.school}')
