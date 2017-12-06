
class Stack:
    def __init__(self):
        self.data=[]
    def push(self,x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()


def _print(x):
    print x

words={
    '+':lambda x,y:[x+y],
    'dup':lambda x:[x,x],
    'drop':lambda x:[],
    'swap':lambda x,y:[y,x],
    'print': _print,
    }


def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True

def num_args(f):
    """retur nthe number of args that ufunction <f>"""
    return f.func_code.co_argcount

class Interpreter:
    def __init__(self):
        self.stack=Stack()

    def process(self,word):
        if is_int(word):
            n=int(word)
            self.stack.push(n)
        else:
            try:
                f=words[word]
            except KeyError:
                raise SyntaxError,"Unknown  word:%s " % word

            #determine number of args
            num=num_args(f)

            #pop that num of args from stack
            args=reversed([self.stack.pop() for i in range(num)])
            #call f with list
            result=f(*args)

            #push result on stack
            for x in result or []:
                self.stack.push(x)

    def process_line(self,line):
            words=line.split()
            for word in words:
                self.process(word)

    
            
            


if __name__=="__main__":
    e=Interpreter()
    while 1:
        line=raw_input(">")
        e.process_line(line)
        print "stack:",e.stack.data

        
