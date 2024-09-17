from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'T1_attention_check'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    effort = models.IntegerField(
        choices=[
            [1, 'almost none'],
            [2, 'very little'],
            [3, 'a little'],
            [4, 'quite a lot'],
            [5, 'very much'],
        ],
        widget=widgets.RadioSelect
    )
    attention = models.IntegerField(
        choices=[
            [1, 'almost none'],
            [2, 'very little of my'],
            [3, 'some of mine'],
            [4, 'most of my'],
            [5, 'my full'],
        ],
        widget=widgets.RadioSelect
    )
    use_data = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ]
    )

    attention_check_pass = models.BooleanField(
        initial=False
    )


# PAGES
class Attention_check(Page):
    form_model = 'player'
    form_fields = ['effort', 'attention', 'use_data']

page_sequence = [Attention_check]
