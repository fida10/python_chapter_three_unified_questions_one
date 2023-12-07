import unittest
from chapter_three_unified_questions_one import city_descriptions, manage_guests, sort_and_reverse


class TestCityDescriptions(unittest.TestCase):
    def test_city_descriptions(self):
        cities = {
            "Paris": "The City of Light",
            "New York": "The Big Apple",
            "Tokyo": "The bustling capital of Japan"
        }
        expected = [
            "Paris: The City of Light",
            "New York: The Big Apple",
            "Tokyo: The bustling capital of Japan"
        ]
        self.assertEqual(city_descriptions(cities), expected)

    def test_empty_dict(self):
        self.assertEqual(city_descriptions({}), [])

if __name__ == '__main__':
    unittest.main()
    

class TestManageGuests(unittest.TestCase):
    def test_guest_replacement(self):
        guests = ["Alice", "Bob", "Charlie"]
        self.assertEqual(
            manage_guests(guests, "Bob", "Diana"),
            ["Alice", "Diana", "Charlie"]
        )

    def test_guest_replacement_not_in_list(self):
        guests = ["Alice", "Charlie"]
        self.assertEqual(
            manage_guests(guests, "Bob", "Diana"),
            # Assuming we add Diana even if Bob wasn't found
            ["Alice", "Charlie", "Diana"]
        )

if __name__ == '__main__':
    unittest.main()


class TestSortAndReverse(unittest.TestCase):
    def test_sort_and_reverse(self):
        numbers = [3, 1, 4, 1, 5, 9, 2]
        sorted_asc, sorted_desc = sort_and_reverse(numbers)
        self.assertEqual(sorted_asc, [1, 1, 2, 3, 4, 5, 9])
        self.assertEqual(sorted_desc, [9, 5, 4, 3, 2, 1, 1])

    def test_empty_list(self):
        self.assertEqual(sort_and_reverse([]), ([], []))


if __name__ == '__main__':
    unittest.main()
