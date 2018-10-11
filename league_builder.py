"""
Python Web Development Techdegree
Project 2 - Build a Soccer League
--------------------------------
"""
import csv


# read soccerplayers.csv into a list of dictionaries called all_players
def csv_to_dicts(csv_filename):
    with open(csv_filename, newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        rows = list(file_reader)
        all_players = []
        headers = rows.pop(0)
        player_list = rows
        for player in player_list:
            all_players.append({
                label: player for label, player in zip(headers, player)
            })
    return all_players


# check that teams have an equal number of exp and total players
def even_up(exp, inexp):
    extra_exp = []
    extra_inexp = []
    if len(exp) % 3 != 0:
        for player in range(0, len(exp) % 3):
            extra_exp.append(exp.pop())
    if len(inexp) % 3 != 0:
        for player in range(0, len(inexp) % 3):
            extra_exp.append(exp.pop())
    if extra_exp or extra_inexp:
        return extra_exp + extra_inexp
    else:
        pass


# sort all_players into a list of dictionaries, experienced_players first
def split_list(file):
    exp_players, inexp_players = [], []
    all_players = csv_to_dicts(file)
    exp_players = [
        player for player in all_players
        if player['Soccer Experience'].upper() == 'YES'
    ]
    inexp_players = [
        player for player in all_players
        if player['Soccer Experience'].upper() == 'NO'
    ]
    extra_players = even_up(exp_players, inexp_players)
    all_players = exp_players + inexp_players
    return all_players, extra_players


# split all_players (sorted) into the 3 teams, Dragons, Sharks, Raptors
def make_teams(players):
    dragons, sharks, raptors = [], [], []
    while players:
        dragons.append(players.pop())
        sharks.append(players.pop())
        raptors.append(players.pop())
    return dragons, sharks, raptors


# create a string out of each team for use in message
def make_team_string(team):
    team_players = ""
    if team:
        for player in team:
            team_players += ", ".join([
                player['Name'],
                player['Soccer Experience'],
                player['Guardian Name(s)'],
                '\n',
            ])
    team = team_players
    return team


# create teams.txt with a list of which players are on which team
def create_league_roster(dragons, sharks, raptors, extra):
    message = ""
    players = ""
    dragon_players, shark_players, raptor_players = "", "", ""
    if extra:
        message += '''
WARNING!
Due to an uneven number of players, some haven't been assigned a team.
Please manually assign the following players to a team:

{}
        '''.format(extra)
    message += '''
Here are this years teams:

Dragons:
{}
{}


Sharks:
{}
{}


Raptors:
{}
{}
    '''.format("=" * 15, dragons, "=" * 15, sharks, "=" * 15, raptors)
    with open('teams.txt', 'a') as file:
        file.write(message)


# create <player's_name>.txt for each player
def create_dragon_letters(dragons, sharks, raptors):
    team, guardian, name, letter_name = "", "", "", ""
    team_names = ["Dragons", "Sharks", "Raptors"]
    for team_name in team_names:
        if team_name == "Dragons":
            team = dragons
        elif team_name == "Sharks":
            team = sharks
        elif team_name == "Raptors":
            team = raptors
        for player in team:
            team = team_name
            guardian = player['Guardian Name(s)']
            name = player['Name']
            letter_name = player['Name'].lower()
            letter_name = letter_name.replace(' ', '_') + '.txt'
            message = '''
    Dear {},

    I am plesed to inform you that {} will be playing for the {} this year.

    The first practice will be November 1 at 4:00pm.

    Sincerely,
    Soccer League Coordinator
            '''.format(guardian, name, team)
            with open(letter_name, 'a') as file:
                file.write(message)


if __name__ == '__main__':
    all_players, extra = split_list('soccer_players.csv')
    dragons, sharks, raptors = make_teams(all_players)
    dragons_string = make_team_string(dragons)
    sharks_string = make_team_string(sharks)
    raptors_string = make_team_string(raptors)
    extra_string = make_team_string(extra)
    create_league_roster(
        dragons_string,
        sharks_string,
        raptors_string,
        extra_string,)
    create_dragon_letters(dragons, sharks, raptors)
