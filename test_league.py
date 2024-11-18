import unittest
from league import parse_results, calculate_points, rank_teams, format_output

class TestLeagueRanking(unittest.TestCase):

    def test_parse_results(self):
        line = "Lions 3, Snakes 3"
        self.assertEqual(parse_results(line), ("Lions", 3, "Snakes", 3))

    def test_calculate_points(self):
        results = [
            ("Lions", 3, "Snakes", 3),
            ("Tarantulas", 1, "FC Awesome", 0),
        ]
        points = calculate_points(results)
        self.assertEqual(points["Lions"], 1)
        self.assertEqual(points["Snakes"], 1)
        self.assertEqual(points["Tarantulas"], 3)
        self.assertEqual(points["FC Awesome"], 0)

    def test_rank_teams(self):
        points = {
            "Lions": 5,
            "Tarantulas": 6,
            "FC Awesome": 1,
            "Snakes": 1,
            "Grouches": 0
        }
        ranked = rank_teams(points)
        self.assertEqual(ranked[0], ("Tarantulas", 6))
        self.assertEqual(ranked[1], ("Lions", 5))
        self.assertEqual(ranked[2], ("FC Awesome", 1))

    def test_format_output(self):
        ranked = [
            ("Tarantulas", 6),
            ("Lions", 5),
            ("FC Awesome", 1),
            ("Snakes", 1),
            ("Grouches", 0)
        ]
        output = format_output(ranked)
        expected_output = (
            "1. Tarantulas, 6 pts\n"
            "2. Lions, 5 pts\n"
            "3. FC Awesome, 1 pt\n"
            "3. Snakes, 1 pt\n"
            "5. Grouches, 0 pts"
        )
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()