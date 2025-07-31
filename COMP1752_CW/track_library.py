import csv # Import the csv module to handle reading/writing CSV file
from library_item import LibraryItem # Import the LibraryItem class from the library_item


def list_all():
    # Returns a formatted string listing all items in the library
    output = ""     # Initialize an empty string to store output
    for key in library:     # Loop through each key in the library dictionary
        item = library[key]     # Retrieve the LibraryItem object based on the key
        output += f"{key} {item.info()}\n"      # Append formatted string of item info to output
    return output # Return the final combined string


def get_name(key):
    # Returns the name of the item by its key
    try:
        item = library[key]     # Attempt to access the item using the key
        return item.name        # Return the name attribute
    except KeyError:
        return None             # If key doesn't exist, return None


def get_artist(key):
    # Return the artist of the item by its key
    try:
        item = library[key]     # Access the item
        return item.artist      # Return the artist name
    except KeyError:
        return None             # Return None if key not found


def get_rating(key):
    # Returns the rating of the item
    try:
        item = library[key]     # Access the item
        return item.rating      # Return the rating value
    except KeyError:
        return -1               # Return -1 if item not found


def set_rating(key, rating):
    # Sets the rating of an item, ensuring it stays within range 1-5
    try:
        rating = int(rating)        # Convert rating to integer

        if rating < 1:              # Minimum rating is 1
            rating = 1
        elif rating > 5:            # Maximum rating is 5
            rating = 5

        item = library[key]         # Access the item
        item.rating = rating        # Update the rating
    except KeyError:
        return                      # Do nothing if the key is not found


def get_play_count(key):
    # Returns the number of times the item has been played
    try:
        item = library[key]         # Access the item
        return item.play_count      # Return the play count
    except KeyError:
        return -1                   # Return -1 if item not found


def increment_play_count(key):
    # Increments the play count of the item by 1
    try:
        item = library[key]         # Access the item
        item.play_count += 1        # Increase play count by 1
    except KeyError:
        return                      # Do nothing if key not found


# Update library to CSV file
def update_library():
    # Saves the current library to a csv file
    file_name = "track_details.csv"     # Define the file name

    with open(file_name, 'w', newline="") as csvfile:   # Open file in write mode
        csv_writer = csv.writer(csvfile)    # Create a CSV writer object
        csv_writer.writerow(["Name", "Artist", "Rating", "Play Count"]) # Write header row

        for i in range(1, len(library) + 1): # Loop through the number of items
            key = "%02d" % i # Formatting key as two-digit string
            csv_writer.writerow([
                library[key].name,          # Write name to CSV
                library[key].artist,        # Write artist to CSV
                library[key].rating,        # Write rating to CSV
                library[key].play_count     # Write play count to CSV
            ])

def read_library():
    # Read the library from a CSV file
    global library  # Declare the global variable library
    library = {}  # Initialize empty dictionary

    with open("track_details.csv", newline="") as csvfile: # Open file in read mode
        csv_reader = csv.reader(csvfile)    # Create a CSV reader object
        next(csv_reader) # Skip the header row

        trackID = 1 # Start track ID from 1
        for details in csv_reader:  # Loop through each row of the CSV
            try:
                rating = int(details[2]) # Convert rating to integer
                # Ensuring rating is within range from 1 to 5
                if rating < 1:
                    rating = 1
                elif rating > 5:
                    rating = 5
            except ValueError:
                rating = 1 # Default rating if invalid

            try:
                play_count = int(details[3]) # Convert play count to integer
            except ValueError:
                play_count = 0 # Default play count to 0 if invalid

            formatted_trackID = "%02d" % trackID     # Formatting track ID as two digit string (e.g, 01, 02)
            library[formatted_trackID] = LibraryItem(details[0], details[1], rating)
            library[formatted_trackID].play_count = play_count  # Set play count
            trackID += 1    # Increment track ID for the next item

        return library # Return the library dictionary


library = read_library() # Load library from CSV file when module is imported

if __name__ == "__main__":
    read_library() # Reload the library
    update_library() # Save the library to CSV

    print(library) # Print the raw dictionary
    for key in library: # Loop through all items
        print(library[key].info()) # Print the formatted info of each item