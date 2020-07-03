class haveInnerClass:
    def __init__(self):
        def innerFunc():
            return print('print inner function')
        self.__func = innerFunc
    
    def call(self):
        self.__func()
        return
        
    
sample = haveInnerClass()
sample.call()
#sample.__func()