from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_CG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#SoMi Control Group
    SoMi_CG = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1] #1: unique object, 2: double object
    )
    uniqueObject = models.StringField()


# PAGES
#SoMi Control Group
##Transition Page
class Transition_to_SoMi_CG(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

##Two red apples
class SoMi_CG(Page):
    form_model = 'player'
    form_fields = ['SoMi_CG']

    @staticmethod
    def vars_for_template(player):
        player.uniqueObject = player.participant.objects_treat[player.round_number-1]
        image_unique = player.uniqueObject + ".JPG"

        if player.participant.objects_treat[player.round_number-1][-1:] == 'a':
            image_double = player.participant.objects_treat[player.round_number-1][:-1] + "b.JPG"
        else:
            image_double = player.participant.objects_treat[player.round_number-1][:-1] + "a.JPG"

        return dict(
            image_unique = image_unique,
            image_double = image_double,
        )

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.round_number == 8:
            return 'SoMi_ManipulationCheck'

page_sequence = [
    Transition_to_SoMi_CG,
    SoMi_CG,
]
