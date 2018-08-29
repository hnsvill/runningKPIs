import unittest
import pr5ks


class test_pr5ks(unittest.TestCase):

    def test_pr5ks(pr5ks):
        pr5ks.assertEqual(pr5ks.wrapper("6bd5f3c04e6b5279aca633c2a245dd9c"), {"user_id": "6bd5f3c04e6b5279aca633c2a245dd9c", "current_year_5k_PRs_pace": 0})