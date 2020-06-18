from abc import *

class abstractClass(metaclass=ABCMeta):
    @abstractmethod
    def personName(self):
        pass
    @abstractmethod
    def personIdNumber(self):
        pass
    @abstractmethod
    def showPersonInformation(self):
        pass

class personIdentification(abstractClass):
    def __init__(self):
        print("let's start")
    def personName(self, name):
        self.name = name
    def personIdNumber(self, id):
        self.id = id
    def showPersonInformation(self):
        print(f'[show] name:{self.name} id:{self.id}')

Jason = personIdentification()
Jason.personName("Jason")
Jason.personIdNumber(18)
Jason.showPersonInformation()