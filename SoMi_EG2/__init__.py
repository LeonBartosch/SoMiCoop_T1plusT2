from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_EG2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
# SoMi Experimental Group 2
    ###Choice other person
    SoMiEG2_out = models.IntegerField(
        choices=[2, 2, 1],  # 1: unique object, 2: double object
        blank=True
    )

    ###SoMi
    SoMiEG2 = models.IntegerField(
        label="Which of the remaining objects do you choose? The other person chose the marked object.",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1]  # 1: unique object, 2: double object
    )

    ###Reaction hostile vs. kind
    SoMiEG2_reac = models.FloatField(blank=True)

    uniqueObject = models.StringField()


# PAGES
# Pages Experimental Group 2
class SoMi_EG2_introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class SoMi_EG2(Page):
    form_model = 'player'
    form_fields = ['SoMiEG2', 'SoMiEG2_out', 'SoMiEG2_reac']

    @staticmethod
    def vars_for_template(player):
        player.uniqueObject = player.participant.objects_treat[player.round_number-1]
        image_unique = player.uniqueObject + ".JPG"

        index = int(player.participant.objects_treat[player.round_number-1][:-1]) - 1

        image_out = player.participant.preferences_other[index] + "_out.JPG"

        if player.participant.objects_treat[player.round_number-1][-1:] == 'a':
            image_double = player.participant.objects_treat[player.round_number-1][:-1] + "b.JPG"
        else:
            image_double = player.participant.objects_treat[player.round_number-1][:-1] + "a.JPG"

        print('image_unique: ',image_unique)
        print('image_double: ',image_double)
        print('image_out: ',image_out)

        return dict(
            image_unique = image_unique,
            image_double = image_double,
            image_out = image_out,
        )

    @staticmethod
    def js_vars(player):
        index = int(player.participant.objects_treat[player.round_number-1][:-1]) - 1

        if player.participant.objects_treat[player.round_number-1][-1:] == player.participant.preferences_other[index][-1:]:
            id_image_out = 2
        else:
            id_image_out = 1

        return dict(
            id_image_out = id_image_out,
        )

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.round_number == 8:
            return 'SoMi_ManipulationCheck'




page_sequence = [
    SoMi_EG2_introduction,
    SoMi_EG2
]
