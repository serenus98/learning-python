from pathlib import Path

working_directory = Path(__file__).absolute().parent
input_file = working_directory / "InputPV5.txt"

outputfile = []

with open(input_file, 'r') as f:
    outputfile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]
    
with open('OutputPV5.txt', 'w') as f:
    f.write(''.join([line for line in outputfile]))

for line in range(0,4):
    print(outputfile[line]) 