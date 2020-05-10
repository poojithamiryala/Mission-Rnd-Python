from contextlib import contextmanager

@contextmanager
def contxtmgr():
    print("enterd cntcmgr")
    try:
        yield 10
        pass
    finally:
        print("exit called")
        raise StopIteration("from method")

def contextFile():
    with contxtmgr() as val:
        print('Entered definitation',val)

def m_gen():
    yield 10
    yield(20)

if __name__== '__main__':
    gen=m_gen()
    with contxtmgr()as gen:
        print('Entered definitation',gen)
        raise StopIteration("from method")