from pathlib import Path

working_directory = Path(__file__).absolute().parent
filename_path = working_directory / "rosalind_grph.txt"

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

lines_list = readFile(filename_path)
fasta_records = readFASTA(lines_list)

k = 3
prefix_dict = {}
edges = []
prefix_list = []

for key in fasta_records:
    uffix = fasta_records[key]
    prefix_dict[key] = uffix[0:k]
    prefix_list.append([uffix[0:k], key])
    for identifier in fasta_records:
        if key != identifier:
            if fasta_records[identifier].endswith(prefix_dict[key]):
                edges.append([key, identifier])

for edge in edges:
    print(edge[1][1:], edge[0][1:])


