
def to_rna(dna_strand):
    dna_strand = list(map(str, dna_strand))
    rna = []
    dna_dict= {"G": "C", "C": "G", "T": "A", "A": "U"}
    for i in range(len(dna_strand)):
        rna.append(dna_dict[dna_strand[i]])

    return ("".join(rna))

