import unittest
import pr5ks
import moreThan10km
import greaterThan3kmStreak

class test_pr5ks(unittest.TestCase):

    def test_pr5ks(self):
        self.assertEqual(pr5ks.wrapper("6bd5f3c04e6b5279aca633c2a245dd9c"), '{"user_id": "6bd5f3c04e6b5279aca633c2a245dd9c", "current_year_5k_PRs_pace": 0}')
        self.assertEqual(pr5ks.wrapper("4e7aaa167b9b5ff7b9b3a22dee8c2085"), '{"user_id": "4e7aaa167b9b5ff7b9b3a22dee8c2085", "current_year_5k_PRs_pace": 0}')
        self.assertEqual(pr5ks.wrapper("c7e962db02da55209f02fe3d8a86c99d"), '{"user_id": "c7e962db02da55209f02fe3d8a86c99d", "current_year_5k_PRs_pace": 2}')
        self.assertEqual(pr5ks.wrapper("d77908482ed2505ebbf17ef72be2f080"), '{"user_id": "d77908482ed2505ebbf17ef72be2f080", "current_year_5k_PRs_pace": 1}')
        self.assertEqual(pr5ks.wrapper("72eff89c74cc57178e02f103187ad579"), '{"user_id": "72eff89c74cc57178e02f103187ad579", "current_year_5k_PRs_pace": 0}')
        self.assertEqual(pr5ks.wrapper("40d7ae29e393582abdbcb8c726249e22"), '{"user_id": "40d7ae29e393582abdbcb8c726249e22", "current_year_5k_PRs_pace": 0}')


class test_moreThan10km(unittest.TestCase):
    
    def test_moreThan10km(self):
        self.assertEqual(moreThan10km.wrapper("6bd5f3c04e6b5279aca633c2a245dd9c"), '{"user_id": "6bd5f3c04e6b5279aca633c2a245dd9c", "weeks_10k_aggregated": 66}')
        self.assertEqual(moreThan10km.wrapper("4e7aaa167b9b5ff7b9b3a22dee8c2085"), '{"user_id": "4e7aaa167b9b5ff7b9b3a22dee8c2085", "weeks_10k_aggregated": 8}')
        self.assertEqual(moreThan10km.wrapper("c7e962db02da55209f02fe3d8a86c99d"), '{"user_id": "c7e962db02da55209f02fe3d8a86c99d", "weeks_10k_aggregated": 3}')
        self.assertEqual(moreThan10km.wrapper("d77908482ed2505ebbf17ef72be2f080"), '{"user_id": "d77908482ed2505ebbf17ef72be2f080", "weeks_10k_aggregated": 10}')
        self.assertEqual(moreThan10km.wrapper("72eff89c74cc57178e02f103187ad579"), '{"user_id": "72eff89c74cc57178e02f103187ad579", "weeks_10k_aggregated": 61}')
        self.assertEqual(moreThan10km.wrapper("40d7ae29e393582abdbcb8c726249e22"), '{"user_id": "40d7ae29e393582abdbcb8c726249e22", "weeks_10k_aggregated": 0}')


class test_greaterThan3kmStreak(unittest.TestCase):
    
    def test_greaterThan3kmStreak(self):
        self.assertEqual(greaterThan3kmStreak.wrapper("6bd5f3c04e6b5279aca633c2a245dd9c"), '{"user_id": "6bd5f3c04e6b5279aca633c2a245dd9c", "kept_distance_consistent": 19}')
        self.assertEqual(greaterThan3kmStreak.wrapper("4e7aaa167b9b5ff7b9b3a22dee8c2085"), '{"user_id": "4e7aaa167b9b5ff7b9b3a22dee8c2085", "kept_distance_consistent": 5}')
        self.assertEqual(greaterThan3kmStreak.wrapper("c7e962db02da55209f02fe3d8a86c99d"), '{"user_id": "c7e962db02da55209f02fe3d8a86c99d", "kept_distance_consistent": 3}')
        self.assertEqual(greaterThan3kmStreak.wrapper("d77908482ed2505ebbf17ef72be2f080"), '{"user_id": "d77908482ed2505ebbf17ef72be2f080", "kept_distance_consistent": 7}')
        self.assertEqual(greaterThan3kmStreak.wrapper("72eff89c74cc57178e02f103187ad579"), '{"user_id": "72eff89c74cc57178e02f103187ad579", "kept_distance_consistent": 21}')
        self.assertEqual(greaterThan3kmStreak.wrapper("40d7ae29e393582abdbcb8c726249e22"), '{"user_id": "40d7ae29e393582abdbcb8c726249e22", "kept_distance_consistent": 0}')


if __name__ == "__main__":
    unittest.main()