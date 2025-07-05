import pytest
from library_item import LibraryItem

# Test instances
track_1 = LibraryItem("Song A", "Artist A", 1)
track_2 = LibraryItem("Song B", "Artist B", 2)
track_3 = LibraryItem("Song C", "Artist C", 3)
track_4 = LibraryItem("Song D", "Artist D", 4)
track_5 = LibraryItem("Song E", "Artist E", 5)

# Parameterized Tests for LibraryItem Constructor

@pytest.mark.parametrize(
    "name, artist, rating",
    [
        ("Song A", "Artist A", 1),
        ("Song B", "Artist B", 2),
        ("Song C", "Artist C", 3),
        ("Song D", "Artist D", 4),
        ("Song E", "Artist E", 5),
    ]
)
def test_library_item_constructor(name, artist, rating):
    """Test that LibraryItem objects are initialized correctly."""
    item = LibraryItem(name, artist, rating)
    assert item.name == name
    assert item.artist == artist
    assert item.rating == rating
    assert item.play_count == 0 # play_count should always start at 0

# Parameterized Tests for stars() method

@pytest.mark.parametrize(
    "rating, expected_stars",
    [
        (0, ""),        # No stars for 0 rating
        (1, "*"),       # One star for 1 rating
        (2, "**"),      # Two stars for 2 rating
        (3, "***"),     # Three stars for 3 rating
        (4, "****"),    # Four stars for 4 rating
        (5, "*****"),   # Five stars for 5 rating
    ]
)
def test_stars_method(rating, expected_stars):
    """Ensure that stars() method returns the correct number of asterisks."""
    item = LibraryItem("Test Song", "Test Artist", rating)
    assert item.stars() == expected_stars

# Parameterized Tests for info() method

@pytest.mark.parametrize(
    "name, artist, rating, expected_info",
    [
        ("Song A", "Artist A", 1, "Song A - Artist A *"),
        ("Song B", "Artist B", 2, "Song B - Artist B **"),
        ("Song C", "Artist C", 3, "Song C - Artist C ***"),
        ("Song D", "Artist D", 4, "Song D - Artist D ****"),
        ("Song E", "Artist E", 5, "Song E - Artist E *****"),

    ]
)
def test_info_method(name, artist, rating, expected_info):
    """Check if the info() method formats the output correctly for various ratings."""
    item = LibraryItem(name, artist, rating)
    assert item.info() == expected_info

# --- Tests for Attribute Modification ---

def test_attribute_modification_name():
    """Test direct modification of the 'name' attribute."""
    item = LibraryItem("Old Name", "Artist", 3)
    item.name = "New Name"
    assert item.name == "New Name"
    assert item.info() == "New Name - Artist ***"

def test_attribute_modification_artist():
    """Test direct modification of the 'artist' attribute."""
    item = LibraryItem("Song", "Old Artist", 3)
    item.artist = "New Artist"
    assert item.artist == "New Artist"
    assert item.info() == "Song - New Artist ***"

def test_attribute_modification_rating():
    """Test direct modification of the 'rating' attribute and its effect on stars/info."""
    item = LibraryItem("Song", "Artist", 2)
    assert item.stars() == "**"
    item.rating = 4
    assert item.rating == 4
    assert item.stars() == "****"
    assert item.info() == "Song - Artist ****"

def test_attribute_modification_play_count():
    """Test direct modification and increment of the 'play_count' attribute."""
    item = LibraryItem("Song", "Artist", 3)
    assert item.play_count == 0
    item.play_count = 10
    assert item.play_count == 10
    item.play_count += 1
    assert item.play_count == 11
    # Verify info() does not include play_count
    assert item.info() == "Song - Artist ***"


def test_play_count_non_integer_direct_assignment():
    """Test direct assignment of a non-integer to play_count."""
    item = LibraryItem("Non-Int Play Count", "Artist")
    item.play_count = "abc"
    assert item.play_count == "abc"
    # Further operations (e.g., item.play_count += 1) would then cause a TypeError

def test_rating_non_integer_direct_assignment():
    """Test direct assignment of a non-integer to rating."""
    item = LibraryItem("Non-Int Rating", "Artist")
    item.rating = "three"
    assert item.rating == "three"
    # Further operations (e.g., item.stars()) would then cause a TypeError

if __name__ == "__main__":
 pytest.main(["-v"]) # '-v' for verbose output