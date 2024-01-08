from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "rosalind_splc.txt"

DNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}

def readFile(filePath):
    # reading a file and returning a list of lines
    with open(filePath, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
# converting FASTA/List file data into a dictionary
def readFASTA(FASTAFile):
    FASTADict = {}
    for line in FASTAFile:
        if ">" in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line
    return FASTADict

def translate_seq(seq, init_pos=0):
   result = [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -2, 3)]
   return result

TESTData = readFile(filename_path)
TESTData_dict = readFASTA(TESTData)

full_sequence = ""
#this bit of code goes through all the keys of the dictionary (all the ">XXXXXXXXXX"-style accession numbers)
#it compares the length of the corresponding value (a string with the sequence) and saves the longest one
#in the variable "full_sequence" since the introns must be shorter than the sequence they originate from.
for key in TESTData_dict:
    if len(TESTData_dict[key]) > len(full_sequence):
        full_sequence = TESTData_dict[key]

introns = []
#this bit of code goes through all the keys of the dictionary (all the ">XXXXXXXXXX"-style accession numbers)
#it then checks that it is different from the accession number of the full_sequence and saves the corresponding
#values, the intron sequences in a list named introns
for key in TESTData_dict:
    if key != TESTData[0]:
        introns.append(TESTData_dict[key])

#for every intron sequence in the list of introns this bit of code replaces the identical sequence in the full_sequence with an empty string
#thus deleting it from the string, this works here because we do not have an overlap of intron sequences
for intron in introns:
    full_sequence = full_sequence.replace(intron, "")

#here we join the aminoacids translated from the intronfree full_sequence and leave out the last one, the "_" for the stop codon
print("".join(translate_seq(full_sequence))[:-1])

