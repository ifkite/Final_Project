"""This module is used to process the data files of players and teams"""

import numpy as np


def read_dataset(input_file):
    performance_dataset = np.genfromtxt("nba_data.csv", dtype=np.float, delimiter=",",
                                        skip_header=1, usecols=(2, 3, 4, 5, 6, 7, 8, 9))
    playerNM_dataset = np.genfromtxt("nba_data.csv", dtype=str, delimiter=",",
                                     skip_header=1, usecols=1)
    team_dataset = np.genfromtxt("nba_data.csv", dtype=str, delimiter=",",
                                 skip_header=1, usecols=10)

    playerNM_unique = np.unique(playerNM_dataset)
    player_performance_dataset = {}
    for player in playerNM_unique:
        performance = performance_dataset[np.where(playerNM_dataset == player)]
        player_performance_dataset[player] = performance

    teamNM_unique = np.unique(team_dataset)
    team_player_time_dataset = {}
    for team in teamNM_unique:
        players = np.unique(playerNM_dataset[np.where(team_dataset == team)])
        team_playing_time = np.sum(performance_dataset[np.where(team_dataset == team)][:, 7])
        team_player_time_dataset[team] = {"players": players, "team_playing_time": team_playing_time}

    return player_performance_dataset, team_player_time_dataset
