"""
Wimbledon
Estimate: 25 minutes
Actual: 31 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Prints Wimbledon winners, and country of Wimbledon winners"""
    lines = extract_data(FILENAME)
    player_to_wins, winning_countries = extract_player_country_results(lines)
    print_results(player_to_wins, winning_countries)


def extract_data(filename):
    """Extract data from input file"""
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove data structure line
        lines = [line.split(',') for line in in_file]
        return lines


def extract_player_country_results(lines):
    """Extract set of winning players countries, and dictionary of winners names and number of wins"""
    yearly_winning_players = [line[2] for line in lines]
    player_to_wins = {}
    for player in yearly_winning_players:
        try:
            player_to_wins[player] = player_to_wins[player] + 1
        except KeyError:
            player_to_wins[player] = 1
    winning_countries = sorted({line[1] for line in lines})
    return player_to_wins, winning_countries


def print_results(player_to_wins, winning_countries):
    """Print winners, how many wins, and which countries have won"""
    for player, wins in player_to_wins.items():
        print(f"{player} {wins}")
    print()
    print(f"These {len(winning_countries)} have won Wimbledon:")
    print(', '.join(winning_countries))


main()
