class LibraryItem:
    """
    # Defines a class named LibraryItem,
     which serves as a blueprint for creating objects
     showing as items in a library
    """
    def __init__(self, name, artist, rating=0): # Constructor method. Calls automatically when a new LibraryItem object is created
        self.name = name # Initialize an instance variable "name" with the value passed in the "name" parameter
        self.artist = artist # Initialize an instance variable "artist" with the value passed in the "artist" parameter
        self.rating = rating # Initialize an instance variable "rating" with the value passed in the "rating" parameter or its default
        self.play_count = 0 # Initialize an instance variable "play_count" to 0. This variable will show how many times the track has been played

    def info(self):
        """
        Defines a method named "info" that returns a formatted string containing information about the library item
        """
        return f"{self.name} - {self.artist} {self.stars()}" # Uses to create a track's detail string

    def stars(self):
        """
        Defines a method named "stars" that generates a string of '*' based on the track's rating.
        """
        stars = "" # Initialize an empty string variable named "stars"
        for i in range(self.rating): # Initialize a for loop that iterates rating's times.
                                     # Meaning that if the star rating is 3, the loop will run 3 times.
            stars += "*" # In each iteration, a '*' is appended to the "stars" string
        return stars # Returns the final string of '*'
