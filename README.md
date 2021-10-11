# League Ranking
**A League ranking application**
---

Winning teams get 3 points for each game, drawing teams get 1 point and a losing team get 0 points.

## Requirements

Tested with:

* Python: 3.6, 3.7, 3.8, 3.9

## Installation

1. Install python 3.6+.
2. git clone git@github.com:cblignaut/leagueranking.git
3. Go to root leagueranking directory

## Usage

### Adding games to the league manually:
1. Run: `python.main.py`
2. Add games in the following format: `[Team 1] [Team 1 score], [Team 2] [Team 2 score]`
3. To quit type `q`

### Process a game score file:
1. The file need to be in the correct format. (See the sample_input.txt file)
2. To process a file run: `python main.py -f sample_input.txt`

## Test

1. Install all python versions: 3.6, 3.7, 3.8, 3.9
2. Install test requirements with: `pip install -r requirements_test.txt`
3. Run tests with `tox`

## Contribution

Please create an issue [New Issue](https://github.com/cblignaut/leagueranking/issues/new)

## License

See LICENSE file for more information.
