#Creating a function that translates DNA codons (input) to their single letter amino acide code (output)

def dna_to_protein(dna_sequence):

    # Incoperating dictionary for the translation process
    # Stop codons are "_"
    codon_table = {
        "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
        "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
        "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
        "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
        "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
        "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
        "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
        "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
        "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
        "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
        "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
        "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
        "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
        "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
        "TAC":"Y", "TAT":"Y", "TAA":"_", 
        "TGC":"C", "TGT":"C", "TGA":"_", 
        "TGG":"W", "TGC":"C", "TAG":"_"  
    }
    # Creating an empty string variable to store the final result
    protein = ""
   
    # Loop through the sequence, 3 letters at a time using range function
    # range arguement = range(start (first codon), stop(last codon), step (skip 3))
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]

        # Tell function to look up the amino acid
        # Capitalise input just incase some are lower case
        amino_acid = codon_table.get(codon.upper(), "X") 
        
        # Stop if a stop codon is found
        if amino_acid == "_":
            break
        
        # Building the protein sequence/string by adding the amino acid codes one by one
        # += shorthand for: protein = protein + amino_acid
        protein += amino_acid

    # End function and return result
    return protein


# Tesing the function
my_dna = "ATGGCCGCTATTGGGAGTAG"
my_protein = dna_to_protein(my_dna)
print(f"DNA: {my_dna}")
print(f"Protein: {my_protein}")


# Output was:
# DNA: ATGGCCGCTATTGGGAGTGA
# Protein: MAAIGS
