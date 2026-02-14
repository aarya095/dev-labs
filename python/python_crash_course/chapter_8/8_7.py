# 8-7. Album

def make_album(artist_name, album_title, num_of_songs_in_album='Not specified'):
    dictionary = {'Artist Name': artist_name,
                  'Album Name' : album_title,
                  'Number of Songs' : num_of_songs_in_album}
    print(dictionary)

make_album('Patti Smith','Horses')
make_album('Neli Young','After the Gold Rush', 12)
make_album('Madonna','Like a Prayer')

