from otree.api import *
from string import ascii_uppercase
import random

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'generate_code'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # generate 4 fields to enter code with maximum & minimum length defined
    mother_code = models.StringField(max_length=2, min_length=2, label="Please enter the first two letters of your mother's first name (e.g. Emma -> EM):")
    father_code = models.StringField(max_length=2, min_length=2, label="Please enter the first two letters of your father's first name (e.g. Noah -> NO):")
    city_code = models.StringField(max_length=2, min_length=2, label="Please enter the first two letters of the city in which you were born (e.g. Leiden -> LE):")
    birthday_code = models.StringField(max_length=3, min_length=3, label="Please enter the last digit of your date, month and year of birth (e.g. 08.12.2002 -> 822):")
    time_end = models.StringField()
    code = models.StringField(blank=True)
    code_memory = models.StringField(blank=True)

# PAGES
class Entering_personal_code(Page):
    form_model = 'player'
    form_fields = ['mother_code', 'father_code', 'city_code', 'birthday_code', 'code']

    @staticmethod
    # define errormessages for wrong answers in fields
    def error_message(player, values):

        if any(c.isdigit() for c in values['mother_code'] + values['father_code'] + values['city_code']):
            return "Please enter your code in the correct format (in the first three fields capital letters only)."

        if len(values['mother_code']) != 2 or len(values['father_code']) != 2 or len(values['city_code']) != 2:
            return 'In the first three fields the code must be two letters long.'

        if any(c not in ascii_uppercase for c in values['mother_code'] + values['father_code'] + values['city_code']):
            return "Please enter your code in the correct format (in the first three fields capital letters only)."

        if len(values['birthday_code']) != 3:
            return 'The code in the last field must be three digits long.'

        if not all(c.isdigit() for c in values['birthday_code']):
            return "Please enter your code in the correct format (in the last field numbers only)."

        path = "payout_information/" + values['mother_code'] + values['father_code'] + values['city_code'] + values['birthday_code'] + ".csv"

        import os
        print(path)
        if not os.path.isfile(path):
            return "Your code does not match any codes from the first part of the study. Please make sure to enter the same code as in the first part. If you don't remember your code, please turn to the experimentator."

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.personal_code = player.code

        SVO_payoff_self = []
        SVO_payoff_other = []

        import csv
        path = "payout_information/" + player.code + ".csv"
        with open(path, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == player.code:
                    SVO_payoff_self.append(row[1])
                    SVO_payoff_other.append(row[2])

        random_index = random.randint(0, 14)

        player.participant.T1_SVO_payoff_self = SVO_payoff_self[random_index]
        player.participant.T1_SVO_payoff_other = SVO_payoff_other[random_index]

        print(player.participant.T1_SVO_payoff_self)
        print(player.participant.T1_SVO_payoff_other)

        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Start_T2(Page):
    pass

page_sequence = [Entering_personal_code, Start_T2]


