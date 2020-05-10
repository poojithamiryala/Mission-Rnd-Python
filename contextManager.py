#format_help_text
#Context Manager with statement

class ContextManager:
    def __init__(self,key):
        self.key=key



    def __enter__(self):
        print("Entered")
        return self.key

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit",exc_type,exc_tb)
        return 1#exception is suppressed-such that it doesn't goes to exception class-here 1 tells that function has handled exception

def test_contextmgr():
    with ContextManager("cc") as someobj:
        print(someobj)
        raise ValueError
        print("In the body")


#Decorators,Genertors,Wraps,Partial,Slots
