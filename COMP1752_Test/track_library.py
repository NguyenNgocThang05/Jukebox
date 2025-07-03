import csv
from library_item import LibraryItem


# library = {}
# library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
# library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
# library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)
# library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
# library["05"] = LibraryItem("Someone Like You", "Adele", 3)


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
    file_name = "data.csv"

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

    with open("data.csv", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) # Skip the header row

        counter = 1
        for details in csv_reader:
            try:
                rating = int(details[2]) # Convert rating to integer
                # Validates rating within valid range from 0 to 5
                if rating < 0:
                    rating = 0
                elif rating > 5:
                    rating = 5
            except ValueError:
                rating = 0 # Default rating to 0 if invalid

            try:
                play_count = int(details[3]) # Convert play count to integer
            except ValueError:
                play_count = 0 # Default play count to 0 if invalid

            formatter = "%02d" % counter     # Formatting key as two digit string
            library[formatter] = LibraryItem(details[0], details[1], rating)
            library[formatter].play_count = play_count
            counter += 1

        return library



library = read_library()

if __name__ == "__main__":
    read_library()
    update_library()

    print(library)
    for key in library:
        print(library[key].info())