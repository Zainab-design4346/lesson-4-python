math=int(input("Enter marks of math: "))
english=int(input("Enter marks of english: "))
science=int(input("Enter marks of science: "))
physics=int(input("Enter marks of physics: "))

sum=math+english+science+physics
percentage= (sum/400) *100
print("Total:",sum)
print("Percentage:",percentage, end="%")