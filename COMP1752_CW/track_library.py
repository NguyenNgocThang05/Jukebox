import csv
from library_item import LibraryItem


def list_all():
    """
    Defines a function named "list_all" that lists all tracks in the library
    """
    output = "" # Initialize an empty string to store the output
    for key in library: # Loops through each key in the library dictionary
        item = library[key] # Retrieves the LibraryItem object with the current key from the library dictionary
        output += f"{key} {item.info()}\n" # Appends a string to "output".
    return output


def get_name(key):
    """
    Defines a function named "get_name" that attempts to return the name of a track given its key
    """
    try:
        # Initialize a try block to handle errors
        item = library[key] # Tries to retrieve the LibraryItem object using the provided key
        return item.name # If success, returns the "name" attribute of the retrieved item
    except KeyError:
        # If the key doesn't exist in the library a KeyError will occure
        return None # Returns None to tell that the track was not found


def get_artist(key):
    """
    Defines a function named "get_artist" that attempts to retrieve the artist of the track given its key
    """
    try:
        # Initialize a try block to handle errors
        item = library[key] # Tries to retrieve the LibraryItem object using its given key
        return item.artist # If success, returns the "artist" attribute of the retrieved item
    except KeyError:
        # If a KeyError occurs
        return None # Returns None


def get_rating(key):
    """
    Defines a function named "get_rating" that attempts to retrieve the rating of a track given its key
    """
    try:
        # Initialize a try block to handle errors
        item = library[key] # Tries to retrieve the LibraryObject using its given key
        return item.rating # If success, returns the "rating" attribute of the item
    except KeyError:
        # If a KeyError occurs
        return -1 # Returns -1 to tell that the track was not found or has no rating


def set_rating(key, rating):
    """
    Defines a function named "set_rating" that attempts to set the rating of a track
    """
    try:
        # Initialize a try block to handle errors
        item = library[key] # Tries to retrieve the LibraryItem Object
        item.rating = rating # If success, sets the "rating" attribute of the item to the provided "rating" value parameter
    except KeyError:
        # If a KeyError occurs
        return # The function returns without doing anything


def get_play_count(key):
    """
    Defines a function named "get_play_count" that attempts to retrieve the play count of a track
    """
    try:
        # Initialize a try block to handle errors
        item = library[key] # Tries to retrieve the LibraryItem object
        return item.play_count # If success, returns the "play_count" attribute of the item
    except KeyError:
        # If a KeyError occurs
        return -1 # Returns -1 to tell that the track was not found


def increment_play_count(key):
    """
    Defines a function named "increment_play_count" that attempts to increase the play count of a track
    """
    try:
        # Initialize a try block to handle errors
        item = library[key] # Tries to retrieve the LibraryItem object
        item.play_count += 1 # If success, increments the "play_count" attribute of the item by 1
    except KeyError:
        # If a KeyError occurs
        return # The function returns without doing anything


# Update library to CSV file
def update_library():
    """
    Defines a function named "update_library" that writes the current state of the "library" dictionary to a CSV file
    """
    file_name = "track_details.csv" # Sets the name of the CSV file to "track_details.csv"

    with open(file_name, 'w', newline="") as csvfile:
        """
        Opens the file in write mode ('w')
        "newline=" is used to prevent extra blank rows in the CSV file
        The "with" statement makes sure that the file is closed even if error occur
        """
        csv_writer = csv.writer(csvfile) # Creates a CSV writer object used to write rows to the CSV file
        csv_writer.writerow(["Name", "Artist", "Rating", "Play Count"]) # Write header row to CSV file

        for trackID in range(1, len(library) + 1):
            """
            Loops from 1 up to total number of tracks in the "library"
            The reason why it starts from 1 and the total of track increment plus 1
            Because we do not want the user to see the ID track of 00
            """
            fixed_trackID = "%02d" % trackID # Formatting fixed_trackID as two-digit string (1 becomes 01, if it's 10 it will stay as 10)
            csv_writer.writerow([
                # Writes a row to the CSV file
                library[fixed_trackID].name, # The name of the track
                library[fixed_trackID].artist, # The artist of the track
                library[fixed_trackID].rating, # The rating of the track
                library[fixed_trackID].play_count # The play count of the track
            ])

# Read the library from a CSV file
def read_library():
    """
    Defines a function named "read_library" that reads library item (track) details from a CSV file and
    populates the library dictionary
    """
    global library # Declares that the "library" variable being used inside this function is the global "library" dictionary,
                   # allowing the function to modify it
    library = {}  # Initialize the global "library" dictionary as an empty string

    with open("track_details.csv", newline="") as csvfile:
        # Open the track_details.csv file in read mode
        csv_reader = csv.reader(csvfile) # Creates a CSV reader object to iterate over rows in the CSV file
        next(csv_reader) # Skip the header row, assuming it's a header row

        trackID = 1 # Initialize a counter for assigning track IDs
        for details in csv_reader:
            # Loops through each remaining row (list of strings) in the CSV file
            try:
                rating = int(details[2]) # Tries to convert the third element of the row (index 2, which is the rating) to an integer
                # Validates rating within valid range from 0 to 5
                if rating < 1: # If the rating is less than 1
                    rating = 1 # Set it to 1
                elif rating > 5: # If the rating is greater than 5
                    rating = 5 # Set it to 5
            except ValueError:
                # If the conversion to integer fails
                rating = 1 # Default rating to 0 if invalid

            try:
                play_count = int(details[3]) # Tries to convert the fourth element of the row (index 3, which is play count) to an integer
            except ValueError:
                # If the conversion to integer fails
                play_count = 0 # Default play count to 0 if invalid

            fixed_trackID = "%02d" % trackID     # Formatting track ID as two digit string (Ex: 1 becomes 01 and 10 is still 10)
            library[fixed_trackID] = LibraryItem(details[0], details[1], rating) # Creates a new LibraryItem object
                                                                                 # This new object is then added to the "library" dictionary with "fixed_trackID" as its key
            library[fixed_trackID].play_count = play_count # Sets the "play_count" attribute of the newly created LibraryItem object
            trackID += 1 # Increments the "trackID" for the next track

        return library # Returns the library dictionary


library = read_library() # Calls the read_library function immediately when the program runs

if __name__ == "__main__":
    read_library()
    update_library()

    print(library)
    for key in library:
        print(library[key].info())