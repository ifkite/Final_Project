"""The team class"""

from Player import Player
import numpy as np


class Team:
    def __init__(self, teamNM, team_player_time_dataset):
        """

        :param teamNM: the name of a team
        :param team_player_time_dataset: A dict.
                                         Key: Team name
                                         Value: A dict with formats like
                                               {'players': A 1-D numpy array of the names of players of this tream,
                                                'team_playing_time': the total amount of team playing time in recent matches}
        """
        self.teamNM = teamNM

        # A list of player objects of this team
        self.players = []

        # A list containing each player's probability of being chosen
        self.players_chosen_prob = []

        # team's total amount of playing time in recent matches
        self.team_playing_time = team_player_time_dataset[self.teamNM]["team_playing_time"]

    def add_players(self, team_player_time_dataset, player_performance_dataset):
        """Add all players of this team and update self.players and self.players_chosen_prob

        :param team_player_time_dataset: A dict as described above
        :param player_performance_dataset: A dict.
                                           Key: Player name
                                           Value: A numpy array whose columns are features such as shot and punishment
                                                  of a player, and whose rows represent records of different matches.
        """
        # Create player objects according to this team's roster of player times
        for playerNM in team_player_time_dataset[self.teamNM]["players"]:
            # Create player object
            player = Player(playerNM, player_performance_dataset)

            # Calculate and update mean and std of performance score, and player's probability of being chosen
            player.cal_performance_mean_std()
            player.cal_prob_being_chosen(self.team_playing_time)

            # Add player object and player's probability of being chosen to the list
            self.players.append(player)
            self.players_chosen_prob.append(player.prob_being_chosen)


    def choose_players(self):
        """Choose 5 players according to the players' probabilities of being chosen.
           The choice of 5 players subjects to discrete distribution.

        :return: five_player_list: A list containing 5 player objects that will be chosen to fight for the
                 upcoming match
        """
        five_player_list = np.random.choice(self.players, size=5, replace=False, p=self.players_chosen_prob)

        return five_player_list

    def estimate_team_performance(self, five_player_list):
        """ Team performance score = player1 performance score + ... + player5 performance score
            Assume that players are independent of each other and player performance score subjects to
            normal distribution. Then team performance score also subjects to normal distribution, and
            E(team_performance_score) = sum(E(player_performance_score))
            D(team_perforamce_score) = sum(D(player_performance_score))
            Randomly choose a team performance score from the distribution

        :return team_performance
        """
        team_performance_mean = sum([player.performance_mean for player in five_player_list])
        team_performance_std = sum([player.performance_std for player in five_player_list])
        team_performance = np.random.normal(loc=team_performance_mean,
                                            scale=team_performance_std,
                                            size=1)
        return team_performance
