def get_grade(score):
    grade=''
    if score>=90 and score<=100 :
        grade='A'
    elif score>=80 and score<=89:
        grade='B'
    elif score>=70 and score<=79:
        grade='C'
    elif score>=60 and score<=69:
        grade='D'
    else:
        grade='F'
    return f'Based on your score {score} Grade you have secured is {grade}'
score=int(input('Enter your score '))
print(get_grade(score))    