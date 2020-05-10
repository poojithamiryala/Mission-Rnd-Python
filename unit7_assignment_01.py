__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
import string
#sorting grouped words amd returning a tuple
def sort_dict(dict):
    for k in dict:
        v=dict[k]
        v=sorted(v,key=lambda s:s.lower())
        dict[k]=v
    print(dict)
    l = []
    for k in dict:
        v = dict[k]
        l.append(v)
    # - for descending order of length
    l = sorted(l, key=lambda s: (-s.__len__(), s[0].lower()))
    return l
def write_into_file(destination,l):
    with open(destination,"w") as f1:
        # we are walking through f as an iterator, so even if file is huge this code acts like a buffered reader!!
        for line in l:
            for l in line:
                f1.write(l+"\n")

def group_words(source):
    dict={}
    result = [word.strip() for word in open(source) if (word.strip().startswith('#') == False and word.strip() != '')]
    for s in result:
        l = list(s.lower())
        l.sort()
        s1 = ''.join(l)
        if (dict.get(s1)):
            v = dict.get(s1)
            v.append(s)
            dict[s1] = v
        else:
            l = []
            l.append(s)
            dict[s1] = l
    return dict
if __name__ == "__main__":
    filename=sys.argv[1]
    group = group_words(sys.argv[1])
    result_list=sort_dict(group)
    write_into_file(filename.replace(".txt","")+"-results.txt",result_list)
    #sys.exit(main())