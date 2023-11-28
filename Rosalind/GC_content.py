from pathlib import Path

working_directory = Path(__file__).absolute().parent
input_file = working_directory / "rosalind_gc(1).txt"

def read_FASTA(filePath):
    with open(filePath, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    FASTADict = {}
    FASTALabel = ""

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line

    return FASTADict

def gc_content(seq):
    return round((seq.count("C") + seq.count("G"))/len(seq)*100,7)


Fasta_dict = read_FASTA(input_file)
temp = 0
for label in Fasta_dict:
    Fasta_dict[label] = gc_content(Fasta_dict[label])
for label in Fasta_dict:
    if Fasta_dict[label] > temp:
        temp = Fasta_dict[label]
        temp_label = label
        print(temp)
    print(Fasta_dict)
    print(f"{temp_label[1:-1]}\n{temp}")