# WAP read scores of n players and display

scores = []

n = int(input("Enter How many players : "))  # eg.3

for i in range(1, n+1):  # star 0, stop 2, -1, step 1
    stores = int(input(f'Enter Player {i} Score : '))
    scores.append(stores)

print(f'\nPlayers Scores : {scores}')
print(f'Maximum Scores : {max(scores)}')
print(f'Minimum Scores : {min(scores)}')
print(f'Total Scores   : {sum(scores)}')