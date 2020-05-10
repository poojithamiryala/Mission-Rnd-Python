__author__ = 'Kalyan'

max_marks = 20

problem_notes = '''
Palindrome is a word which spells the same from both ends.

Create the smallest palindrome from a given word by appending characters to its end.

Examples:
- Malayalam -> Malayalam
- Malayal -> Malayalam (we want smallest palindrome)


Notes:
1. Don't change the letters of the initial word, only add new small letters
2. The palindrome is case-insensitive (ie) Tat is a valid palindrome
3. Only letters are allowed, any other characters should raise a ValueError
4. Non strings should raise a TypeError
5. Empty string is considered as a palindrome.
'''
def check(word,count):
    t=word[count:].lower()
    r=list(t)
    r.reverse()
    str=''.join(r)
    if(str==t):
        return 0
    return 1
def add(count,word):
    res=[x for x in list(word)]
    for i in range(count-1,-1,-1):
        res.append(word[i].lower())
    return ''.join(res)


def smallest_palindrome(word):
    if(type(word).__name__!='str'):
        raise TypeError("should enter strings")
    elif(word==""):
        return ""
    else:
        l=[x for x in list(word) if(not(x.isalpha()))]
        res=""
        if(len(l)==0):
            count=0
            while(check(word,count)):
                count+=1
                if(count==len(word)):
                    res=add(count,word)
            res=add(count,word)
            return res
        else:
            raise ValueError("Should enter valid char")





# write your own tests
def test_smallest_palindrome():
    assert 'RoTator'==(smallest_palindrome("RoTator"))
    assert 'RORaror'==(smallest_palindrome("RORar"))

