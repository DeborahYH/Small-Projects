"""
Aim: Convert a sequence of DNA into its protein equivalent
DNA Sequence: must be translated to a sequence of aminoacids where each aminoacid is represented by a unique letter
https://www.ncbi.nlm.nih.gov/nuccore/NM_207618.2: download a DNA strand as a text file
"""

dna_file = open("dna.txt", "r")
dna_text = dna_file.read()
print(dna_text)

# replace(): removes the hidden character "/n" from the original txt file. 

dna_clean = dna_text.replace(" ", "")
dna_sequence = dna_clean.replace("\n", "")
print("Original DNA Sequence:", dna_sequence)

# Transcription: creates an RNA molecule based on a gene's DNA sequence

nucleot_table = str.maketrans({"A":"U", 
                               "T":"A", 
                               "C":"G",
                               "G":"C"})

def transcription(dna):
    rna = dna.upper().translate(nucleot_table)
    print(rna)
    return rna

rna_sequence = transcription(dna_sequence)
print("RNA Sequence:", rna_sequence)

"""
translation(): function is fed the RNA sequence --> RNA sequence is converted into its protein equivalent
codon = triplet nucleotide which forms a single amino acid = RNA sequence must be divisible by 3 
Codons are matched with the aminoacids in the dictionary
Protein: formed by the aminoacid sequence --> returned by the function

Aminoacid Sequence: must be compared to the original one found on the NCBI website --> returns true if both are exactly the same copy
Unaltered aminoacid sequence txt file must be opened in Python
Function read_seq(): removes the unwanted characters and form the altered amino acid’s sequence txt file. 
"""

aminoacids = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
        'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
        'UAU':'Y', 'UAC':'Y', 'UAA':'_', 'UAG':'_',
        'UGU':'C', 'UGC':'C', 'UGA':'_', 'UGG':'W',
        'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',                 
        'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
        'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
        'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
        'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
        'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
        'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
        'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
        'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
        'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
        'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
        'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    }

def translation(rna):

    aminoacid_sequence = []
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    print("Codons:", codons) # lista de strings

    # loops through the aminoacids dictionary --> converts each codon to an aminoacid
    for codon in codons: 
        for key, value in aminoacids.items():
            if key == codon:
                codon = value
                aminoacid_sequence.append(codon)
                protein = ("".join(aminoacid_sequence))
    
    return protein

result = translation(rna_sequence)
print(result)

