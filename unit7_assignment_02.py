__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
def find_firstvowel(word):
    i=0
    while(word[i]!='\0'):
        if(word[i] in set("aeiou")):
            return i
        else:
            i+=1
    else:
        return i
def proper_case(word,res):
    res1=""
    for i in range(len(word)):
        if(word[i].isalpha()):
            if(word[i].isupper()):
                res1=res1+res[i].upper()
            else:
                res1=res1+res[i].lower()
        else:
            res1=res1+res[i]
    return res1


def split_words(sentence):
    list_words=sentence.split()
    result=""
    for i in range(0,len(list_words)):
        word=list_words[i]
        last_letter=''
        if(list_words[i][-1]=='.' or list_words[i][-1]==','):
            last_letter=list_words[i][-1]
            word=word[:-1]
        index=find_firstvowel(word)
        res=""
        if(index==len(list_words) or index==0):
            res=res+word
        else:
            res=word[index:]+word[:index]
            res=proper_case(word,res)
        result=result+res+"ay"+last_letter+" "
    return result
if __name__ == "__main__":
    sentence=sys.argv[1]
    result=split_words("There is, however, no need for fear.")
    print(result)
    #sys.exit(main())