__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Given a string of digits, you must return a list of all (substring, count) in the input string such that count >=2 and 
len(substring) >= 2. count represents the number of times the substring repeats in the input string (non-overlapping 
occurances).

The result must be sorted by count first (descending) and then in case of a tie the numerical value of 
substring (descending)

For e.g. if input is "123451236786712" you must return [("12", 3), ("123", 2), ("67", 2), ("23", 2)]

Notes:
1. if input is not a str, raise TypeError
2. Write clean bruteforce code to do this using python features. Do not devise new algorithms in the exam!
3. Write your own test cases 
'''

def repeats(digits):
    if(type(digits).__name__!="str"):
        raise TypeError
    substring_len=2
    res=[]
    while(substring_len<=(len(digits))):
        for i in range(0,len(digits)-substring_len+1):
            str=digits[i:i+substring_len]
            count=digits.count(str)
            if(count>=2):
                res.append((str,count))
        substring_len+=1
    res=list(set(res))
    res.sort(key=lambda x:(-x[1],-int(x[0])))
    return res



def test_repeats():
    assert [("12", 3), ("123", 2), ("67", 2), ("23",2)] == repeats("123451236786712")