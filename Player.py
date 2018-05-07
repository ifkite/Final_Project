"""
The player class
"""

import numpy as np

class Player:

    def __init__(self, playerNM, player_performance_dataset):
        """

        :param playerNM: the name of a player
        :param player_performance_dataset:  A dict.
                                            Key: Player name
                                            Value: A numpy array whose columns are features such as shot and punishment
                                                   of a player, and whose rows represent records of different matches.
        """
        self.playerNM = playerNM
        self.performance = player_performance_dataset[playerNM]

        # The mean and standard deviation of player's performance scores of recent matches
        self.performance_mean = None
        self.performance_std = None

        # The probability that a player will be chosen to fight for the upcoming match
        self.prob_being_chosen = None

    def cal_performance_mean_std(self):
        """ player performance score = w1 * feature1 + w2 * feature2 + ... + w7 * feature7
            Weights are assigned to measure how much contribution a feature makes to a player's comprehensive performance,
            and sum(weights) = 1, negative weights mean the relevant features are punishments of a player.
        """
        # Assign weights subjectively based on experience
        weight = [0.4, 0.3, 0.3, 0.1, 0.1, -0.15, -0.05]

        # Calculate player performance score for each match
        performance_scores = np.sum(self.performance[:, 0:7] * weight, axis=1)

        # Calculate the mean and std of player performance scores in recent matches
        self.performance_mean = np.mean(performance_scores)
        self.performance_std = np.std(performance_scores)

    def cal_prob_being_chosen(self, team_playing_time):
        """player's probability of being chosen = player's total playing time / team's total playing time
           The longer a player playes in recent matches, the higher the probability that he will be chosen
           to fight for the upcoming matches.

        :param team_playing_time: total amount of the team's playing time in recent matches.
        """
        # Calculate player's total playing time
        player_playing_time = np.sum(self.performance[:, 7])
        self.prob_being_chosen = player_playing_time / team_playing_time
