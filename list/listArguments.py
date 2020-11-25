

def func(*nets):
    print("----------------------------")
    print(f"arguments: {nets}")
    print(f"arguments type: {type(nets)}")
    print(f"arguments length: {len(nets)}")
    print(f"argument[0] type: {type(nets[0])}")
    print(f"argument[1] type: {type(nets[1])}")
    print(isinstance(nets[0],list))
    print(isinstance(nets[0],tuple))
    print("----------------------------")

argsList = ["TCP", "127.0.0.1", 1000]
argsTuple = ("TCP", "127.0.0.1", 1000)

#func(argsList)
#func(*argsTuple)

argsLists = [["TCP", "127.0.0.1", 1000], ["UDP", "127.0.0.1", 1001]]
argsTuples = (["TCP", "127.0.0.1", 1000], ["UDP", "127.0.0.1", 1001])

func(*argsLists)
func(*argsTuples)
