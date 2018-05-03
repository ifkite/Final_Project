"""the match class"""

import Player
import Team
import numpy as np


class Match:

    def __init__(self, teamA, teamB):
        self.teamA = teamA  # team object
        self.teamB = teamB

    def fight_predict_champion(self):
        team_vs_list = [self.teamA, self.teamB]
        team_performance_list = []
        for team in team_vs_list:
            five_player_list = team.choose_players()
            team_performance = team.estimate_team_performance(five_player_list)
            team_performance_list.append(team_performance)

        teamA_performance = team_performance_list[0]
        teamB_performance = team_performance_list[1]
        if teamA_performance > teamB_performance:
            winner = self.teamA
            print(self.teamA.teamNM + "VS" + self.teamB.teamNM + ": " + "%.2f : %.2f" + "," + self.teamA.teamNM + "wins!"
                  %(teamA_performance, teamB_performance))
        elif teamA_performance < teamB_performance:
            winner = self.teamB
            print(self.teamA.teamNM + "VS" + self.teamB.teamNM + ": " + "%.2f : %.2f" + "," + self.teamB.teamNM + "wins!"
                  %(teamA_performance, teamB_performance))
        else:
            self.fight_predict_champion(self)

        return winner


