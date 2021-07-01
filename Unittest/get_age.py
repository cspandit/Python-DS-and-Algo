from datetime import date
import unittest
import sys
from unittest import mock

def get_person_age(person_id):
    raise RuntimeError


def calculate_person_age(person_id):
    person = get_person_age(person_id)
    ani = person['anniversary']
    bd = person['birthday']

    return ani.year-bd.year

class Tests(unittest.TestCase):
    def test_person_age(self):
        module = sys.modules[__name__]
        print(module)
        with mock.patch.object(module, 'get_person_age') as m:
            m.return_value = {'anniversary':date(2012, 10, 2),
              '               birthday':date(1990, 10, 2)}

        age = calculate_person_age(43)
        self.assertEqual(age, 23)
        m.assert_called_once_with(43)

if __name__ == '__main__':
    unittest.main()