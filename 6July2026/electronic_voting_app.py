import random
"""
Candidates:
    - Ali
    - Ahmed
    - Sara
    - Fatima

Requirements:
    - Allow 20 people to vote
    - After 20 votes, Display the Winner with total number of votes
    - In case of tie, Display all with the same number of votes
"""
candidates = ["Ali", "Ahmed", "Faizan", "Sara", "Fatima"]

# Crate a dict with 0 votes for each candidate
votes = {}
for candidate in candidates:
    votes[candidate] = 0
print(votes)

# Voting Manually
"""
num_of_votes = 20
for i in range(num_of_votes):
    user_input_candidate = input("Enter candidate name: ")
    votes[user_input_candidate] += 1
print(votes)
"""

# Voting Randomly using Index
"""
num_of_votes = 20
for i in range(num_of_votes):
    random_index = random.randint(0,len(candidates)-1)
    candidate_name = candidates[random_index]
    votes[candidate_name] += 1
print(votes)
"""

# Voting Randomly using random.choice
num_of_votes = 20
for i in range(num_of_votes):
    candidate_name = random.choice(candidates)
    # print(candidate_name)
    votes[candidate_name] += 1
print(votes)



