import unittest
import cli
from location.scoring import StumbleScore

class CLITestCase(unittest.TestCase):
    def setUp(self):
        self.location = StumbleScore(19078)
        self.location.search()

    def test_cli_welcome(self):
        r = cli.cli('test')
        self.assertIn('Welcome to StumbleScore', r)

    def test_cli_address(self):
        r = cli.cli(19078)
        self.assertIn('19078', r)
    
    def test_cli_geocode(self):
        r = cli.cli(19078)
        self.assertIn('-75.32', r)
        self.assertIn('39.8', r)
    
    def test_bar_count(self):
        r = self.location.bar_count()
        self.assertEqual(r, 3)

    def test_score(self):
        r = self.location.score()
        self.assertEqual(r, 15.0)

    def test_category(self):
        r = self.location.category()
        self.assertEqual(r, 'Dry')

if __name__ == '__main__':
    unittest.main()
