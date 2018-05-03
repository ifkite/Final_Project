# Running Monte Carlo simulation to predict the final champion
from data_tools import read_dataset
import numpy as np
import collections
import Player
import Team
import Match

player_performance_dataset, team_player_time_dataset = read_dataset("nba_data.csv")

rank_teamNM_dict = {1: "A_NM", 2: "B_NM", 3: "C_NM", 4: "D_NM", 5: "E_NM", 6: "F_NM", 7: "G_NM", 8: "H_NM"}

# Create teams and add players for each team
rank_teamOBJ_dict = {}
for rank, teamNM in rank_teamNM_dict.items():
    teamOBJ = Team(teamNM, team_player_time_dataset)
    teamOBJ.add_players()
    rank_teamOBJ_dict[rank] = teamOBJ

# Apply Monte Carlo Simulation (100 simulation times)
# Create battle teams according to NBA game rules
simulation_times = 100
for i in range(simulation_times):
    champion_list = []
    # First round of the game
    winner_1_8 = Match(rank_teamOBJ_dict[1], rank_teamOBJ_dict[8]).fight_predict_champion()
    winner_2_7 = Match(rank_teamOBJ_dict[2], rank_teamOBJ_dict[7]).fight_predict_champion()
    winner_3_6 = Match(rank_teamOBJ_dict[3], rank_teamOBJ_dict[6]).fight_predict_champion()
    winner_4_5 = Match(rank_teamOBJ_dict[4], rank_teamOBJ_dict[5]).fight_predict_champion()

    # Second round of the game
    winner18_45 = Match(winner_1_8, winner_4_5).fight_predict_champion()
    winner27_36 = Match(winner_2_7, winner_3_6).fight_predict_champion()

    # The last round
    champion = Match(winner18_45, winner27_36).fight_predict_champion()

    print("The Champion of western conference is" + champion.teamNM)
    champion_list.append(champion.teamNM)

# Calulate probability of winning for teams
champion_count_dict = dict(collections.Counter(champion_list))
team_win_prob_dict = {}
for teamNM, win_times in champion_count_dict.items():
    team_win_prob = win_times / simulation_times
    team_win_prob_dict[teamNM] = team_win_prob

# Add those teams who does not get champion at any simulation iteration
# And set their winning probabilities to 0
for teamNM in rank_teamNM_dict.values():
    if teamNM not in team_win_prob_dict.keys():
        team_win_prob_dict[teamNM] = 0

# Sort team_win_prob_dict according to its values, with reverse=True
sorted_team_win_prob_list = sorted(team_win_prob_dict.items(), key=lambda x: x[1], reverse=True)
for team_win_prob_tuple in sorted_team_win_prob_list:
    print("Team name: " + team_win_prob_tuple[0] + ": " + "%.2f winning probability." % (team_win_prob_tuple[1] * 100))
