# This class represents a music library item with name, artist, rating and play count
class LibraryItem:
    # Constructor method to initialize the object
    def __init__(self, name, artist, rating=0):
        self.name = name        # Store the name of the item
        self.artist = artist    # Store the artist's name
        self.rating = rating    # Store the rating
        self.play_count = 0     # Initialize play count to 0

    #This function returns a formatted string with the name, artist, and star rating
    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    #This function convert numeric rating into a visual star format using "*"
    def stars(self):
        stars = ""                      # Initialize an empty string to hold stars
        for i in range(self.rating):    # Repeat loop equal to the rating value
            stars += "*"                # Add one star for each rating point
        return stars                    # Return the final star string
