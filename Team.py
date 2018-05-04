"""The team class"""

import Player
import numpy as np


class Team:
    def __init__(self, teamNM, team_player_time_dataset):
        self.teamNM = teamNM
        self.players = []
        self.players_chosen_prob = []
        self.team_playing_time = team_player_time_dataset[self.teamNM]["team_playing_time"]

    def add_players(self, team_player_time_dataset, player_performance_dataset):
        for playerNM in team_player_time_dataset[self.teamNM]["players"]:
            player = Player(playerNM, player_performance_dataset)
            player.cal_performance_mean_std()
            player.cal_prob_being_chosen(self.team_playing_time)
            self.players.append(player)

        self.players_chosen_prob = [player.prob_being_chosen for player in self.players]

    def choose_players(self):
        five_player_list = np.random.choice(self.players, size=5, replace=False, p=self.players_chosen_prob)

        return five_player_list

    def estimate_team_performance(self, five_player_list):
        team_performance_mean = sum([player.performance_mean for player in five_player_list])
        team_performance_std = sum([player.performance_std for player in five_player_list])
        team_performance = np.random.normal(loc=team_performance_mean,
                                            scale=team_performance_std,
                                            size=1)
        return team_performance
