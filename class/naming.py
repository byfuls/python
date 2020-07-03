
class hasPrivate():
    def __init__(self, val):
        self.__private = val

class hasProtected():
    def __init__(self, val):
        self._protected = val

class hasPublic():
    def __init__(self, val):
        self.public = val

pri = hasPrivate(1)
pro = hasProtected(2)
pub = hasPublic(3)

print(f'public: {pub.public}')
print(f'protected: {pro._protected}')
#print(f'private: {pri.__private}')

class wantPrivate(hasPrivate):
    def __init__(self, val):
        super(wantPrivate, self).__init__(val)

    def printPrivate(self):
        print(f'print private val: {self.__private}')

wp = wantPrivate(3)
wp.printPrivate()