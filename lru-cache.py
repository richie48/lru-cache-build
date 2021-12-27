
def func(x):
    res=[]
    for i in range(len(x)):
        if i in x:
            continue
        else:
            res.append(i)
    print(res)

func([1,3,4])