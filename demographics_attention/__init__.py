from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'attention_check'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
# demographics
    ##radio buttons for gender
    gender = models.IntegerField(
        label="Your gender:",
        widget=widgets.RadioSelect, choices=[
            [0, 'Female'],
            [1, 'Male'],
            [2, 'Diverse']
        ]
    )

    ##answer field for age
    age = models.IntegerField(max_length=3, min_length=2, label="Your age in numbers:")

    ##radio buttons for education level
    education = models.IntegerField(
        label="Your highest level of education:",
        widget=widgets.RadioSelect, choices=[
            [0, 'VMBO'],
            [1, 'HAVO'],
            [2, 'VWO'],
            [3, 'MBO'],
            [4, 'HBO'],
            [5, 'WO Bachelor'],
            [6, 'WO Master'],
            [7, 'Other: ']
        ]
    )

    ##answer field in case of answer "Other" in education level
    other_education = models.StringField(
        blank=True
    )

#attention check
    ##attention check effort
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

    ##attention check attention
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
class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'education', 'other_education']

class Attention_check(Page):
    form_model = 'player'
    form_fields = ['effort', 'attention', 'use_data']

page_sequence = [Demographics, Attention_check]
