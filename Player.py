"""The player class"""
import numpy as np

class Player:

    def __init__(self, playerNM, player_performance_dataset):
        self.playerNM = playerNM
        self.performance = player_performance_dataset[playerNM]
        self.performance_mean = None
        self.performance_std = None
        self.prob_being_chosen = None

    def cal_performance_mean_std(self):
        weight = [0.6, 0.2, 0.1, 0.1, 0.1, -0.05, -0.05]
        performance_scores = np.sum(self.performance[:, 0:7] * weight, axis=1)
        self.performance_mean = np.mean(performance_scores)
        self.performance_std = np.std(performance_scores)

    def cal_prob_being_chosen(self, team_playing_time):
        player_playing_time = np.sum(self.performance[:, 7])
        self.prob_being_chosen = player_playing_time / team_playing_time
