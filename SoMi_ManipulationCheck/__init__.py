from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_MC'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#SoMi Manipulation Check

##Manipulation Check 1: Two green M&Ms
    MC_exa = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1]  # 1: unique object, 2: double object
    )

##Manipulation Check 2: Two blue M&Ms
    MC_exb = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1]
    )


# PAGES
#SoMi Control Group
##Transition Page
class Transition_to_SoMi_MC(Page):
    pass

##Example 1: Two green M&Ms (always first)
class MC_exa(Page):
    form_model = 'player'
    form_fields = ['MC_exa']

##Example 2: Two blue M&Ms (always second)
class MC_exb(Page):
    form_model = 'player'
    form_fields = ['MC_exb']

page_sequence = [Transition_to_SoMi_MC,
                 MC_exa,
                 MC_exb
                 ]
