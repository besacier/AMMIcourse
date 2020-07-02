

f = open("./Session38.txt", "r")
lines = f.readlines()
result=open("Session38.txt", "w")

for line in lines:
    line = '##'+ line
    result.write(line)
result.close()
