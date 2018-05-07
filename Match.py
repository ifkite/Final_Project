"""the match class"""

from Player import Player
from Team import Team
import numpy as np


class Match:

    def __init__(self, teamA, teamB):
        """

        :param teamA: team object
        :param teamB: team object
        """
        self.teamA = teamA
        self.teamB = teamB

    def fight_predict_champion(self):
        """Predict the champion of this match.

        :return: winner: winner team object
        """
        team_vs_list = [self.teamA, self.teamB]

        # For each team, estimate the team performance score and add it to team_performance_list
        team_performance_list = []
        for team in team_vs_list:
            # choose 5 players to fight for the match
            five_player_list = team.choose_players()
            # estimate team performance score and add it to the list
            team_performance = team.estimate_team_performance(five_player_list)
            team_performance_list.append(team_performance)

        # The team with the higher score wins the match
        # If teamA_performace = teamB_performance, then predict again
        teamA_performance = team_performance_list[0][0]
        teamB_performance = team_performance_list[1][0]
        if teamA_performance > teamB_performance:
            winner = self.teamA
            print(self.teamA.teamNM + " VS " + self.teamB.teamNM + ": " + "%.2f VS %.2f"
                  %(teamA_performance, teamB_performance) + ", " + self.teamA.teamNM + " wins!")
        elif teamA_performance < teamB_performance:
            winner = self.teamB
            print(self.teamA.teamNM + " VS " + self.teamB.teamNM + ": " + "%.2f VS %.2f"
                  %(teamA_performance, teamB_performance) + ", " + self.teamB.teamNM + " wins!")
        else:
            self.fight_predict_champion(self)

        return winner


