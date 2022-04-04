###
### Author: Simran Sall
### Course: CSc 110
### Description: This program considers a text file that includes the
###              documents of a game and provides a summary of that game.
###              The program will print out which team won the game, how
###              many points were scored by each team, as well as the first
###              scorer and last scorer of the game.
###

def filing_info(name, score_1, score_2, team_1, team_2, total_players):
    '''This function evaluates the information in the file. Team names,
    total amount of players, last scorer, and the scores for each team are all
    evaluated.
    name: gets the name of the file that the user wants to be opened
    score_1: team one's score is set to zero and updates during the for loop (line 31)
        based on which team scored
    score_2: team two's score is set to zero and updates during the for loop (line 31)
        based on which team scored
    team_1: gets the name of the first team
    team_2: gets the name of the second team
    total_players: this value is set to zero and updates during the for loop (line 31)
        based on the amount of players who scored
    '''
    # open the user's game log file
    game_log_file = open(name, 'r')
    players = []
    points = []
    last_scorer = []
    # go through each line of the file
    for line in game_log_file:
        # split each line to separate values of team, player, and points
        lst = line.split()
        # get the names of each team
        if team_1 == '':
            team_1 = lst[0]
        if team_2 == '' and team_1 != '' and team_1 != lst[0]:
            team_2 = lst[0]
        # calculate the last scorer of the game
        last_player = lst[1]
        # calculate the total amount of players who scored
        player = lst[1]
        if player not in players:
            players.append(player)
            total_players += 1
        else:
            total_players += 0
        # calculate score for each team
        if lst[0] == team_1:
            score_1 += int(lst[2])
        else:
            score_2 += int(lst[2])
    # return all the info so that they can be reflected in game output
    list = [total_players, score_1, score_2, team_1, team_2, players, last_player]
    return list

def game_output(name,score_1,score_2,team_1,team_2,total_players,players,last_player):
    '''This function evaluates the returned values from the filing_info
    function and uses the returned value to print out the statistics of
    the game.
    name: gets the name of the file that the user wants to be opened
    score_1: returned final value of team one's score from the filing_info function.
    score_2: returned final value of team two's score from the filing_info function.
    team_1: gets the name of the first team
    team_2: gets the name of the second team
    total_players: returned final value of the total amount of players from the
        filing_info function
    players: evaluates the list of all the players who scored.
    last_player: returned the final player from all the players who scored.
    '''
    game_log_file = open(name, 'r')
    for line in game_log_file:
        lst = line.split()
    print()
    # print which team won the game
    if score_1 > score_2:
        print(team_1, 'won!')
    else:
        print(team_2, 'won!')
    # print other stats of the game
    print(team_1, 'scored', score_1, 'points.')
    print(team_2, 'scored', score_2, 'points.')
    print(total_players, 'players scored.')
    print(players[0], 'scored first.')
    print(last_player, 'scored last.')

def main():
    name = input('enter gamelog file name: ')
    team_1 = ''
    team_2 = ''
    # defining the scores and total players at 0 before it iterates through the list
    score_1 = 0
    score_2 = 0
    total_players = 0
    # set parameters of filing_info function equal to a variable
    # so that the values can update each time
    info = filing_info(name, score_1, score_2, team_1, team_2, total_players)
    game_output(name, info[1], info[2], info[3], info[4], info[0], info[5], info[6])

main()