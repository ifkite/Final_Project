"""
590PR Spring 2018
Final Assignment: Predicting NBA western conference champion of season 2017-2018
Author: Mengyuan Li, Xiang Chen, Yushuo Fan, Ruoqiao Zhang(Thursday)

Purpose:  This program aims to use Monte Carlo Methods to predict NBA western conference champion of season 2017-2018.
          After the execution of Monte Carlo simulation of the match, the team who has the highest winning probability
          (calculated by predicted winning times / simulation times) will be the predicted winner.

Scenario: The match is going on now and has come to the playoff.
          There are 8 teams surviving to compete for the champion.These 8 teams are ranked according to their
          performance in previous matches and we represented them as Team1, Team2,...,Team8 according to their ranks.

According to NBA rule, there are 3 rounds:

The 1st round:
Team1 VS Team8 ===> Winner(1,8)
Team2 VS Team7 ===> Winner(2,7)
Team3 VS Team6 ===> Winner(3,6)
Team4 VS Team5 ===> Winner(4,5)

The 2nd round:
Winner(1,8) VS Winner(4,5) ===> Final_Team1
Winner(2,7) VS Winner(3,6) ===> Final_Team2

The 3rd round:
Final_Team1 VS Final_Team2 ===> Champion

Assumption:
1. Players are independent of each other.
2. Player performance score subjects to normal distribution
3. The longer a player plays in recent matches, the higher the probability that he will be chose to play
the upcoming match.
4. After the simulation, the team who has highest probability of winning, namely who wins the most times in
the simulation, will be the predicted winner.

*** Package Version: numpy 1.14.2. (Please do not use versions below numpy 1.14) ***
"""

from data_tools import read_dataset
import numpy as np
import collections
from Player import Player
from Team import Team
from Match import Match

# Process the raw dataset
player_performance_dataset, team_player_time_dataset = read_dataset("nba_data.csv")

# The rank of teams at the beginning of the 1st round of the playoff
# Key: rank; Value: Team name
rank_teamNM_dict = {1: "Rockets", 2: "Warriors", 3: "Trailblazers", 4: "Thunders", 5: "Jazz", 6: "Pelicans", 7: "Spurs", 8: "Timberwolves"}

# Create rank_teamOBJ_dict based on rank_teamNM_dict.
# Key: rank; Value: Team object
rank_teamOBJ_dict = {}
for rank, teamNM in rank_teamNM_dict.items():
    teamOBJ = Team(teamNM, team_player_time_dataset)
    # Add players for each team
    teamOBJ.add_players(team_player_time_dataset, player_performance_dataset)
    rank_teamOBJ_dict[rank] = teamOBJ

# Create battle teams according to NBA game rule and apply Monte Carlo Simulation
simulation_times = 15000
champion_list = []
for i in range(simulation_times):
    # A list containing the winner team name of each simulation
    # First round of the game
    print("First Round: ")
    winner_1_8 = Match(rank_teamOBJ_dict[1], rank_teamOBJ_dict[8]).fight_predict_champion()
    winner_2_7 = Match(rank_teamOBJ_dict[2], rank_teamOBJ_dict[7]).fight_predict_champion()
    winner_3_6 = Match(rank_teamOBJ_dict[3], rank_teamOBJ_dict[6]).fight_predict_champion()
    winner_4_5 = Match(rank_teamOBJ_dict[4], rank_teamOBJ_dict[5]).fight_predict_champion()
    print()

    # Second round of the game
    print("Second Round: ")
    winner18_45 = Match(winner_1_8, winner_4_5).fight_predict_champion()
    winner27_36 = Match(winner_2_7, winner_3_6).fight_predict_champion()
    print()

    # The last round
    print("Last Round: ")
    champion = Match(winner18_45, winner27_36).fight_predict_champion()
    print()

    print("The Champion of western conference is " + champion.teamNM)
    print("=============================================================")
    champion_list.append(champion.teamNM)


# Calulate winning probability for each team.
# champion_count_dict: Key: name of champion; Value: winning times
champion_count_dict = dict(collections.Counter(champion_list))
team_win_prob_dict = {}
for teamNM, win_times in champion_count_dict.items():
    team_win_prob = win_times / simulation_times
    team_win_prob_dict[teamNM] = team_win_prob

# Add those teams who does not get champion at any simulation iteration
# And set their winning probabilities to 0
for teamNM in rank_teamNM_dict.values():
    if teamNM not in team_win_prob_dict.keys():
        team_win_prob_dict[teamNM] = 0.00

# Sort team_win_prob_dict according to its values, with reverse=True
sorted_team_win_prob_list = sorted(team_win_prob_dict.items(), key=lambda x: x[1], reverse=True)
for team_win_prob_tuple in sorted_team_win_prob_list:
    print("Team name: " + team_win_prob_tuple[0] + ": " + "%.2f percent winning probability." %(team_win_prob_tuple[1] * 100))

