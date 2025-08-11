import datetime

# Python test faili programmine skript

name = input('What is your name? ')
age = input('How old are you? ')
print(f'Hello {name}')
print(f'You are {age} years old.')
#print('You are learning IT programming.')

if age.isdigit():
    age = int(age)
    if age < 18:
        print('Sorry, must be 18 years old or older to learn IT programming.')
    else:
        print('Good to go. You are learning IT programming.')

location = str.upper(input('Where do you live? '))
print(f'You\'re living location at {location}')

current_year = datetime.datetime.now().year
year_of_birth = current_year - age

print(f'You were born in {year_of_birth}.')
print('Have a nice day!')

canadaDayDate = datetime.datetime(2023, 7, 1)
print(f'Canada Day is on {canadaDayDate.strftime("%A, %B %d, %Y")}.')