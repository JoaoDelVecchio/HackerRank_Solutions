def undo(stack):
    if stack:
        return stack.pop()
    return ""

Q = int(input())
vetorComandos = []
s = ""
stack = []

for i in range(Q):
    x = input()
    comando = int(x[0])
    argumento = x[2:]
    
    if comando == 1:
        stack.append(s)
        s = s + argumento
    elif comando == 2:
        u = len(s) - int(argumento)
        stack.append(s)
        s = s[:u]
    elif comando == 3:
        print(s[int(argumento) - 1])
    elif comando == 4:
        s = undo(stack)