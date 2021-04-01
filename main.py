score = float(input("What is your score? "))
while score > 10 or score < 0:
  score = float(input("What is your score? "))
if score >= 9 and score <= 10:
  print("A+")
elif score >= 8.5 and score < 9:
  print("A")
elif score >= 7.8 and score < 8.5:
  print("B+")
elif score >= 7 and score < 7.8:
  print("B")
elif score >= 6.5 and score < 7:
  print("C+")
elif score >= 6 and score < 6.5:
  print("C")
elif score >= 5.5 and score < 6:
  print("D+")
elif score >= 5 and score < 5.5:
  print("D")
else:
  print("F")
