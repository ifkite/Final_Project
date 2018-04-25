# The player class

class Player:
    def __init__(self, player_id, player_data):
        self.player_id = player_id
        self.player_nm = player_data[player_id]
        self.team = player_data[player_id]
        self.performance_mean = self.cal_performance_mean()
        self.performance_var = self.cal_performance_var()
        self.prob_be_chosen = self.cal_prob_be_chosen()

    def cal_performance_mean(self):
        pass

    def cal_performance_var(self):
        pass

    def cal_prob_be_chosen(self):
        pass
