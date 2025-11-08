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

#######

# Creating a function to calculate the hamming distance between two strings

def calculate_hamming_distance(string1, string2):

    # First create a variable that sets the initial value to 0
    distance = 0

    # Calculate length of both strings
    len1 = len(string1)
    len2 = len(string2)

    # Determine the length to compare (the length of the shorter string)
    min_length = min(len(string1), len(string2))

    # Loop through each position up to the minimum length
    for i in range(min_length):
        # Check if the characters at this position are different 
        # Tally up the differences by taking the current distance and add one
        if string1[i] != string2[i]:
            distance += 1
    
    # Account for length of longer string
    # If we want function to only return length of the shorter string difference then exclude
    length_difference = abs(len1 - len2)
    distance += length_difference

    #Stop function and return final output hamming distance
    return distance



# Testing the function
slack_username = "chelsea751"
twitter_handle = "chelsea_uju_hackbio"

# Calculate distance 
distance = calculate_hamming_distance(slack_username, twitter_handle)
print(f"\nSlack: {slack_username}")
print(f"Twitter: {twitter_handle}")
print(f"Hamming distance (longest) between my slack and twitter usernames: {distance}")
