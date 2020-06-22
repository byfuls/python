class classTaste():
    def __init__(self):
        super(classTaste, self).__init__()
        print('[classTaste] init start')
    
    def __enter__(self):
        print('[classTaste] enter start')
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('[classTaste] exit start')

with classTaste() as classTest:
    print('[main] start')