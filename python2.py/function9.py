def notes(*n, situation=False):
    """
    -> Function(n and situation)
    (sit)= is the situation(good,bad and median)
    (n)= is the values 

    """
    dictionary=dict()
    dictionary['full']= len(n)
    dictionary['bigger']= max(n)
    dictionary['small']= min(n)
    dictionary['median']= sum(n)/len(n)
    if situation:
        if dictionary['median']>= 7:
            dictionary['situation']='good'
        elif dictionary['median']>6 and dictionary['median']<7:
            dictionary['situation']='median'
        elif dictionary['median']<6:
            dictionary['situation']='bad'
    return dictionary

answer=notes(5,6,9,2,3, situation=True)
print(answer)
help(notes)