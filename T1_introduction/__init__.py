from otree.api import *
from otree.api import models

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'T1_introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    informed_consent = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ],
        blank=False, label=""
    )
    time_end = models.StringField()
    code = models.StringField(label="")


# PAGES
class Introduction(Page): #Verweis auf html page, die diese Eigenschaften haben soll
    def before_next_page(player, timeout_happened):
        import datetime
        # player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") #Speicherung der Zeit, wenn der Spieler die Seite verlässt

class Informed_consent(Page):
    form_model = 'player'
    form_fields = ['informed_consent']

    @staticmethod
    def error_message(player, values):
        if values['informed_consent'] is not True:
            return 'You must consent to the statements above to be able to take part in this study.'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


page_sequence = [Introduction, Informed_consent]