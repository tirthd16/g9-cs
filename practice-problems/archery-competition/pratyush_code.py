Maxcompetitor=30
rounds=10
Maxscore=30
#input the competitor names
names=[]
scores=[]
Qualified = 0
Reserved = 0
Not_Qualified = 0
for i in range(Maxcompetitor):
    name = str(input(f"\nEnter competitor name {i+1}: "))
    names.append(name)

    #input the scores for each competitor
for i in range(Maxcompetitor):
    print(f"\nEnter scores for competitor {names[i]}:")
    scores_for_competitor = []
    for j in range(rounds):
        score = int(input(f"Score for round {j+1}: "))
        while score < 0 or score > Maxscore:
            print(f"Invalid score. Please enter a score between 0 and {Maxscore}.")
            score = int(input(f"Score for round {j+1}: "))
        scores_for_competitor.append(score)
    scores.append(scores_for_competitor)


#calculting the scores and determining the status of each competitor
for i in range(Maxcompetitor):
    total_score = sum(scores[i])
    max_score = max(scores[i])
    min_score = min(scores[i])
    #discarding the highest and lowest scores
    total_score = total_score - max_score - min_score
    if total_score >= 210:
        Qualified += 1
        status = "Qualified"
    elif total_score >= 180:
        Reserved += 1
        status = "Reserved"
    else:
        Not_Qualified += 1
        status = "Not Qualified"
    print(f"\nCompetitor: {names[i]}")
    print(f"Total Score: {total_score}")
    print(f"Status: {status}")

print("Qualified:",Qualified)
print("Reserved:",Reserved)
print("Not_Qualified:",Not_Qualified)
        
