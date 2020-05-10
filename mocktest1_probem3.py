__author__ = 'Kalyan'

max_marks = 35 # 15 marks for encode and 20 for decode

problem_notes ='''
 This problem deals with number conversion into a custom base 5 notation and back.
 In this notation, the vowels a e i o u are used for digits 0 to 4.

 E.g. decimal 10 in this custom base 5 notation is "ia", decimal 5 is "ea" etc.

 Your job is to write encoding and decoding (both) routines to deal with this notation.
'''

# Notes:
# - If number is not a valid int raise TypeError
# - Negative numbers should result in a - prefix to the result similar to how bin works
#  use lower case letters in your result [aeiou].
def to_custom_base5(number):
    s="aeiou"
    if(type(number).__name__!='int'):
        raise TypeError
    temp=number
    if(temp<0):
        temp=-temp
    res=[]
    if(temp==0):
        return 'a'
    while(temp):
        res.append(s[temp%5])
        temp=temp//5
    if(number<0):
        res.append('-')
    res.reverse()

    return ''.join(res)



# Notes:
# - if s is not a string, raise TypeError
# - if the encoding is not right or empty string, raise ValueError
# - allow both - and + as prefixes which represent sign.
# - allow trailing and starting spaces (but not once the sign or number starts)
# - allow both capital and small letters.
# - return a int that corresponds to the number.
def from_custom_base5(s):
    w="aeiou"
    if(type(s).__name__!="str"):
        raise TypeError
    if(s=="" or s==None):
        raise ValueError
    s=s.strip()
    res=s
    first=""
    if(s[0]=="+" or s[0]=='-'):
        first=s[0]
        res=s[1:]
    l=[x for x in res if(x not in set("aeiou"))]
    if(len(l)==0):
        t=[str(w.find(x.lower())) for x in res]
        y=int(''.join(t),base=5)
        if(first=="-"):
            y=y*-1
        return  y
    else:
        raise  ValueError






# a basic test is given, write your own tests based on constraints.
def test_to_custom_base5():
    assert "-eoaae" == to_custom_base5(-1001)

# a basic test is given, write your own tests based on constraints.
def test_from_custom_base5():
    assert -1101 == from_custom_base5(" Eohuae ")