
def sum_or_product(*args,**opp):
    s = 0
    p = 1
    if opp["op"] == '+':
        for i in args:
            s += i
        return s
    elif opp["op"] == '*':
        for i in args:
            p *= i
        return p
    else: 
        print("Error: Operation not supported: ", opp["op"])    
s = sum_or_product(1,2,3,4,5,op = '+')
p = sum_or_product(1,2,3,4,5,op = '*')
print ("Sum: {0}, Product: {1}".format(s,p))