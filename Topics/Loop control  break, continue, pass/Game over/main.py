scores = input().split()
i = 0
inc_count = 0
cor_count = 0
while i < len(scores):
    if inc_count == 3:
        print("Game over")
        print(cor_count)
        break
    if scores[i] == "C":
        cor_count += 1
    else:
        inc_count += 1
    i += 1
else:    
    print("You won")
    print(cor_count)
