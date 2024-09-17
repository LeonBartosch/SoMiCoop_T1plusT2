
from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'closing_part'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    payout_part_1 = models.CurrencyField()
    payout_part_1_who = models.StringField()
    pgg_payoff = models.CurrencyField()
    SVO_payoff = models.CurrencyField()
    SVO_payoff_who = models.StringField()
    T1_SVO_payoff = models.CurrencyField()
    T1_SVO_payoff_who = models.StringField()
    payout_part_2 = models.CurrencyField()
    task_chosen = models.StringField()
    final_payoff = models.CurrencyField()

    #feedback field
    feedback = models.LongStringField(blank=True, label="If you would like to give us feedback or have any comments on "
                                                        "this study, please let us know below:")
    time_end = models.StringField()

# Grouping
def group_by_arrival_time_method(subsession, waiting_players):
    if len(waiting_players) >= 8:
        print('about to create a group')

        #PGG Payoff Group 1:
        contributions = waiting_players[0].participant.PGG_contribution + waiting_players[1].participant.PGG_contribution + waiting_players[2].participant.PGG_contribution + waiting_players[3].participant.PGG_contribution
        group_1 = [waiting_players[0], waiting_players[1], waiting_players[2], waiting_players[3]]
        for p in group_1:
            p.pgg_payoff = (cu(600) - p.participant.PGG_contribution + 2*contributions/4)

        #PGG Payoff Group 2:
        contributions = waiting_players[4].participant.PGG_contribution + waiting_players[5].participant.PGG_contribution + waiting_players[6].participant.PGG_contribution + waiting_players[7].participant.PGG_contribution
        group_2 = [waiting_players[4], waiting_players[5], waiting_players[6], waiting_players[7]]
        for p in group_2:
            p.pgg_payoff = (cu(600) - p.participant.PGG_contribution + 2*contributions/4)

        #SVO Payoff
        who = ["you", "another participant"]

        for index in range(4):
            payoff_players = random.choice([0, 1])
            waiting_players[index].SVO_payoff_who = who[payoff_players]
            waiting_players[index+4].SVO_payoff_who = who[1-payoff_players]
            if payoff_players == 0:
                waiting_players[index].SVO_payoff = waiting_players[index].participant.SVO_payoff_self
                waiting_players[index+4].SVO_payoff = waiting_players[index].participant.SVO_payoff_other
            else:
                waiting_players[index].SVO_payoff = waiting_players[index+4].participant.SVO_payoff_other
                waiting_players[index+4].SVO_payoff = waiting_players[index+4].participant.SVO_payoff_self

        for index in range(4):
            payoff_players = random.choice([0, 1])
            waiting_players[index].T1_SVO_payoff_who = who[payoff_players]
            waiting_players[7-index].T1_SVO_payoff_who = who[1-payoff_players]
            if payoff_players == 0:
                waiting_players[index].T1_SVO_payoff = cu(waiting_players[index].participant.T1_SVO_payoff_self)
                waiting_players[7-index].T1_SVO_payoff = cu(waiting_players[index].participant.T1_SVO_payoff_other)
            else:
                waiting_players[index].T1_SVO_payoff = cu(waiting_players[7-index].participant.T1_SVO_payoff_other)
                waiting_players[7-index].T1_SVO_payoff = cu(waiting_players[7-index].participant.T1_SVO_payoff_self)

        return [waiting_players[0], waiting_players[1], waiting_players[2], waiting_players[3], waiting_players[4], waiting_players[5], waiting_players[6], waiting_players[7]]
    else:
        print('not enough players yet to create a group')


# PAGES
class PayoutWaitPage(WaitPage):
    group_by_arrival_time = True

class Payout(Page):
    @staticmethod
    def vars_for_template(player):
        player.payout_part_1 = player.T1_SVO_payoff#.to_real_world_currency(player.session)
        player.payout_part_1_who = player.T1_SVO_payoff_who

        player.task_chosen = random.choice(["SVO", "PGG"])
        if player.task_chosen == "SVO":
            player.payout_part_2 = player.SVO_payoff#.to_real_world_currency(player.session)
        if player.task_chosen == "PGG":
            player.payout_part_2 = player.pgg_payoff#.to_real_world_currency(player.session)

        player.final_payoff = (player.payout_part_1 + player.payout_part_2)

        pgg_contribution = cu(player.participant.PGG_contribution)#.to_real_world_currency(player.session)
        money_kept = cu(600)-pgg_contribution
        player2_contribution = cu(player.get_others_in_group()[0].participant.PGG_contribution)#.to_real_world_currency(player.session)
        player3_contribution = cu(player.get_others_in_group()[1].participant.PGG_contribution)#.to_real_world_currency(player.session)
        player4_contribution = cu(player.get_others_in_group()[2].participant.PGG_contribution)#.to_real_world_currency(player.session)

        return dict(
            payout_part_1 = player.payout_part_1.to_real_world_currency(player.session),
            SVO_payoff = player.SVO_payoff.to_real_world_currency(player.session),
            pgg_payoff = player.pgg_payoff.to_real_world_currency(player.session),
            final_payoff = player.final_payoff.to_real_world_currency(player.session),
            pgg_contribution=pgg_contribution.to_real_world_currency(player.session),
            money_kept=money_kept.to_real_world_currency(player.session),
            player2_contribution=player2_contribution.to_real_world_currency(player.session),
            player3_contribution=player3_contribution.to_real_world_currency(player.session),
            player4_contribution=player4_contribution.to_real_world_currency(player.session),
        )

class Debriefing(Page):
    form_model = 'player'
    form_fields = ['feedback']
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Close_window(Page):
    pass

page_sequence = [PayoutWaitPage, Payout, Debriefing, Close_window]
