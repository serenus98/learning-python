Nucleotides = ["A","C", "G", "T"]

def validateSeq(dna_seq):
    tempseq = dna_seq.upper()                       #assigns an uppercase version of the dna_seq to tempseq
    for nt in tempseq:                              #checks if all the characters in the string correspond to an element in the list Nucleotides
        if nt not in Nucleotides:
            return False
    return tempseq 


def reverse_complement(seq):
    Reverse = {"A": "T", 
               "C": "G", 
               "G": "C", 
               "T": "A"
            }
    val_seq = validateSeq(seq)
    if val_seq == False:
        print("This is no DNA sequence!")
    else:
        return ''.join([Reverse[nuc] for nuc in val_seq])[::-1]
#loops through DNAStr and switches characters accorgind to dict, 
# [::-1] reverses the resulting string

print(reverse_complement("ATATATA"))