from phonebook import Phonebook
import pytest
import sys

@pytest.fixture
def phonebook(tmpdir):
    """ returns a Phonebook object. """
    return Phonebook(tmpdir)

def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")

@pytest.mark.skip("WIP")
# @pytest.mark.skipif(sys.version_info < (3,6), reason="requires python3.6 or higher")
def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")
    