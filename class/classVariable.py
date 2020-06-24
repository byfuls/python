class classVariable:
    go = True
    pi = 3.14
    def update(self):
        classVariable.pi = 5

cv = classVariable()
print(cv)
print(cv.go)
print(cv.pi)

cv.update()
print(cv)
print(cv.go)
print(cv.pi)

new_cv = classVariable()
print(new_cv)
print(new_cv.go)
print(new_cv.pi)