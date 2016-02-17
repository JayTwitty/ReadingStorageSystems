import unittest

from database_classes import StorageSystem


class DBTestCase(unittest.TestCase):

    def test_storage_system_can_format_expected_file_structure(self):
        expected_input = ["jtwitty,1234,jamario twitty,dec 7,hacker", "gtwitty,1234,gelisa twitty,dec 7,consultant"]
        expected_output = [["jtwitty", "1234", "jamario twitty", "dec 7", "hacker"], ["gtwitty", "1234", "gelisa twitty", "dec 7", "consultant"]]
        self.assertEqual(StorageSystem(expected_input), expected_output)

    def test_storage_system_can_format_expected_file_structure_in_init(self):
        expected_input = ["jtwitty,1234,jamario twitty,dec 7,hacker", "gtwitty,1234,gelisa twitty,dec 7,consultant"]
        expected_output = [["jtwitty", "1234", "jamario twitty", "dec 7", "hacker"], ["gtwitty", "1234", "gelisa twitty", "dec 7", "consultant"]]
        storage_reader = StorageSystem(expected_input)
        self.assertEqual(storage_reader.cleaned_data, expected_output)

    def test_storage_system_can_get_record_by_name_as_a_list(self):
        file_input = ["jtwitty,1234,jamario twitty,dec 7,hacker", "gtwitty,1234,gelisa twitty,dec 7,consultant"]
        storage_reader = StorageSystem(file_input)
        self.assertEqual(storage_reader.get_by_username_pw("jtwitty", "1234"),
                         ["jtwitty,1234,jamario twitty,dec 7,hacker"])
        self.assertEqual(storage_reader.get_by_username_pw("gtwitty", "1234"),
                         ["gtwitty,1234,gelisa twitty,dec 7,consultant"])

