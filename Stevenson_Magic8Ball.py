import random

filename = "8_ball_responses.txt"
f=open(filename)#open file for readinf
responses=f.readlines()#read all the lines into a list, with newline character at end of each line
f.close()
ques=input("Enter your yes/no question or q to exit: ")
while ques!='quit':
    #random.randrange(0,len(responses)) will randomly generate an index from 0 to length of responses-1
    print(responses[random.randrange(0,len(responses))].strip())#use strip to remove newline character
    ques=input("Enter your yes/no question or quit to exit: ")