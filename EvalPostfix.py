from Stack import stack
s = stack(100)

def evalPostfix(expr):
    for token in expr:
        if token in '+-/*':
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'):
                s.push(val1 + val2)
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '/'):
                s.push(val1 / val2)
            elif (token == '*'):
                s.push(val1 * val2)
        else:
            s.push(float(token))

    return s.peek()
                

if __name__ == "__main__":
    expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
    expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
    print(evalPostfix(expr1))
    print(evalPostfix(expr2))

