import io
from unittest import mock, TestCase

from leagueranking.leagueranking import League


class TestLeague(TestCase):
    def test_extract_score(self):
        league = League()
        self.assertEqual(
            league.extract_score("FC Awesome 0"),
            {"team": "FC Awesome", "score": 0}
        )

    def test_extract_score_fail(self):
        league = League()
        self.assertEqual(
            league.extract_score("No Score"),
            {}
        )

    def test_update_ranking_team_1_win(self):
        league = League()
        league.update_ranking("Tarantulas 1, FC Awesome 0")
        self.assertEqual(
            league.ranking,
            {"FC Awesome": 0, "Tarantulas": 3},
        )

    def test_update_ranking_team_2_win(self):
        league = League()
        league.update_ranking("Grouches 0, Snakes 1")
        self.assertEqual(
            league.ranking,
            {"Snakes": 3, "Grouches": 0},
        )

    def test_update_ranking_draw(self):
        league = League()
        league.update_ranking("Tarantulas 1, FC Awesome 1")
        self.assertEqual(
            league.ranking,
            {"FC Awesome": 1, "Tarantulas": 1},
        )

    def test_process_file(self):
        league = League()
        league.process_file(filename="sample_input.txt")
        self.assertDictEqual(
            league.ranking,
            {
                "Tarantulas": 6,
                "Lions": 5,
                "FC Awesome": 1,
                "Snakes": 1,
                "Grouches": 0,

            },
        )

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_ranking(self, mock_stdout):
        league = League()
        league.update_ranking("Lions 3, Snakes 3")
        league.update_ranking("Tarantulas 3, FC Awesome 1")
        league.print_ranking()
        self.assertEqual(
            "1 Tarantulas 3 pts\n2 Lions 1 pts\n2 Snakes 1 pts\n4 FC Awesome 0 pts\n",
            mock_stdout.getvalue()
        )

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_integration_sample_input(self, mock_stdout):
        league = League()
        league.process_file(filename="sample_input.txt")
        league.print_ranking()
        self.assertEqual(
            "1 Tarantulas 6 pts\n2 Lions 5 pts\n3 FC Awesome 1 pts\n3 Snakes 1 pts\n"
            "5 Grouches 0 pts\n",
            mock_stdout.getvalue()
        )
