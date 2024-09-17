from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_EG1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#SoMi Experimental Group 1

##Two red apples
    ###Reveal option
    SoMiEG1_R = models.IntegerField(
        label="Please select, whether you want to continue with or without the information.",
        choices=[
            [1, 'Reveal the object preference of the second chooser to me.'],
            [2, 'Let me immediately select one of the objects.'],
        ],
        widget=widgets.RadioSelect,
        blank = True
    )

    ###SoMi
    SoMiEG1 = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1]  # 1: unique object, 2: double object
    )

    uniqueObject = models.StringField()




# PAGES
# Pages Experimental Group 1
class SoMi_EG1_introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

##Two red apples
class SoMi_EG1(Page):
    form_model = 'player'
    form_fields = ['SoMiEG1_R', 'SoMiEG1']

    @staticmethod
    def vars_for_template(player):
        player.uniqueObject = player.participant.objects_treat[player.round_number-1]
        image_unique = player.uniqueObject + ".JPG"

        if player.participant.objects_treat[player.round_number-1][-1:] == 'a':
            image_double = player.participant.objects_treat[player.round_number-1][:-1] + "b.JPG"
        else:
            image_double = player.participant.objects_treat[player.round_number-1][:-1] + "a.JPG"

        index = int(player.participant.objects_treat[player.round_number-1][:-1]) - 1

        image_preference_other = player.participant.preferences_other[index] + ".JPG"

        return dict(
            image_unique = image_unique,
            image_double = image_double,
            image_preference_other = image_preference_other,
        )

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.round_number == 8:
            return 'SoMi_ManipulationCheck'




page_sequence = [
    SoMi_EG1_introduction,
    SoMi_EG1
]
