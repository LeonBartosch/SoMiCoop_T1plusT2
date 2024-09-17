from otree.api import *
import csv



doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SVO_PGG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#Public Goods Game (PGG)
    ##PGG comprehension check
    PGG_comprehension1 = models.IntegerField(max_length=0, min_length=1000,
                                         label="How much do you need to contribute (in cents) to get the highest payout for the entire group?")

    PGG_comprehension2 = models.IntegerField(max_length=0, min_length=1000,
                                         label="How much do you need to contribute (in cents) to maximize your personal "
                                               "income? ")
    PGG_comprehensionCount = models.IntegerField(initial=0, blank=True)
    ##PGG task
    PGG_amount = models.IntegerField()

    #SVO task
    svo_choice_1 = models.IntegerField(blank=True)
    svo_choice_2 = models.IntegerField(blank=True)
    svo_choice_3 = models.IntegerField(blank=True)
    svo_choice_4 = models.IntegerField(blank=True)
    svo_choice_5 = models.IntegerField(blank=True)
    svo_choice_6 = models.IntegerField(blank=True)
    svo_choice_7 = models.IntegerField(blank=True)
    svo_choice_8 = models.IntegerField(blank=True)
    svo_choice_9 = models.IntegerField(blank=True)
    svo_choice_10 = models.IntegerField(blank=True)
    svo_choice_11 = models.IntegerField(blank=True)
    svo_choice_12 = models.IntegerField(blank=True)
    svo_choice_13 = models.IntegerField(blank=True)
    svo_choice_14 = models.IntegerField(blank=True)
    svo_choice_15 = models.IntegerField(blank=True)
    svo_tot_ego = models.IntegerField()
    svo_tot_alter = models.IntegerField()
    svo_mean_ego = models.FloatField()
    svo_mean_alter = models.FloatField()
    svo_ratio = models.FloatField()
    svo_angle = models.FloatField()
    svo_check_pass = models.BooleanField(
        initial=False
    )
    svo_random_item = models.IntegerField(blank=True)
    svo_random_self = models.IntegerField(blank=True)
    svo_random_other = models.IntegerField(blank=True)


# Pages Public Goods Game (PGG)
class Transition_to_PGG(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.PGG_first and player.round_number == 1) or (not player.participant.PGG_first and player.round_number == 2)

class PGG_instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.PGG_first and player.round_number == 1) or (not player.participant.PGG_first and player.round_number == 2)

class PGG_transition_to_comprehension_check(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.PGG_first and player.round_number == 1) or (not player.participant.PGG_first and player.round_number == 2)

class PGG_comprehension_check(Page):
    form_model = 'player'
    form_fields = ['PGG_comprehension1', 'PGG_comprehension2', 'PGG_comprehensionCount']

    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.PGG_first and player.round_number == 1) or (not player.participant.PGG_first and player.round_number == 2)

class PGG_task(Page):
    form_model = "player"
    form_fields = ["PGG_amount"]

    @staticmethod
    def is_displayed(player: Player):
        return (player.participant.PGG_first and player.round_number == 1) or (not player.participant.PGG_first and player.round_number == 2)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.PGG_contribution = player.PGG_amount


# Pages SVO
class Transition_to_SVO(Page):
    def before_next_page(player, timeout_happened):
        with open(player.session.config['svo_file']) as f:
            r = csv.reader(f, delimiter=";")
            c = [line for line in r]
            h = c[0]
            d = [dict(zip(h, l)) for l in c[1:]]
            for row in r:
                print(row)
            player.session.vars["SVO_Fullx11"] = [
                [[r, l["A" + str(i + 1)], l["B" + str(i + 1)]] for i in range(int(9))]
                for r, l in enumerate(d)]
        import datetime
       # player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def is_displayed(player: Player):
        return (not player.participant.PGG_first and player.round_number == 1) or (player.participant.PGG_first and player.round_number == 2)

class SVO_items(Page):
    form_model = 'player'
    form_fields = ["svo_choice_1", "svo_choice_2", "svo_choice_3", "svo_choice_4", "svo_choice_5", "svo_choice_6", "svo_choice_7", "svo_choice_8", "svo_choice_9", "svo_choice_10", "svo_choice_11", "svo_choice_12", "svo_choice_13", "svo_choice_14", "svo_choice_15", "svo_tot_ego", "svo_tot_alter", "svo_mean_ego", "svo_mean_alter", "svo_ratio", "svo_angle", "svo_random_self", "svo_random_other", "svo_random_item"]

    @staticmethod
    def vars_for_template(player):
        SVO = player.session.vars["SVO_Fullx11"]
        return dict(
            SVO = SVO
        )

    @staticmethod
    def js_vars(player):
        SVO = player.session.vars["SVO_Fullx11"]
        return dict(
            SVO=SVO
        )

    @staticmethod
    def is_displayed(player: Player):
        return (not player.participant.PGG_first and player.round_number == 1) or (player.participant.PGG_first and player.round_number == 2)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.SVO_payoff_self = player.svo_random_self
        player.participant.SVO_payoff_other = player.svo_random_other

page_sequence = [
    Transition_to_PGG,
    PGG_instructions,
    PGG_transition_to_comprehension_check,
    PGG_comprehension_check,
    PGG_task,
    Transition_to_SVO,
    SVO_items
]