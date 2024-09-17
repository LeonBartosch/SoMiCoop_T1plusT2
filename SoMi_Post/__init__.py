from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'SoMi_Post'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
#SoMi Post test
    SoMi_Post = models.IntegerField(
        label="Which of these objects would you take? You pick first, then the other!",
        widget=widgets.RadioSelectHorizontal, choices=[2, 2, 1] #1: unique object, 2: double object
    )
    uniqueObject = models.StringField()

# PAGES
#SoMi Pretest
##Instruction
class SoMi_Post_introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

###following pages randomized
class SoMi_Post(Page):
    form_model = 'player'
    form_fields = ['SoMi_Post']

    @staticmethod
    def vars_for_template(player):
        player.uniqueObject = player.participant.objects_post[player.round_number-1]
        image_unique = player.uniqueObject + ".JPG"

        if player.participant.objects_post[player.round_number-1][-1:] == 'a':
            image_double = player.participant.objects_post[player.round_number-1][:-1] + "b.JPG"
        else:
            image_double = player.participant.objects_post[player.round_number-1][:-1] + "a.JPG"

        return dict(
            image_unique = image_unique,
            image_double = image_double,
        )

page_sequence = [
    SoMi_Post_introduction,
    SoMi_Post
]

