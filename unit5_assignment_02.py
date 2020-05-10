__author__ = 'Kalyan'

notes = '''
Again while this code passes the tests, this code is wrong as it has been modified for the sake of the tests.

Write a test case that will fail this test. Ignore infinite sequences for now.

Note: if you cannot figure out the yield statement behavior by reading the web documentation, then do this assignment 
after unit6 where we will cover generators.

'''

def generator_zip(seq1, seq2, *more_seqs):
    count = 0
    flag = 1
    final_res = []
    while True:
        res = []
        if (type(seq1).__name__ == 'generator'):
            try:
                tup = next(seq1)
                res.append(tup)
            except:
                flag = 0
                break
        elif (seq1.__len__() > count):
            res.append(seq1[count])
        else:
            break
        if (type(seq2).__name__ == 'generator'):
            try:
                tup = next(seq2)
                res.append(tup)
            except:
                flag = 0
                break
        elif (seq2.__len__() > count):
            res.append(seq2[count])
        else:
            break
        flag = 1
        for i in range(0, len(more_seqs)):
            if (type(more_seqs[i]).__name__ == 'generator'):
                try:
                    tup = next(more_seqs[i])
                    res.append(tup)
                except:
                    flag = 0
                    break
            elif (more_seqs[i].__len__() > count):
                res.append(more_seqs[i][count])
            else:
                flag = 0
                break
        if (flag == 1):
            yield tuple(res)
            count = count + 1
        else:
            break


# add some test inputs that fail with the above code, then fix the above code.
def test_generator_zip_student():
    gen = generator_zip([],"",[1,2])
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 0,0)
    gen = generator_zip([], "")
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 0, 0)

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1, 5), "abc", [1, 2])
    assert [(1, 'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1, 2), "abcd")
    assert [(1, 'a'), (2, 'b')] == list(gen)

    gen = generator_zip("abcd", "abcd", "abcd")
    assert type(gen).__name__ == 'generator'

    assert [('a', 'a', 'a'), ('b', 'b', 'b'), ('c', 'c', 'c'), ('d', 'd', 'd')] == list(gen)

def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert True, "generator did not finish as expected"
    except StopIteration as se:
        pass


# this will run only on our runs and will be skipped on your computers.
# DO NOT EDIT
import pytest
def test_generator_zip_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_generator_zip(generator_zip)
