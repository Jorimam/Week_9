print("Enter score\n")
score = float(input())

if score >= 70 and score <= 100:
    print("A")
elif score >= 50 and score < 70:
    print("B")        
elif score >= 40 and score < 50:
    print("C")
elif score >= 30 and score < 40:
    print("D")
elif score >= 0 and score < 30:
    print("F")
else:
    print("Invalid score")
   
