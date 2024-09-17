from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_Pre'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#SoMi Pre test

##Example 1: Two green M&Ms
    SoMi_Pre_exa = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1] #1: unique object, 2: double object
    )

##Example 2: Two blue M&Ms
    SoMi_Pre_exb = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1]
    )

    SoMi_Pre = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1] #1: unique object, 2: double object
    )

    uniqueObject = models.StringField()


# PAGES
#SoMi Pretest
##Instruction
class SoMi_Pre_introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

##Example 1: Two green M&Ms (always first)
class SoMi_Pre_exa(Page):
    form_model = 'player'
    form_fields = ['SoMi_Pre_exa']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

##Example 2: Two blue M&Ms (always second)
class SoMi_Pre_exb(Page):
    form_model = 'player'
    form_fields = ['SoMi_Pre_exb']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class SoMi_Pre_start(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

###following pages randomized
class SoMi_Pre(Page):
    form_model = 'player'
    form_fields = ['SoMi_Pre']

    @staticmethod
    def vars_for_template(player):
        player.uniqueObject = player.participant.objects_pre[player.round_number-1]
        image_unique = player.uniqueObject + ".JPG"

        if player.participant.objects_pre[player.round_number-1][-1:] == 'a':
            image_double = player.participant.objects_pre[player.round_number-1][:-1] + "b.JPG"
        else:
            image_double = player.participant.objects_pre[player.round_number-1][:-1] + "a.JPG"

        return dict(
            image_unique = image_unique,
            image_double = image_double,
        )

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.round_number == 8:
            return player.participant.treatment

page_sequence = [
    SoMi_Pre_introduction,
    SoMi_Pre_exa,
    SoMi_Pre_exb,
    SoMi_Pre_start,
    SoMi_Pre,
]

