people = [
    {
        'first name':'hari',
        'last name' : 'yadav',
        'relationship':'friend',
        'phone number': 12334556789,
        'city' : 'kolkata'
    },
    {
        'first name':'bharat',
        'last name' : 'patel',
        'relationship':'cousin',
        'phone number': 28736482736,
        'city' : 'delhi'
    },
    {
        'first name':'pusha',
        'last name' : 'sharma',
        'relationship':'colleague',
        'phone number': 97234723422,
        'city' : 'chennai'
    }
]

for person in people:
    """Prints lines describing each person"""
    print(f"\n{person['first name'].title()} {person['last name'].title()} is my {person['relationship'].title()}.")
    print(f"{person['first name'].title()} lives in {person['city'].title()}.")
    print(f"{person['first name'].title()}'s phone number is {person['phone number']}.\n")