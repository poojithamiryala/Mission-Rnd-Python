max_marks = 20

problem_notes = '''
Given a sentence in which words are separated by spaces.

Re-arrange it so that words are reordered according to the following criteria.
 - longer words come before shorter words
 - if two words have same length, the one with smaller vowel occurance count comes first (feeel counts as 3 vowel occurances)
 - if even that is same, then order them lexicographically (case insensitive). For e.g. a comes before b

Constraints:
- Only allowed characters are a-zA-Z in the words
- raise a ValueError if the sentence contains any characters beyond the above
- raise a TypeError if input is not a string
- The result should preserve the words as is without changing case etc. but the sentence should be sorted so that
longer words precede shorter words. In case of tie, the word with fewer vowels comes first, if there is a tie even there,
preserve the original order.
- If there are multiple spaces, merge them into a single space in the result.
- If there is any leading or trailing space, remove it from the result.


Note: 
1. use the features of python to solve this problem, DON'T WRITE YOUR OWN SORT ROUTINE!
2. You can write additional routines as you see fit.
'''
def transform(sentence):
    if(type(sentence).__name__!="str"):
        raise TypeError("invalid type..")
    length=[x for x in sentence if(not(x.isalpha()) and x!=' ')]
    if(len(length)==0):
        s=sentence.strip(' ')
        res = [y.strip() for y in s.split(' ') if (y.strip())]
        l=sorted(res,key=lambda x:(-len(x),sum([x.count(y) for y in set("aeiou")]),x.lower()))
        return ' '.join(l)
    else:
        raise ValueError("invalid characters in sentence")




def test_transform():
    assert "Elephant fast runs the" == transform(' fast   runs   the  Elephant ')