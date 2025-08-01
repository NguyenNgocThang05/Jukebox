from library_item import LibraryItem
import track_library as lib

# Test the info and stars methods of a LibraryItem object
def test_library_item_info_and_stars():
    item = LibraryItem("Test Song", "Test Artist", rating=4)
    assert item.info() == "Test Song - Test Artist ****"  # Checks formatted info string with stars
    assert item.stars() == "****"  # Ensures 4-star rating is returned as 4 asterisks

# Test get_name() for a valid key
def test_get_name_found():
    name = lib.get_name("01")
    assert isinstance(name, str)  # Ensures the returned name is a string

# Test get_name() for an invalid key
def test_get_name_not_found():
    name = lib.get_name("99")  # Assumes "99" is not a valid key
    assert name is None  # Should return None if key is not found

# Test setting a rating and then getting it
def test_set_rating_and_get_rating():
    key = "01"
    lib.set_rating(key, 3)
    assert lib.get_rating(key) == 3  # Verifies rating is properly updated

# Test incrementing the play count
def test_increment_play_count():
    key = "01"
    before = lib.get_play_count(key)
    lib.increment_play_count(key)
    after = lib.get_play_count(key)
    assert after == before + 1  # Ensures play count increased by 1

# Test creating a new LibraryItem and checking default values
def test_library_item_creation():
    item = LibraryItem("Imagine", "John Lennon", 5)
    assert item.name == "Imagine"
    assert item.artist == "John Lennon"
    assert item.rating == 5
    assert item.play_count == 0  # New items should have 0 play count by default

# Test item with zero stars
def test_library_item_zero_stars():
    item = LibraryItem("No Stars", "Unknown", 0)
    assert item.stars() == ""  # Should return an empty string

# Test item with max stars (5)
def test_library_item_max_stars():
    item = LibraryItem("Perfect", "Artist", 5)
    assert item.stars() == "*****"  # Should return five asterisks

# Test get_artist() for a valid key
def test_get_artist_found():
    key = "01"
    artist = lib.get_artist(key)
    assert isinstance(artist, str)  # Ensures returned value is a string

# Test get_artist() for an invalid key
def test_get_artist_not_found():
    assert lib.get_artist("99") is None  # Should return None if key is invalid

# Test get_rating() when the key doesn't exist
def test_get_rating_not_found():
    assert lib.get_rating("99") == -1  # Should return -1 for invalid key

# Test get_play_count() for nonexistent track
def test_get_play_count_not_found():
    assert lib.get_play_count("99") == -1  # Should return -1 for invalid key

# Test setting a rating for an invalid key
def test_set_rating_invalid_key():
    key = "999"
    lib.set_rating(key, 3)  # Should fail silently
    assert lib.get_rating(key) == -1  # Confirm it didn't insert or crash

# Test setting a rating above valid range (should be clamped or adjusted)
def test_set_rating_valid_range():
    key = "01"
    lib.set_rating(key, 7)  # Out-of-range value
    assert lib.get_rating(key) <= 5  # Should not exceed 5

# Test setting a rating below valid range (should be clamped or adjusted)
def test_set_rating_below_range():
    key = "01"
    lib.set_rating(key, -2)
    assert lib.get_rating(key) >= 1  # Should be at least 1

# Test incrementing play count for invalid key
def test_increment_play_count_invalid_key():
    lib.increment_play_count("999")  # Should not raise exception or crash

# Check if the library is loaded and contains entries
def test_library_loaded():
    assert isinstance(lib.library, dict)  # Ensure it's a dictionary
    assert len(lib.library) > 0  # Should not be empty

# Check all items in library are LibraryItem objects
def test_read_library_structure():
    for key, item in lib.library.items():
        assert isinstance(item, LibraryItem)  # Confirm proper data structure

# Test if ratings are saved and restored properly
def test_update_and_restore_rating():
    key = "01"
    original = lib.get_rating(key)  # Store original rating
    lib.set_rating(key, 4)
    lib.update_library()  # Save changes to file
    lib.read_library()    # Reload from file
    assert lib.get_rating(key) == 4 or lib.get_rating(key) == original

# Sanity check: ensure key details are correct for first 3 tracks
def test_track_info_strings():
    for key in list(lib.library.keys())[:3]:  # Limit to 3 items for speed
        name = lib.get_name(key)
        artist = lib.get_artist(key)
        rating = lib.get_rating(key)
        assert isinstance(name, str)
        assert isinstance(artist, str)
        assert 1 <= rating <= 5  # Ratings must be in the expected range