import itertools

# Custom Password word list
user_list = ['apple', 'banana', 'cherry', '123', 'password', '!@#']

# A function for generating all possible combinations of words
def generate_passwords(words):
    # Generating word combinations
    combinations = []
    for r in range(1, len(words) + 1):
        for combination in itertools.combinations(words, r):
            combinations.append(combination)
    
    # Generating permutations for each combination
    passwords = []
    for combination in combinations:
        for p in itertools.permutations(combination):
            passwords.append(''.join(p))
    
    return passwords

# Generating all possible passwords
passwords = generate_passwords(user_list)

# Saving passwords to a file
with open('passwords.txt', 'w') as file:
    for password in passwords:
        file.write(password + '\n')

print("Passwords are saved to a file 'passwords.txt'")