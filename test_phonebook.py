import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook()

    # def tearDown(self):
    #     pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_numbers(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12346")
        self.assertTrue(self.phonebook.is_consistent())
    
    def test_inconsistent_with_duplicate(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")
        self.assertFalse(self.phonebook.is_consistent())