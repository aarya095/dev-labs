pets = [{
    'pet name' : 'turbo',
    'kind' : 'turtle',
    'owner name' : 'usha',
},
{
    'pet name' : 'lily',
    'kind' : 'dog',
    'owner name' : 'Diana'
},
{
    'pet name' : 'jerry',
    'kind' : 'guinea pig',
    'owner name' : 'roger'
},
{
    'pet name' : 'red',
    'kind' : 'fish',
    'owner name' : 'Omkar'
}]

for pet in pets:
    """Loops through the list and prints the information in lines"""
    print(f"{pet['pet name'].title()} is a {pet['kind'].title()}.")
    print(f"{pet['pet name'].title()} is owned by {pet['owner name'].title()}.\n")