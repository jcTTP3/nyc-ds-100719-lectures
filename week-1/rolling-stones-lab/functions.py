
import csv
import json
import matplotlib.pyplot as plt
with open('data.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)


#SEARCH FUNCTIONS
def find_name(string, data):
    for item in data:
        if string == item['album']:
            return item
    return None


def find_rank(string, data):
    for item in data:
        if string == item['number']:
            return item
    return None


def find_year(string, data):
    year = []
    for item in data:
        if item['year'] == string:
            year.append(item)
    return year

def find_by_years(start, end, data):
    albums = []
    for year in range(start, end +1):
        albums.append(find_year(str(year)))
    return albums

def find_by_ranks(start, end, data):
    ranks = []
    for rank in range(start, end+1):
        ranks.append(find_rank(str(rank)))
    return ranks

#ALL FUNCTIONS
def all_titles(data):
    titles = []
    for item in data:
        titles.append(item['album'])
    return titles

def all_artists(data):
    artists = []
    for item in data:
        artists.append(item['artist'])
    return artists

#QUESTIONS TO ANSWER FUNCTION
def most_albums(data):
    album_counts = {}
    for item in data:
        if item['artist'] not in album_counts:
            album_counts[item['artist']] = 1
        else:
            album_counts[item['artist']] += 1

    highest = {}
    highest_frequency = max(album_counts.values())
    for k,v in album_counts.items():
        if v == highest_frequency:
            highest[k] = v
    return highest

def most_popular_word(data):
    titles = all_titles()
    words = []
    for title in titles:
        for word in title.split():
            words.append(word)


    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    highest = {}
    highest_frequency = max(word_counts.values())
    for k,v in word_counts.items():
        if v == highest_frequency:
            highest[k] = v
    return highest

def hist_albums(data):
    album_years = []
    for item in data:
        album_years.append(int(item['year']))
    range_start = (min(album_years)//10)*10
    range_end = (max(album_years)//10+1)*10
    bins =int((range_end - range_start) / 10)
    plt.hist(album_years, range = (range_start, range_end), bins = bins)

def hist_genre(data):
    all_genres =[]
    for item in data:
        all_genres.append(item['genre'])
    single_word =[]
    for genre in all_genres:
        for word in genre.split(", "):
            single_word.append(word)

    genre_counts = {}
    for word in single_word:
        if word not in genre_counts:
            genre_counts[word] = 1
        else:
            genre_counts[word] += 1
    plt.xticks(rotation='vertical')
    plt.bar(genre_counts.keys(), genre_counts.values())

text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()

def string_to_list(string):
    list_strings = []
    for item in string.split("\t"):
        list_strings.append(item)
    return list_strings

def create_dict(list_):
    new_dict = {'rank': list_[0], 'name': list_[1], 'artist': list_[2], 'year': list_[3].strip('\n')}
    return new_dict
def list_of_songs(data):
    main_list = []
    for line in lines:
        x = string_to_list(line)
        main_list.append(create_dict(x))
    return main_list



file = open('track_data.json', 'r')
json_data = json.load(file)

def albumWithMostTopSongs(albums_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])

    album_counts = {}
    for album in albums_data:
        for track in album['tracks']:
            if track in song_names:
                if album['album'] not in album_counts.keys():
                    album_counts[album['album']] = 1
                else:
                    album_counts[album['album']] += 1
    highest = {}
    highest_frequency = max(album_counts.values())
    for k,v in album_counts.items():
        if v == highest_frequency:
            highest[k] = v
    return highest

def albumsWithTopSongs(albums_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])

    top_albums = []
    for album in albums_data:
        for track in album['tracks']:
            if track in song_names:
                top_albums.append(album['album'])
    return set(top_albums)

def songsThatAreOnTopAlbums(albums_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])

    songs_on_albums = []
    for album in albums_data:
        for track in album['tracks']:
            if track in song_names:
                songs_on_albums.append(track)
    return songs_on_albums

def top10AlbumsByTopSongs(albums_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])

    album_counts = {}
    for album in albums_data:
        for track in album['tracks']:
            if track in song_names:
                if album['album'] not in album_counts.keys():
                    album_counts[album['album']] = 1
                else:
                    album_counts[album['album']] += 1
    sorted_values = sorted(album_counts.values(), reverse = True)[:10]

    top_ten_album_counts = {}
    #while len(top_ten_album_counts) < 10:
    for k,v in album_counts.items():
        if v in sorted_values:
            top_ten_album_counts[k] = v
    x = top_ten_album_counts.keys()
    y = top_ten_album_counts.values()

    plt.xticks(rotation = 'vertical')
    return plt.bar(x, y)

    top10AlbumsByTopSongs(json_data, list_of_songs(lines))
