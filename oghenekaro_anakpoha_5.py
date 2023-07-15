 
#a. Print the string to the page 
str = "The quick brown fox jumps over the lazy dog" 
print(str)

#b. Print the length of the string to the page 
print(len(str))  

 
#c. Print the string in all uppercase letters 
up_txt = str.upper() 
print(up_txt)

 
#d. Print the string in all lowercase letters 
small_txt = str.lower() 
print(small_txt) 

 
#e. Print the string in the title case 
tit_txt = str.title() 
print(tit_txt)

 

#f. Print the string in reverse 
str = "The quick brown fox jumps over the lazy dog"[::-1] 
print(str) 

 
#g. Print the string in reverse title case 
str = "The quick brown fox jumps over the lazy dog" 
title_case_string = str.title() 
reverse_title_case_string = title_case_string[::-1] 
print(reverse_title_case_string) 

 
#h. Count the number of times the letter “a” appears in the string 
str = "The quick brown fox jumps over the lazy dog" 
count = str.count("a") 
print(count) 


#i. Count the number of times the word “the” appears in the string 
str = "The quick brown fox jumps over the lazy dog" 
count = str.count("The") 
print(count) 

 
#j. Replace the word “the” with the word “a” 
str = "The quick brown fox jumps over the lazy dog" 
new_string = str.replace("the", "a") 
print(new_string) 

 

#4. count the frequency of each letter in the string and save the results in a dictionary (15 marks) 
str = "The quick brown fox jumps over the lazy dog" 
occurance = {} 
for letter in str: 
  occurance[letter] = occurance.get(letter, 0) + 1 
print(occurance) 

 
#5. Given the below lists; (15 marks) 
people = ['Jane', 'John', 'Jack', 'Janet'] 
sex = ['Female', 'Male', 'Male', 'Female'] 
age = [23, 34, 16, 28] 

#Interpolate the three lists into a string that reads: 

#Jane the Female is 23 years old. 

#John the Male is 34 years old. 

#Jack the Male is 16 years old. 

#Janet the Female is 28 years old. 

people = ['Jane', 'John', 'Jack', 'Janet'] 
sex = ['Female', 'Male', 'Male', 'Female'] 
age = [23, 34, 16, 28] 

for person, gender, years in zip(people, sex, age): 
  print(f"{person} the {gender} is {years} years old.") 

 

 