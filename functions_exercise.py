def basic_calculator(total_value,*args,operator) :
    if operator=='+' :
        return total_value+sum(args)
    elif operator=='-':
        return total_value-sum(args)
    else :
        return 'invalid input'
print(basic_calculator(100,10,20,30,operator='-'))