def calc():
    exp = input()
    try:
        print(eval(exp))
    except:
        print("Can't evaluate this expression.")
