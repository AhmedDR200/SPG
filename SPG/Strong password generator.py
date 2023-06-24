import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


char_number = input("how many characters for thr password? : ")


while True:
    try:
        char_number = int(char_number)
        if char_number < 6 :
            print("You need at least 6 char")
            char_number = input("Please enter number again : ")
        else:
            break

    except:
      print("Please enter numbers only")
      char_number = input("Please enter number again : ") 



#   shuffle all lists

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#راوند بتقرب الرقم بحيث يبقى رقم صحيح

part1 = round(char_number * (30/100))  
part2 = round(char_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])


for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

print(password)