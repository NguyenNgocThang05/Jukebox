import csv
from library_item import LibraryItem


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return


# Update library to CSV file
def update_library():
    file_name = "track_details.csv"

    with open(file_name, 'w', newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Name", "Artist", "Rating", "Play Count"]) # Write header row

        for i in range(1, len(library) + 1):
            key = "%02d" % i # Formatting key as two-digit string
            csv_writer.writerow([
                library[key].name,
                library[key].artist,
                library[key].rating,
                library[key].play_count
            ])

# Read the library from a CSV file
def read_library():
    global library
    library = {}  # Initialize empty dictionary

    with open("track_details.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) # Skip the header row

        trackID = 1
        for details in csv_reader:
            try:
                rating = int(details[2]) # Convert rating to integer
                # Validates rating within valid range from 0 to 5
                if rating < 1:
                    rating = 1
                elif rating > 5:
                    rating = 5
            except ValueError:
                rating = 1 # Default rating to 0 if invalid

            try:
                play_count = int(details[3]) # Convert play count to integer
            except ValueError:
                play_count = 0 # Default play count to 0 if invalid

            fixed_trackID = "%02d" % trackID     # Formatting track ID as two digit string
            library[fixed_trackID] = LibraryItem(details[0], details[1], rating)
            library[fixed_trackID].play_count = play_count
            trackID += 1

        return library


library = read_library()

if __name__ == "__main__":
    read_library()
    update_library()

    print(library)
    for key in library:
        print(library[key].info())