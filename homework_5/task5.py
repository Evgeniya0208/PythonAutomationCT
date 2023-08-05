# 5) Create a function called print_song_details that prints the details of a song. The function should take two positional arguments:
# title and artist, and three keyword arguments: duration, genre, and year. Assume that duration has a default value of 0,
# genre has a default value of "Unknown", and year has a default value of None.
def print_song_details(title, artist, duration=0, genre="Unknown", year=None):
    print(title, artist, duration, genre, year)


print_song_details("'Hello, Dolly'", "Louis Armstrong", duration=187, genre="jazz", year=1969)
