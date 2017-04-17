import random
import csv
from time import strftime

music = []      # establish list for use
times = []

with open('music.csv', 'r', newline='', encoding='utf-8-sig') as f:
    reader = csv.reader((line.replace(' | ', '|') for line in f), delimiter='|')
    for row in reader:
        name = (row[0], row[1])     # make tuplet with artist and album name
        row[2] = int(row[2])        # change date of album to int
        information = (row[2], row[3], row[4])  # make tuplet with year genre length
        name_and_information = (name, information)  # make tuplet with 2 tuplet
        music.append(name_and_information)
        times.append(row[4])


def add_new_element():
    artist = input("Enter name of artist: ")
    album = input("Enter name of album: ")
    year = input("Enter year of release album: ")
    if not year.isdigit():
        add_new_element()
    else:
        type_music = input("Enter type of music: ")
        time = input("Enter time of album in format min:sec (example 43:42): ")

        new = artist + ' | ' + album + ' | ' + year + ' | ' + type_music + ' | ' + time
        with open('music.csv', "a") as add_record:
            add_record.write(new + "\n")

        music.append(((artist, album), (int(year), type_music, time)))


def find_album_by_artist():
    names_of_albums = []
    found = False
    print("Enter name of artist:")
    artist_name = input()
    for main_tuple in music:
        if artist_name.lower() == str(main_tuple[0][0]).lower():
            author = main_tuple[0][0]
            album_name = main_tuple[0][1]
            names_of_albums.append(album_name)
            found = True
    if found is True:
        print("All albums maked by this artist:\n")
        print("\n".join(names_of_albums))
    else:
        print("Artist not found! Please try again.")


def find_album_by_year():
    names_of_albums = []
    found = False
    print("Enter year of album:")
    year_album = input()
    for main_tuple in music:
        if year_album.lower() == str(main_tuple[1][0]).lower():
            year = main_tuple[1][0]
            album_name = main_tuple[0][1]
            names_of_albums.append(album_name)
            found = True
    if found is True:
        print("All albums maked in this year:\n")
        print("\n".join(names_of_albums))
    else:
        print("Year not found! Please try again.")


def find_musician_by_album():
    names_of_musician = []
    found = False
    print("Enter name of album:")
    album_name = input()
    for main_tuple in music:
        if str(main_tuple[0][1]).lower() == album_name.lower():
            author = main_tuple[0][0]
            album_name = main_tuple[0][1]
            names_of_musician.append(author)
            found = True
    if found is True:
        print("Author of your album is: ".join(names_of_musician))
    else:
        print("Album not found! Please try again.")


def find_album_by_letter():
    names_of_albums = []
    found = False
    letter = input("Type letter(s)")
    for main_tuple in music:
        if letter.lower() in str(main_tuple[0][1]):
            album = main_tuple[0][1]
            names_of_albums.append(album)
            found = True
    if found is True:
        print("Albums with your letter(s): ")
        print("\n".join(names_of_albums))
    else:
        print("No album with that letter(s)")


def find_album_by_genre():
    names_of_albums = []
    found = False
    print("Enter name of genre:")
    genre_name = input()
    for main_tuple in music:
        if genre_name.lower() == str(main_tuple[1][1]).lower():
            genre = main_tuple[1][1]
            album_name = main_tuple[0][1]
            names_of_albums.append(album_name)
            found = True
    if found is True:
        print("Albums for choosen genre:\n ")
        print("\n".join(names_of_albums))
    else:
        print("Albums not found! Please try again.")


def Calculate_age_of_all_albums():
    sum_age = 0
    current_year = int(strftime("%Y"))
    for main_tuple in music:
        album_year = int(main_tuple[1][0])
        age = current_year - album_year
        sum_age += age
    print(sum_age)


def choose_random_album_by_genre():
    random_genre = []
    found = False
    genre_name = input("Enter genre: ")
    for main_tuple in music:
        if genre_name.lower() == str(main_tuple[1][1]).lower():
            genre = main_tuple[1][1]
            album_name = main_tuple[0][1]
            random_genre.append(album_name)
            found = True
    if found is True:
        genre_random = random.choice(random_genre)
        print(genre_random)
    else:
        print("Genre or album not found! Please try again.")


def amount_of_albums_by_artist():
    name_albums = []
    amount = 0
    found = False
    artist_name = input("Eneter the artist name: ")
    for main_tuple in music:
        if artist_name.lower() == str(main_tuple[0][0]).lower():
            author = main_tuple[0][0]
            album_name = main_tuple[0][1]
            name_albums.append(album_name)
            amount += 1
            found = True
    if found is True:
        print("Albums for choosen artist:\n ")
        print("\n".join(name_albums))
        print("\nAmount of albums = %s" % amount)
    else:
        print("Artist or album not founded! Please try again.")


def longest_time_album():
    longest = sorted(times)[-1]  # getting the time of longest album
    for main_tuple in music:
        if (main_tuple[1])[2] == longest:
            name_of_longest = (main_tuple[0])[1]
            print("Longest album: " + name_of_longest + "It lasts " + longest)


# menu loop
while True:

    menu = input("""\nWelcome in the CoolMusic! Choose the action:
1) Add new album
2) Find albums by artist
3) Find albums by year
4) Find musician by album
5) Find albums by letter(s)
6) Find albums by genre
7) Calculate the age of all albums
8) Choose a random album by genre
9) Show the amount of albums by an artist
10) Find the longest-time album
0) Exit\n
Enter the number: """)
    # here we use definitions from top
    if menu == "1":
        add_new_element()

    elif menu == "2":
        find_album_by_artist()

    elif menu == "3":
        find_album_by_year()

    elif menu == "4":
        find_musician_by_album()

    elif menu == "5":
        find_album_by_letter()

    elif menu == "6":
        find_album_by_genre()

    elif menu == "7":
        Calculate_age_of_all_albums()

    elif menu == "8":
        choose_random_album_by_genre()

    elif menu == "9":
        amount_of_albums_by_artist()

    elif menu == "10":
        longest_time_album()
    else:
        if menu != "0":
                print("\nUncorrect vaule")
        elif menu == "0":
            print("\nSee you!\n")
            exit()
# musiccolector
