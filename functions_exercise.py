def functionExample(total_value,*args,operator) :
    if operator=='+' :
        return total_value+sum(args)
    else:
        return total_value-sum(args)
print(functionExample(100,10,20,30,operator='-'))