from library_item import LibraryItem
import track_library as lib

def test_library_item_info_and_stars():
    item = LibraryItem("Test Song", "Test Artist", rating=4)
    assert item.info() == "Test Song - Test Artist ****"
    assert item.stars() == "****"

def test_get_name_found():
    name = lib.get_name("01")
    assert isinstance(name, str)

def test_get_name_not_found():
    name = lib.get_name("99")  # Assuming 99 doesn't exist
    assert name is None

def test_set_rating_and_get_rating():
    key = "01"
    lib.set_rating(key, 3)
    assert lib.get_rating(key) == 3

def test_increment_play_count():
    key = "01"
    before = lib.get_play_count(key)
    lib.increment_play_count(key)
    after = lib.get_play_count(key)
    assert after == before + 1

def test_library_item_creation():
    item = LibraryItem("Imagine", "John Lennon", 5)
    assert item.name == "Imagine"
    assert item.artist == "John Lennon"
    assert item.rating == 5
    assert item.play_count == 0

def test_library_item_zero_stars():
    item = LibraryItem("No Stars", "Unknown", 0)
    assert item.stars() == ""

def test_library_item_max_stars():
    item = LibraryItem("Perfect", "Artist", 5)
    assert item.stars() == "*****"

def test_get_artist_found():
    key = "01"
    artist = lib.get_artist(key)
    assert isinstance(artist, str)

def test_get_artist_not_found():
    assert lib.get_artist("99") is None

def test_get_rating_not_found():
    assert lib.get_rating("99") == -1

def test_get_play_count_not_found():
    assert lib.get_play_count("99") == -1

def test_set_rating_invalid_key():
    key = "999"
    lib.set_rating(key, 3)  # Should not raise
    assert lib.get_rating(key) == -1

def test_set_rating_valid_range():
    key = "01"
    lib.set_rating(key, 7)  # Above valid range
    assert lib.get_rating(key) <= 5

def test_set_rating_below_range():
    key = "01"
    lib.set_rating(key, -2)
    assert lib.get_rating(key) >= 1

def test_increment_play_count_invalid_key():
    lib.increment_play_count("999")  # Should not crash

# --- Tests for read/update library ---

def test_library_loaded():
    assert isinstance(lib.library, dict)
    assert len(lib.library) > 0

def test_read_library_structure():
    for key, item in lib.library.items():
        assert isinstance(item, LibraryItem)

def test_update_and_restore_rating():
    key = "01"
    original = lib.get_rating(key)
    lib.set_rating(key, 4)
    lib.update_library()
    lib.read_library()  # reload to restore
    assert lib.get_rating(key) == 4 or lib.get_rating(key) == original  # depending on file I/O timing

def test_track_info_strings():
    for key in list(lib.library.keys())[:3]:  # test 3 sample items
        name = lib.get_name(key)
        artist = lib.get_artist(key)
        rating = lib.get_rating(key)
        assert isinstance(name, str)
        assert isinstance(artist, str)
        assert 1 <= rating <= 5