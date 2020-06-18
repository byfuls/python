from abc import *

class abcClass(metaclass=ABCMeta):
    @abstractmethod
    def sayMyName(self):
        pass

class A_class(abcClass):
    def __init__(self):
        print(f'[{type(self).__name__}] init')

    def sayMyName(self):
        print(f'[{type(self).__name__}] say my name!')

class B_class(abcClass):
    def __init__(self):
        print(f'[{type(self).__name__}] init')

    def sayMyName(self):
        print(f'[{type(self).__name__}] say my name!')

class factoryClass():
    def __init__(self, factoryMethod):
        self.__factoryMethod = factoryMethod
    def callFactoryMethod(self):
        self.__calledFactoryMethod = self.__factoryMethod()
        return self.__calledFactoryMethod
    @property
    def getCalledFactoryMethod(self):
        return self.__calledFactoryMethod

# just input factory method into class
fc1 = factoryClass(A_class)
fc2 = factoryClass(B_class)

# call factory method init via the class
fc1.callFactoryMethod()
fc2.callFactoryMethod()

# call factory method init and factory method func
fc1.callFactoryMethod().sayMyName()
fc2.callFactoryMethod().sayMyName()

# call factory method func via the class
fc1.getCalledFactoryMethod.sayMyName()
fc2.getCalledFactoryMethod.sayMyName()