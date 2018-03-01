def to_rna(dna_strand):
    rna_strand = ''
    dna_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for ch in dna_strand:
        if not dna_rna.get(ch):
            raise ValueError("Invalid DNA strand. Available nucleotides in DNA strand are G, C, T, A.")
        rna_strand += dna_rna.get(ch)
    return rna_strand
