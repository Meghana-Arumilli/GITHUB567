import unittest

from github import get_from_github


class TestGetRepo(unittest.TestCase):
    def test_normal_response(self):
        expected = [
            'Repo: BUMP Number of commits: 8',
            'Repo: DBMS Number of commits: 1',
            'Repo: Github567 Number of commits: 12',
            'Repo: IDS-PROJECT Number of commits: 4',
            'Repo: Knowledge-Management Number of commits: 3',
            'Repo: Testing567 Number of commits: 19'
]
        repos = get_from_github('Meghana-Arumilli')
        for r in repos:
            print(r)
            self.assertIn(r, expected)

    def test_bad_user_name(self):
        self.assertEqual(get_from_github('bbbaaddd'), 'unable to fetch repos from user')
        self.assertEqual(get_from_github(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()

# result = get_from_github('Meghana-Arumilli')
# for r in result:
#     print(r)