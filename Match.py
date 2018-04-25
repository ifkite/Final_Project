# the match class

class Match:

    def __init__(self, team_nm, team_data):
        self.team_nm = team_nm
        self.team_player_list = self.get_player_list()
        self.team_init_rank = team_data[team_nm]

    def get_player_list(self):
        pass

    def choose_player(self, team_player_list):
        pass

    def pred_team_performance(self, chosen_players):
        pass
