# 8-8. User Album

def make_album():
    while True:
        user_input_artist_name = input("Enter Artist Name: ").lower(). strip()
        user_input_album_title = input("Enter Album Name: ").lower().strip()
        user_input_num_of_songs = int(input("Enter the number of songs the album has: "))

        if user_input_album_title == 'quit' or user_input_artist_name == 'quit'\
        or user_input_num_of_songs == 0:
            break
        dictionary = {'Artist Name': user_input_artist_name,
                    'Album Name' : user_input_album_title,
                    'Number of Songs' : user_input_num_of_songs}
        print(dictionary)

make_album()