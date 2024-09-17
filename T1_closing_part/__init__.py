from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'T1_closing_part'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    feedback = models.LongStringField(blank=True, label="If you would like to give us feedback or have any comments on "
                                                        "this study, please let us know below:")
    time_end = models.StringField()


# PAGES
class Closing_part(Page):
    form_model = 'player'
    form_fields = ['feedback']
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Close_window(Page):
    form_model = 'player'

page_sequence = [Closing_part, Close_window]
