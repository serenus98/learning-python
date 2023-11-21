DNA_seq = "GATATATGCATATACTT"
motif = "ATAT"
matches = []

for i in range(0, len(DNA_seq)-len(motif)-1):
    if DNA_seq[i:i+len(motif)] == motif:
        matches.append(str(i+1))
print(' '.join(matches))
