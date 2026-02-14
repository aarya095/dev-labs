favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

people_list = ['jen','albert','sarah','edward','phil','roger']

for person in people_list:
    
    if person not in favorite_languages.keys():
        print(f"{person.title()} you should take the poll.")
    else: 
        print(f"Thank you for responding {person.title()}!")