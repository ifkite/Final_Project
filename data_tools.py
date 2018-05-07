"""
This module is used to process the raw NBA data
As for the detailed description of dataset, please refer to "data_description.pdf "
"""

import numpy as np


def read_dataset(input_file):
    """Given the input file (NBA data), read and process it.

    :param input_file: The file path
    :return

    player_performance_dataset: A dict.
                                Key: Player name
                                Value: A numpy array whose columns are features such as shot and punishment of a player,
                                       and whose rows represent records of different matches.

    team_player_time_dataset: A dict.
                              Key: Team name
                              Value: A dict with formats like
                                     {'players': A 1-D numpy array of the names of players of this tream,
                                      'team_playing_time': the total amount of team playing time in recent matches}
    """
    # Extract player performance data
    performance_dataset = np.genfromtxt(input_file, dtype=np.float, delimiter=",",
                                        skip_header=1, usecols=(2, 3, 4, 5, 6, 7, 8, 9))
    # Extract player names data
    playerNM_dataset = np.genfromtxt(input_file, dtype=str, delimiter=",",
                                     skip_header=1, usecols=1)
    # Extract team names data
    team_dataset = np.genfromtxt(input_file, dtype=str, delimiter=",",
                                 skip_header=1, usecols=10)

    # Match player's performances data with player's name to create player_performance_dataset
    playerNM_unique = np.unique(playerNM_dataset)
    player_performance_dataset = {}
    for player in playerNM_unique:
        performance = performance_dataset[np.where(playerNM_dataset == player)]
        player_performance_dataset[player] = performance

    # Match roster of players, total amount of team playing time with team name to create team_player_time_dataset
    teamNM_unique = np.unique(team_dataset)
    team_player_time_dataset = {}
    for team in teamNM_unique:
        players = np.unique(playerNM_dataset[np.where(team_dataset == team)])
        team_playing_time = np.sum(performance_dataset[np.where(team_dataset == team)][:, 7])
        team_player_time_dataset[team] = {"players": players, "team_playing_time": team_playing_time}

    return player_performance_dataset, team_player_time_dataset
