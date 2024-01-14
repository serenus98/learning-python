from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "TESTDATA_Consensus_and_Profile.txt"

# read data from the FASTA file
def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
def gc_content(seq):
    return round((seq.count("C") + seq.count("G"))/len(seq)*100, 6)   

# storing file contents in a list
FASTAFile = readFile(filename_path)
#print(FASTAFile)

# dictionary for labels + data
FASTADict = {}

# String for hodling the current label
FASTALabel = ""

#print(FASTAFile)

# converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if ">" in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

#print(FASTADict)

ntDict = {"A": 0, "C": 0, "G": 0, "T": 0}
ntList = []
ntListA = []
ntListC = []
ntListG = []
ntListT = []
ntString = ""
for i in range(0, len(FASTADict[FASTALabel])):
    for key in FASTADict:
        sequence = FASTADict[key]
        ntString += sequence[i]
    ntList.append(ntString)
    ntString = ""

'''
for i in range(0, len(ntList)-1):
    seq = ntList[i]
    for letter in seq:
        if letter in ntDict:
            ntDict[letter] += 1
            tempDict = ntDict
        print(tempDict)
    ntDict = {"A": 0, "C": 0, "G": 0, "T": 0}
'''
#print(ntList)
for i in range(0, len(ntList)):
    ntDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for j in range(0, len(ntList[0])):
        #print(j)
        if ntList[i][j] in ntDict:
            ntDict[ntList[i][j]] += 1
            tempDict = ntDict
    #print(tempDict)
    ntListA.append(ntDict["A"])
    ntListC.append(ntDict["C"])
    ntListG.append(ntDict["G"])
    ntListT.append(ntDict["T"])
maxList = [] 
consensus = ""
tmp = "NONE"
for i in range(len(ntListT)):
    maxList.append(ntListA[i])
    maxList.append(ntListC[i])
    maxList.append(ntListG[i])
    maxList.append(ntListT[i])
    tep = max(maxList)
    temp = maxList.index(tep)
    #print(maxList, temp)
    if temp == 0:
        consensus += "A"
    if temp == 1:
        consensus+= "C"
    if temp == 2:
        consensus+= "G"
    if temp == 3:
        consensus += "T"
    maxList = []
        
print(consensus)
As = ' '.join(map(str, ntListA))
print("A: ", As)
Cs = ' '.join(map(str, ntListC))
print("C: ", Cs)
Gs = ' '.join(map(str, ntListG))
print("G: ", Gs)
Ts = ' '.join(map(str, ntListT))
print("T: ", Ts)
# using a dictionary comprehension to generate a new dictionary with GC content
#RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

#print(RESULTDict)

# looking for max value in values() of our new dictionary
#MaxGCKey = max(RESULTDict, key=RESULTDict.get)

# printing Rosalind formatted result
#print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')