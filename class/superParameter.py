import sys

if __name__ == '__main__':
    if sys.argv[1] == 'init':
        class topClass():
            def __init__(self):
                print('[topClass] init start')

        class mid1Class(topClass):
            def __init__(self):
                print('[mid1Class] init start')
                topClass.__init__(self)

        class mid2Class(topClass):
            def __init__(self):
                print('[mid2Class] init start')
                topClass.__init__(self)

        class bottomClass(mid1Class, mid2Class):
            def __init__(self):
                print('[bottomClass] init start')
                mid1Class.__init__(self)
                mid2Class.__init__(self)

        bt = bottomClass()
    elif sys.argv[1] == 'super':
        class topClass():
            def __init__(self):
                print('[topClass] init start')
        
        class mid1Class(topClass):
            def __init__(self):
                print('[mid1Class] init start')
                super().__init__()
        
        class mid2Class(topClass):
            def __init__(self):
                print('[mid2Class] init start')
                super().__init__()
        
        class bottomClass(mid1Class, mid2Class):
            def __init__(self):
                print('[bottomClass] init start')
                super().__init__()

        bt = bottomClass()
    elif sys.argv[1] == 'super-init':
        class topClass():
            def __init__(self):
                print('[topClass] init start')
                super(topClass, self).__init__()
        
        class mid1Class(topClass):
            def __init__(self):
                print('[mid1Class] init start')
                super(mid1Class, self).__init__()
        
        class mid2Class(topClass):
            def __init__(self):
                print('[mid2Class] init start')
                super(mid2Class, self).__init__()
        
        class bottomClass(mid1Class, mid2Class):
            def __init__(self):
                print('[bottomClass] init start')
                super(bottomClass, self).__init__()

        bt = bottomClass()
    else:
        print('[main] check parameter again')
