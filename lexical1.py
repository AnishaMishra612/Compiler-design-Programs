import re
sentence = input(" ")
tokens=[]
single = sentence.split()
print(single)
for each in single:
    if each in ['int','string','char','bool','float','double']:
        tokens.append(["Datatype",each])
    elif re.match("[A-Z]",each) or re.match("[a-z]",each):
        if each in ["return","print","if","else","else if"]:
            tokens.append(["keyword",each])
        else:
            tokens.append(["IDENTIFIER",each])
    elif each in '.+-/=%*><':
        tokens.append(["Operator",each])

    elif re.match("[0-9]",each):
        tokens.append(["INTEGER",each])
    elif each==';':
        tokens.append(["STATEMENT SEPARATOR",each])

print(tokens)
