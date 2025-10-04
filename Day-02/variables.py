# variables in python

first_name = "John"
last_name = "Smith"
country = "England"
city = "London"
age = "35"
is_married = True
skills = ['HTML', 'Python']
person_info = {
    'firstname' : 'John',
    'lastname' : 'Smith',
    'country' : 'England',
    'city' :'London'
}

# printing the value stored in varaibles
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'John', 'Smith', 'London', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)