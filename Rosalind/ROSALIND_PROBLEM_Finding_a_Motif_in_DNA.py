def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
TESTData = readFile('TESTDATA_Motif.txt')

substring = TESTData[1]
template = TESTData[0]
positionstring = ""
temp = 0

print(substring)
print(template)

while temp >= 0:
    position = template[temp:].find(substring) + 1
    temp += position
    positionstring += str(temp) + ' '
    if template[temp:].find(substring) == -1:
        positionstring = positionstring[:-1]
        break

print(positionstring)


#for letter in substring:   
#for i in range(0, len(template)-len(substring)-1):
    #if template[i] == substring[0]:
        #temp = template[i]
