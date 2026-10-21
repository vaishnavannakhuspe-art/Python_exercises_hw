# write a program to findout which player has scored maximum and minimum run from data stored in dictionary using for loop
cricket_scores = {
    "Rohit Sharma": 78,
    "Shubman Gill": 34,
    "Virat Kohli": 96,
    "Shreyas Iyer": 45,
    "KL Rahul": 62,
    "Hardik Pandya": 29,
    "Ravindra Jadeja": 51,
    "Kuldeep Yadav": 12,
    "Jasprit Bumrah": 7,
    "Mohammed Shami": 18,
    "Mohammed Siraj": 4
}
runs = cricket_scores.values()

max_runs = max(runs)
min_runs = min(runs)
print(max_runs)
print(min_runs)
for player in cricket_scores:
    if cricket_scores[player] == max_runs:
        print("Player who scor maximun runs is ",player)
    else:
        if cricket_scores[player] == min_runs:
            print("Player who scored minimum runs is ",player)
        




