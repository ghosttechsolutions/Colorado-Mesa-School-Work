import random
import secrets
import string
print("Please enter your full name")
print("First Name:")
firstName = input()
print("Last Name:")
lastName = input()
firstThreeDigits = '007'
fourthDigit = random.randrange(0,9)
fifthDigit = random.randrange(0,9)
sixDigit = random.randrange(0,9)
sevenDigit = random.randrange(0,9)
eightDigit = random.randrange(0,9)
nineDigit = random.randrange(0,9)
studentId = int(str(firstThreeDigits) + str(fourthDigit) + str(fifthDigit) + str(sixDigit) + str(sevenDigit) + str(eightDigit) + str(nineDigit))
if len(firstName) > 3 and len(lastName) > 3:
    username = firstName + lastName

if len(lastName) == 2 and len(firstName) == 6:
    username = firstName[0:4] + lastName[0:2]

if len(lastName) == 6 and len(firstName) == 2:
    username = firstName[0:2] + lastName[0:4]

if len(firstName) == 2 and len(lastName) == 2:
    username = firstName + lastName + str(studentId[5:9])

print("Student ID:" + str(studentId))
print("Username:" + username)

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
passCodeLength = 12

while True:
    tempPassCode = ''
    for i in range(passCodeLength):
        tempPassCode += ''.join(secrets.choice(alphabet))

    if(any(char in special_chars for char in tempPassCode) and sum(char in digits for char in tempPassCode)>= 2):
        break
print("Temporary Passcode:" + tempPassCode)