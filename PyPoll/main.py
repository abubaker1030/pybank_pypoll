import csv

candidates= []
with open("E:/FreeLance/Fiverr/Hinaa11/Project1/PyPoll/Resources/election_data.csv", 'r') as file:
    data = csv.reader(file)
    for row in data:
        candidates.append(row[2])
candidates = [candidate for candidate in candidates[1:]]
total = 0
unique_candidates = {candidates[0]}
for candidate in candidates:
    total = total + 1
    unique_candidates.add(candidate)
unique_candidates_list = list(unique_candidates)
vote_for_each_candidate = [0 for i in range(len(unique_candidates_list))]
print(unique_candidates_list)
for name in candidates:
    index = unique_candidates_list.index(name)
    vote_for_each_candidate[index] = vote_for_each_candidate[index] + 1

print('Election Result')
print('---------------------')
print(f'Total Votes: {total}')
print('---------------------')
for index in range(len(unique_candidates_list)):
    candidateName = unique_candidates_list[index]
    candidateVotes = vote_for_each_candidate[index]
    percentage = round((candidateVotes/total) * 100,3) 
    print(f"{candidateName}: {percentage}% ({candidateVotes})")
print('---------------------')
max_votes = max(vote_for_each_candidate)
max_votes_index = vote_for_each_candidate.index(max_votes)
winner = unique_candidates_list[max_votes_index]
print(f"Winner: {winner}")
print('---------------------')

with open('E:/FreeLance/Fiverr/Hinaa11/Project1/PyPoll/Analysis/election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total) + "\n")
    text.write("---------------------------------------\n")
    for index in range(len(unique_candidates_list)):
        candidateName = unique_candidates_list[index]
        candidateVotes = vote_for_each_candidate[index]
        percentage = round((candidateVotes/total) * 100,3) 
        text.write(f"{candidateName}: {percentage}% ({candidateVotes})\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")