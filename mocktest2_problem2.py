__author__ = 'Kalyan'

max_marks = 25  # encrypt -> 13, decrypt 12

problem_notes = '''
Write encryption and decryption routines according to the given scheme. 

A secret key is used to encrypt a text message in the following manner: 
- key is a string of letters in which each letter represents the right displacement of the source character (a -> 0, z-> 25)
- text -> input text to be sent 

Letters of the input text are mapped to the letters in the key in a round robin manner. For e.g:

For: key = "abcde", text="hi there", the mapping is 
h->a, i -> b, (space is ignored) t ->c, h -> d, e-> e, (go back to starting a here) r -> a, e->b 

now to get the encrypted text, you move h by 0, i by 1, t by 2, h by 3 etc. So you finally get the text "hj vkirf"

The decryption works in the reverse way and returns the original text.

Notes:
- Preserve the casing(lower case remains lower case, Upper case remains Upper case).
- Ignore non-letters and punctuations, i.e., leave them as is in the final result
- For displacement, both small and large letters represent the same displacement. For e.g. b and B both represent 1
- raise TypeError if text and key are not strings.
- raise ValueError if key is empty or has non alphabet characters

Write helper sub routines as required. Make good use of the available datatypes!
'''

# do type checking, non-str should raise TypeException
def encrypt(text, key):
    if(type(text).__name__!='str' or type(key).__name__!="str"):
        raise TypeError("Need to enter strings")
    l=[x for x in list(key) if(not(x.isalpha()))]
    res = []
    if(len(l)==0):
        count=0
        for y in text:
            if(not(y.isalpha())):
                res.append(y)
            else:
                displacement=ord(key[count].lower())-ord('a')
                count+=1
                if(count==len(key)):
                    count=0
                z=displacement+ord(y.lower())-ord('a')
                if(z>25):
                    z-=26
                if(y.isupper()):
                    res.append(chr(z+ord('A')))
                else:
                    res.append(chr(z + ord('a')))
    else:
        raise ValueError("invalid characters in key")
    return ''.join(res)




def decrypt(text, key):
    """if (type(text).__name__ != 'str' or type(key).__name__ != 'str'):
        raise TypeError
    elif (key == None or key.strip() == ''):
        raise ValueError
    else:
        for i in key:
            if (not (i.isalpha())):
                raise ValueError
        l = []
        count = 0
        for i in text:
            if (len(key) > count):
                if (len(key) - 1 == count):
                    l.append(chr(ord(i) - count))
                    count = 0
                elif (i != ' '):
                    l.append(chr(ord(i) - count))
                    count = count + 1
                else:
                    l.append(' ')
        return ''.join(l)"""
    if (type(text).__name__ != 'str' or type(key).__name__ != "str"):
        raise TypeError("Need to enter strings")
    l = [x for x in list(key) if (not (x.isalpha()))]
    res = []
    if (len(l) == 0):
        count = 0
        for y in text:
            if (not (y.isalpha())):
                res.append(y)
            else:
                displacement = ord(key[count].lower()) - ord('a')
                z=0
                if (ord(y.lower())<ord(key[count].lower())):
                    z=26+ord(y.lower())-ord('a')-displacement
                else:
                    z=ord(y.lower())-ord('a')-displacement
                if (y.isupper()):
                    res.append(chr(z + ord('A')))
                else:
                    res.append(chr(z + ord('a')))
                count+=1
                if(count==len(key)):
                    count=0
    else:
        raise ValueError("invalid characters in key")
    return ''.join(res)


def test_encrypt():
    assert "Ec Uvgkwx 10:20 Ovwlskg" == encrypt('My Secret 10:20 Message', 'secret')

def test_decrypt():
    assert "My Secret 10:20 Message" == decrypt("Ec Uvgkwx 10:20 Ovwlskg", "secret")

