import fileinput
import re


class League:
    def __init__(self):
        self.ranking = dict()

    @staticmethod
    def extract_score(team_score: str) -> dict:
        """
        Extract score from text.
        :param team_score: A string with the team name and score.
        :return: Dictionary with the team and score.
        """
        score_tuple = re.findall(r"(.+) (\d+)", team_score)
        if score_tuple:
            return {
                "team": score_tuple[0][0], "score": int(score_tuple[0][1])
            }
        else:
            return {}

    def update_ranking(self, line: str):
        """
        Updates league ranking with game score line
        :param line: Game score line in [Team 1] [Team 1 score], [Team 2] [Team 2 score] format.
        """
        scores = []
        team_1_score, team_2_score = 0, 0
        for team in line.split(","):
            league_score = self.extract_score(team)
            if league_score:
                scores.append(league_score)
        if len(scores) == 2:
            if scores[0]["score"] == scores[1]["score"]:
                team_1_score = 1
                team_2_score = 1
            elif scores[0]["score"] > scores[1]["score"]:
                team_1_score = 3
            else:
                team_2_score = 3
            team_1 = scores[0]["team"].strip()
            team_2 = scores[1]["team"].strip()
            self.ranking[team_1] = self.ranking.get(team_1, 0) + team_1_score
            self.ranking[team_2] = self.ranking.get(team_2, 0) + team_2_score

    def print_ranking(self):
        """
        Prints out league ranking with places.
        """
        last_score, rank, duplicate_rank = 0, 0, 0
        for team, score in sorted(self.ranking.items(), key=lambda x: (-x[1], x[0])):
            if last_score == score:
                duplicate_rank += 1
            else:
                if duplicate_rank:
                    rank += duplicate_rank
                    duplicate_rank = 0
                rank += 1
            print(f"{rank} {team} {score} pts")
            last_score = score

    def process_file(self, filename: str = None):
        """
        Process file and update league rankings.
        :param filename: Filename and location of file to process
        """
        if filename:
            for line in fileinput.input(files=filename):
                self.update_ranking(line)

