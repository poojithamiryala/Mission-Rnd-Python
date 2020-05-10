__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    if(sentence!=None and sentence.find(" either ")>0 and sentence.find(" or ")>0 and sentence.find(" either or ")<0 and sentence.count(" ") and sentence.find(" either ")<sentence.find(" or ")):
        sentence=sentence.replace(" either "," ")
        index_or=sentence.find("or")
        s=sentence.replace(sentence[sentence.find(" or "):-1], "")
        if(s[-1].isalnum()):
            return s[:-1]
        else:
            return s
    else:
        return sentence

def test_prune_either_or_student():
    assert "it either or way"==prune_either_or("it either or way")
    assert "we could eitheron go orto a movie nor a hotel -> we could go to a movie." == prune_either_or("we could eitheron go orto a movie nor a hotel -> we could go to a movie.")

# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
