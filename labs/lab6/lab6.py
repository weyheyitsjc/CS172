import sys
#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list
class Stack:
    #Create a New Empty Stack
    def __init__(self):
        self.__S = []
    #Display the Stack
    def __str__(self):
        return str(self.__S)
    #Add a new element to top of stack
    def push(self,x):
        self.__S.append(x)
    #Remove the top element from stack
    def pop(self):
        return self.__S.pop()
    #See what element is on top of stack
    #Leaves stack unchanged
    def top(self):
        return self.__S[-1]
    
def postfix(exp):
    exp = exp.split()
    stack = Stack()
    for n in exp:
        if n == "+":
            x = int(stack.pop())
            y = int(stack.pop())
            result = x + y
            stack.push(result)
        elif n == "-":
            x = int(stack.pop())
            y = int(stack.pop())
            result = y - x
            stack.push(result)
        elif n == "*":
            x = int(stack.pop())
            y = int(stack.pop())
            result = x * y
            stack.push(result)
        elif n == "/":
            x = int(stack.pop())
            y = int(stack.pop())
            result = y / x
            stack.push(result)
        elif n == " ":
            continue
        else:
            stack.push(n)
    return result
   
if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit.")

    exp = input("Enter Expression:\n")

    while exp.lower() != "exit":
        answer = postfix(exp)
        if isinstance(answer, int) == True:
            print("Result: %.1f" % (answer))
        else:
            print("Result:", answer)
        exp = input("Enter Expression:\n")

    sys.exit()

