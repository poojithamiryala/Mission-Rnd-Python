__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''


def unjumble(jumbled_text, n):
    if(type(jumbled_text).__name__!='str'):
        raise TypeError
    if(n<=0):
        raise ValueError
    if (jumbled_text == "" or (jumbled_text.strip() == "")):
        return jumbled_text
    dict=[]
    count=0
    step = n
    low = 0
    dec = -1
    count = 0
    while (len(jumbled_text) >= count):
        dict.append((step,[]))
        count += step
        low = low + step
        step = step + dec
        if (step == 0):
            step = 1
            dec = -dec
        elif (step == n + 1):
            step = n
            dec = -dec
    low=0
    for i in range(1,n+1):
        for j,k in dict:
            if(i==j):
                k.extend(jumbled_text[low:low+i])
                low=low+i
    res=[]
    for j,k in dict:
        res.extend(k)
    return ''.join(res)





def test_unjumble():
    assert "Ashokan" == unjumble("hoAskan", 2)