from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_EG3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    SoMiEG3 = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1]  # 1: unique object, 2: double object
    )
    uniqueObject = models.StringField()

# PAGES
class SoMi_EG3_introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class SoMi_EG3(Page):
    form_model = 'player'
    form_fields = ['SoMiEG3']

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
    SoMi_EG3_introduction,
    SoMi_EG3
]
