fname = "steps.txt"
try:
    fhand = open(fname)
except:
    print("can't open the steps.txt file!!: " + fname)
    exit()
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
day = 0
daySteps = 0
monthlySteps = 0
print("\nAverage steps : \n")
for line in fhand:
    if(line[-1] == "\n"):
        line = line[:-1]
    daySteps = int(line)
    day +=1
    monthlySteps += daySteps
    if days[0] == day:
        print(months[0],":", round(monthlySteps/days[0], 0))
        day = 0
        monthlySteps = 0
        days = days[1:]
        months = months[1:]