# 5-1. Conditional Tests | 5-2. More Conditional Tests

my_age = 19

#1
print("Am I 18+? I predict True.")
print(my_age > 18)

#2
print("\nAm I a tennager? I predict True.")
print(12 < my_age < 20)

#3
print("\nAm I in my early twenties? I predict False.")
print(20 <= my_age <= 25)

#4
print("\nAm I just a kid? I predict False.")
print(4 <= my_age <= 12)

#5
print("\nAm I 15 years old? I preduct False.")
print(my_age == 15)

my_name = 'aarya'

#6
print("\nIs my name aarya? I predict True.")
print(my_name == 'aarya')

#7
print("\nIs my name manish? I predict False.")
print(my_name == 'manish')

friend_name = 'Manish'

#8
print("\nIs my friend's name manish? I predict True.")
print(friend_name.lower() == 'manish')

#9
print("\nIs my friend's name manish? I predict True.")
print(friend_name == 'manish') #without using lower() method

my_interests = ['linux','networking','python']

#10
print("\nAm I interested in python? I predict True.")
print('python' in my_interests)

#11
print("\nAm I interested in game development? I predict False.")
print('game development' in my_interests)

#12
print("\nAm I interested in linux and networking? I predict True.")
print('linux' in my_interests and 'networking' in my_interests)

#13
print("\nAm I interested in python and java? I predict False.")
print('python' in my_interests and 'java' in my_interests)

#14
print("\nAm I interested in definitely either python or java, aren't I? I predict True.")
print('python' in my_interests or 'java' in my_interests)

#15
print("\nI am not interested in game development, right? I predict True.")
print('game development' not in my_interests)

#16
print("\nI am not interested in linux, right? I predict False.")
print('linux' not in my_interests)