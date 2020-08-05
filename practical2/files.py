#Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
name = input(str("Enter your name "))
f = open("name.txt","w")
f.write(name)
f.close()

#Write code that opens "name.txt" and reads the name (as above) then prints,"Your name is Bob" (or whatever the name is in the file).
f = open("name.txt", "r")
name = f.read()
print('Your name is:', name)
f.close()

#Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it:
f = open("numbers.txt", "r")
number_1 = int(f.readline())
number_2 = int(f.readline())
sum = number_1 + number_2
print('The sum of two numbers is:', sum)

f.close()

#Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

file = open("numbers.txt","r")
total = 0
for line in file :
    number = int(line)
    total = total + number
f.close()
print(total)
