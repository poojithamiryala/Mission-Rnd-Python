__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
dict={}
def anagram(s):
    l=list(s.lower())
    l.sort()
    s1=''.join(l)
    if(dict.get(s1)):
        v=dict.get(s1)
        v.append(s)
        dict[s1]=v
    else:
        l=[]
        l.append(s)
        dict[s1]=l
def sort_dict():
    for k in dict:
        v=dict[k]
        v=sorted(v,key=lambda s:s.lower())
        dict[k]=v
    print(dict)
def tuple_dict():
    l=[]
    for k in dict:
        v=dict[k]
        l.append(v)
    #- for descending order of length
    l = sorted(l,key=lambda s:(-s.__len__(),s[0].lower()))
    return l
def anagram_sort(source, destination):
    result = [word.strip() for word in open(source) if(word.strip().startswith('#')==False and word.strip()!='')]
    for i in result:
        anagram(i)
    sort_dict()
    l=tuple_dict()
    with open(destination,"w") as f1:
        # we are walking through f as an iterator, so even if file is huge this code acts like a buffered reader!!
        for line in l:
            for l in line:
                f1.write(l+"\n")


def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
