import unittest
from unittest.mock import patch
from parameterized import parameterized
from src.app import check_document_existance, get_doc_shelf, get_doc_owner_name, get_all_doc_owners_names, add_new_shelf

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


class TestFunctions(unittest.TestCase):

    @parameterized.expand(
        [
            ('11-2', True),
            ('2222222', False),
            ('2207 876234', True)
        ]
    )
    def test_check_document_existance(self, doc_number: str, flag: bool):
        self.assertEqual(check_document_existance(doc_number), flag)

    @patch("builtins.input", lambda *args: '222')
    def test_get_doc_shelf_1(self):
        self.assertNotEqual(get_doc_shelf(), '1')

    @patch("builtins.input", lambda *args: '11-2')
    def test_get_doc_shelf_2(self):
        self.assertEqual(get_doc_shelf(), '1')

    @patch("builtins.input", lambda *args: '11-2')
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), "Геннадий Покемонов")

    @parameterized.expand(
        [
            ('', ('3', False)),
            ('2', ('2', False)),
            ('5', ('5', True))
        ]
    )
    @patch("builtins.input", lambda *args: '3')
    def test_add_new_shelf(self, inp: str, out: tuple):
        self.assertTrue(add_new_shelf(inp) == out)

    def test_get_all_doc_owners_names(self):
        self.assertSetEqual(get_all_doc_owners_names(), {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})
