from optparse import OptionParser

from leagueranking.leagueranking import League


def main():
    print()
    print("--------------------League-Ranking-------------------")
    print()
    print("Welcome to League Ranking v1.00!")
    print()
    parser = OptionParser()
    parser.add_option(
        "-f", "--file", dest="filename",
        help="File to input", metavar="FILE"
    )
    (options, args) = parser.parse_args()
    if options.filename:
        print(f"The file {options.filename} was processed successfully:")
        print()
        print("Final League rankings:")
        league = League()
        league.process_file(filename=options.filename)
        league.print_ranking()
        print()
    else:
        print("Please add league game scores in the following format:")
        print("[Team 1] [Team 1 score], [Team 2] [Team 2 score]")
        print("For example: 'Lions 3, Snakes 3'")
        print()
        print("Or rerun the program with a file option -f [filename]")
        print("For example: 'python main.py -f sample_input.txt'")
        print()
        new_score = ""
        league = League()
        while new_score != "q":
            new_score = input("Please add a league game score or enter 'q' to quit:\n")
            league.update_ranking(new_score)
            print()
            print(f"{'Current' if new_score != 'q' else 'Final'} League rankings:")
            league.print_ranking()
            print()
    print("----------------------Thank-You----------------------")


main()
