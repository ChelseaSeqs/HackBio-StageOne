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
