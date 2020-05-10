__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
For this problem you have to implement a generator which returns all k digit 
numbers whose sum of digits is n. 

Note that you must not generate the entire solution set at one go (ie) the 
result should be generated on demand (when next is called on generator). This means that 
I can call it with large values of n and k like 1000 and 500 and still 
its use of memory must be modest.

Notes:
1. raise TypeError if n and k are not ints.  
2. if n or k are not positive, raise ValueError 
3. the result numbers must be yield'ed in increasing order. 
4. you are free (encouraged :-) ) to define additional sub-routines as you see fit as long as you do not   
   violate the generator semantics given above

Examples:
 for n = 2 and k = 2, the generator must yield 11, 20 in that order
 for n = 4 and k = 2, the generator must yield 13, 22,31,40 in that order
 
Note that numbers starting with 0 are not valid For e.g. 02 is not a valid 2 digit number
'''
def sum_digit(n):
    res=0
    r=n
    while(n>0):
        res=res+(n%10)
        n=n//10
    return res
def first_no(n,k):
    list_n=list(str(k))
    sum=n-int(list_n[0])
    if(sum<0):
        raise StopIteration
    for i in range(len(list_n)-1,0,-1):
        if(sum==0):
            break
        elif(sum<9):
            list_n[i]=str(sum)
            sum=0
        elif(sum>9):
            list_n[i]=str(9)
            sum-=9
    return ''.join(list_n)
def next_no(n,k):
    list_n=list(str(k))
    sum=n-1
    index=0
    for i in range(len(list_n)-1,0,-1):
        if(list_n[i]!='9'):
            index=i
            break
    y=int(''.join(list_n[:index+1]))
    y=y+9
    list_n[:index+1]=list(str(y))
    return ''.join(list_n)
#Implement this generator.
def kdigitnums(n, k):
    """
    This is a generator returns all k digit numbers whose sum is n. The numbers are yielded in
    increasing order
    """
    if(type(n).__name__!='int' or type(k).__name__!='int'):
        raise TypeError("Enter integer values")
    if(n<=0 or k<=0):
        raise ValueError("Enter crct values")
    start=10**(k-1)
    add=start
    first=int(first_no(n,start))
    if (sum_digit(first) == n):
        yield first
    else:
        raise StopIteration
    while(True):
        p=int(next_no(n,first))
        if(sum_digit(p)==n and len(str(p))==k):
            yield p
            first=p
        else:
            if(k>2):
                start=start+add
                first=int(first_no(n,start))
                if(sum_digit(first)==n):
                    yield first
                else:
                    raise StopIteration
            else:
                raise StopIteration


# write more tests
def test_kdigitnums():
    l=kdigitnums(50,30)
    print(list(l))
