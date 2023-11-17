def countNucFreq(seq):
    tempFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nt in seq:
        tempFreqDict[nt] += 1
    return tempFreqDict

print(countNucFreq(seq="ATTGTATAGCCGATCGAT"))