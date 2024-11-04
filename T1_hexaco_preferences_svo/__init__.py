from otree.api import *
import random
import csv


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'hexaco_preference_svo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 15


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

#HEXACO Items
    h1 = models.IntegerField(
        label="If I knew that I could never get caught, I would be willing to steal a million euros.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h2 = models.IntegerField(
        label="I worry a lot less than most people do.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h3 = models.IntegerField(
        label="I rarely, if ever, have trouble sleeping due to stress or anxiety.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h4 = models.IntegerField(
        label="I am energetic nearly all the time.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h5 = models.IntegerField(
        label="I try to give generously to those in need.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h6 = models.IntegerField(
        label="People often joke with me about the messiness of my room or desk.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h7 = models.IntegerField(
        label="Most people are more upbeat and dynamic than I generally am.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h8 = models.IntegerField(
        label="People sometimes tell me that I am too critical of others.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h9 = models.IntegerField(
        label="I make a lot of mistakes because I don't think before I act.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h10 = models.IntegerField(
        label="The first thing that I always do in a new place is to make friends.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h11 = models.IntegerField(
        label="I prefer jobs that involve active social interaction to those that involve working alone.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h12 = models.IntegerField(
        label="People often tell me that I should try to cheer up.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h13 = models.IntegerField(
        label="I want people to know that I am an important person of high status.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h14 = models.IntegerField(
        label="I would be very bored by a book about the history of science and technology.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h15 = models.IntegerField(
        label="I find it hard to fully forgive someone who has done something mean to me.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h16 = models.IntegerField(
        label="I sometimes can't help worrying about little things.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h17 = models.IntegerField(
        label="I wouldn't pretend to like someone just to get that person to do favors for me.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h18 = models.IntegerField(
        label="I would never accept a bribe, even if it were very large.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h19 = models.IntegerField(
        label="I find it boring to discuss philosophy.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h20 = models.IntegerField(
        label="I don’t allow my impulses to govern my behavior.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h21 = models.IntegerField(
        label="I find it hard to compromise with people when I really think I’m right.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h22 = models.IntegerField(
        label="People often call me a perfectionist.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h23 = models.IntegerField(
        label="I avoid making small talk with people.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h24 = models.IntegerField(
        label="If I want something from a person I dislike, I will act very nicely toward that person in order to get "
              "it.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h25 = models.IntegerField(
        label="I prefer to do whatever comes to mind, rather than stick to a plan.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h26 = models.IntegerField(
        label="Most people tend to get angry more quickly than I do.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h27 = models.IntegerField(
        label="I generally accept people’s faults without complaining about them.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h28 = models.IntegerField(
        label="I would be tempted to buy stolen property if I were financially tight.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h29 = models.IntegerField(
        label="I plan ahead and organize things, to avoid scrambling at the last minute.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h30 = models.IntegerField(
        label="I like the idea that only the strong should survive.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h31 = models.IntegerField(
        label="I always try to be accurate in my work, even at the expense of time.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h32 = models.IntegerField(
        label="I feel strong emotions when someone close to me is going away for a long time.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h33 = models.IntegerField(
        label="People have often told me that I have a good imagination.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h34 = models.IntegerField(
        label="I'm interested in learning about the history and politics of other countries.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h35 = models.IntegerField(
        label="I am usually quite flexible in my opinions when people disagree with me.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h36 = models.IntegerField(
        label="I tend to feel quite self-conscious when speaking in front of a group of people.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h37 = models.IntegerField(
        label="I rarely discuss my problems with other people.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h38 = models.IntegerField(
        label="I think of myself as a somewhat eccentric person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h39 = models.IntegerField(
        label="I am an ordinary person who is no better than others.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h40 = models.IntegerField(
        label="If I had the opportunity, I would like to attend a classical music concert.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h41 = models.IntegerField(
        label="It wouldn’t bother me to harm someone I didn’t like.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h42 = models.IntegerField(
        label="I feel reasonably satisfied with myself overall.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h43 = models.IntegerField(
        label="I think that paying attention to radical ideas is a waste of time.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h44 = models.IntegerField(
        label="I have sympathy for people who are less fortunate than I am.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h45 = models.IntegerField(
        label="Sometimes I like to just watch the wind as it blows through the trees.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h46 = models.IntegerField(
        label="In social situations, I'm usually the one who makes the first move.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h47 = models.IntegerField(
        label="When working on something, I don't pay much attention to small details.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h48 = models.IntegerField(
        label="I rarely hold a grudge, even against people who have badly wronged me.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h49 = models.IntegerField(
        label="When people tell me that I’m wrong, my first reaction is to argue with them.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h50 = models.IntegerField(
        label="When someone I know well is unhappy, I can almost feel that person's pain myself.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h51 = models.IntegerField(
        label="I try to respect other people’s feelings.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h52 = models.IntegerField(
        label="When working, I sometimes have difficulties due to being disorganized.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h53 = models.IntegerField(
        label="People think of me as someone who has a quick temper.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h54 = models.IntegerField(
        label="I’d be tempted to use counterfeit money, if I were sure I could get away with it.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h55 = models.IntegerField(
        label="I would like to be seen driving around in a very expensive car.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h56 = models.IntegerField(
        label="I clean my office or home quite frequently.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h57 = models.IntegerField(
        label="When I suffer from a painful experience, I need someone to make me feel comfortable.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h58 = models.IntegerField(
        label="I wouldn’t want people to treat me as though I were superior to them.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h59 = models.IntegerField(
        label="I rarely express my opinions in group meetings.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h60 = models.IntegerField(
        label="I think that most people like some aspects of my personality.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h61 = models.IntegerField(
        label="I would be quite bored by a visit to an art gallery.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h62 = models.IntegerField(
        label="I don’t mind doing jobs that involve dangerous work.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h63 = models.IntegerField(
        label="I would like a job that requires following a routine rather than being creative. ",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h64 = models.IntegerField(
        label="	I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h65 = models.IntegerField(
        label="People see me as a hard-hearted person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h66 = models.IntegerField(
        label="I rarely feel anger, even when people treat me quite badly.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h67 = models.IntegerField(
        label="I feel like crying when I see other people crying.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h68 = models.IntegerField(
        label="I would enjoy creating a work of art, such as a novel, a song, or a painting.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h69 = models.IntegerField(
        label="When working, I often set ambitious goals for myself.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h70 = models.IntegerField(
        label="If I want something from someone, I will laugh at that person's worst jokes.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h71 = models.IntegerField(
        label="Whenever I feel worried about something, I want to share my concern with another person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h72 = models.IntegerField(
        label="I can handle difficult situations without needing emotional support from anyone else.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h73 = models.IntegerField(
        label="I feel that I am an unpopular person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h74 = models.IntegerField(
        label="Often when I set a goal, I end up quitting without having reached it.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h75 = models.IntegerField(
        label="I am a soft-hearted person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h76 = models.IntegerField(
        label="I enjoy looking at maps of different places.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h77 = models.IntegerField(
        label="On most days, I feel cheerful and optimistic.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h78 = models.IntegerField(
        label="I’ve never really enjoyed looking through an encyclopedia.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h79 = models.IntegerField(
        label="	I find it hard to keep my temper when people insult me.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h80 = models.IntegerField(
        label="People sometimes tell me that I'm too stubborn.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h81 = models.IntegerField(
        label="I think that I am entitled to more respect than the average person is.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h82 = models.IntegerField(
        label="I don't think of myself as the artistic or creative type.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h83 = models.IntegerField(
        label="Even in an emergency I wouldn't feel like panicking.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h84 = models.IntegerField(
        label="I often check my work over repeatedly to find any mistakes.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h85 = models.IntegerField(
        label="I would feel afraid if I had to travel in bad weather conditions.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h86 = models.IntegerField(
        label="I sometimes feel that I am a worthless person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h87 = models.IntegerField(
        label="When it comes to physical danger, I am very fearful.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h88 = models.IntegerField(
        label="I do only the minimum amount of work needed to get by. ",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h89 = models.IntegerField(
        label="I make decisions based on the feeling of the moment rather than on careful thought.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h90 = models.IntegerField(
        label="My attitude toward people who have treated me badly is 'forgive and forget'",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h91 = models.IntegerField(
        label="I tend to be lenient in judging other people.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h92 = models.IntegerField(
        label="I would like to live in a very expensive, high-class neighborhood.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h93 = models.IntegerField(
        label="I would get a lot of pleasure from owning expensive luxury goods.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h94 = models.IntegerField(
        label="I get very anxious when waiting to hear about an important decision.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h95 = models.IntegerField(
        label="I wouldn't spend my time reading a book of poetry.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h96 = models.IntegerField(
        label="If someone has cheated me once, I will always feel suspicious of that person.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h97 = models.IntegerField(
        label="I would feel very badly if I were to hurt someone.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h98 = models.IntegerField(
        label="I remain unemotional even in situations where most people get very sentimental.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h99 = models.IntegerField(
        label="When I'm in a group of people, I'm often the one who speaks on behalf of the group.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h100 = models.IntegerField(
        label="I like people who have unconventional views.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h101 = models.IntegerField(
        label="I often push myself very hard when trying to achieve a goal.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h102 = models.IntegerField(
        label="Even when people make a lot of mistakes, I rarely say anything negative.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h103 = models.IntegerField(
        label="I enjoy having lots of people around to talk with.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    h104 = models.IntegerField(
        label="Having a lot of money is not especially important to me.",
        widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5]
    )
    hexaco_check_pass = models.BooleanField(
        initial=False)

#preference rating items
    pref_exa = models.FloatField(
        blank=True
    ) #green M&M (exercise)
    pref_exb = models.FloatField(
        blank=True
    ) #blue M&M (exercise)

    pref_a = models.FloatField(
        blank=True
    )
    pref_b = models.FloatField(
        blank=True
    )
    object = models.IntegerField()

#svo slider items
    svo_choice_1 = models.IntegerField(blank=True)
    svo_choice_2 = models.IntegerField(blank=True)
    svo_choice_3 = models.IntegerField(blank=True)
    svo_choice_4 = models.IntegerField(blank=True)
    svo_choice_5 = models.IntegerField(blank=True)
    svo_choice_6 = models.IntegerField(blank=True)
    svo_choice_7 = models.IntegerField(blank=True)
    svo_choice_8 = models.IntegerField(blank=True)
    svo_choice_9 = models.IntegerField(blank=True)
    svo_choice_10 = models.IntegerField(blank=True)
    svo_choice_11 = models.IntegerField(blank=True)
    svo_choice_12 = models.IntegerField(blank=True)
    svo_choice_13 = models.IntegerField(blank=True)
    svo_choice_14 = models.IntegerField(blank=True)
    svo_choice_15 = models.IntegerField(blank=True)
    svo_choice_1_self = models.IntegerField(blank=True)
    svo_choice_2_self = models.IntegerField(blank=True)
    svo_choice_3_self = models.IntegerField(blank=True)
    svo_choice_4_self = models.IntegerField(blank=True)
    svo_choice_5_self = models.IntegerField(blank=True)
    svo_choice_6_self = models.IntegerField(blank=True)
    svo_choice_7_self = models.IntegerField(blank=True)
    svo_choice_8_self = models.IntegerField(blank=True)
    svo_choice_9_self = models.IntegerField(blank=True)
    svo_choice_10_self = models.IntegerField(blank=True)
    svo_choice_11_self = models.IntegerField(blank=True)
    svo_choice_12_self = models.IntegerField(blank=True)
    svo_choice_13_self = models.IntegerField(blank=True)
    svo_choice_14_self = models.IntegerField(blank=True)
    svo_choice_15_self = models.IntegerField(blank=True)
    svo_choice_1_other = models.IntegerField(blank=True)
    svo_choice_2_other = models.IntegerField(blank=True)
    svo_choice_3_other = models.IntegerField(blank=True)
    svo_choice_4_other = models.IntegerField(blank=True)
    svo_choice_5_other = models.IntegerField(blank=True)
    svo_choice_6_other = models.IntegerField(blank=True)
    svo_choice_7_other = models.IntegerField(blank=True)
    svo_choice_8_other = models.IntegerField(blank=True)
    svo_choice_9_other = models.IntegerField(blank=True)
    svo_choice_10_other = models.IntegerField(blank=True)
    svo_choice_11_other = models.IntegerField(blank=True)
    svo_choice_12_other = models.IntegerField(blank=True)
    svo_choice_13_other = models.IntegerField(blank=True)
    svo_choice_14_other = models.IntegerField(blank=True)
    svo_choice_15_other = models.IntegerField(blank=True)
    svo_tot_ego = models.IntegerField()
    svo_tot_alter = models.IntegerField()
    svo_mean_ego = models.FloatField()
    svo_mean_alter = models.FloatField()
    svo_ratio = models.FloatField()
    svo_angle = models.FloatField()
    svo_check_pass = models.BooleanField(
        initial=False
    )

##Randomisierung der measures + Randomisierung von preference-ratings
def creating_session(subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            random_measure = list(range(1, 4)) #1 = hexaco, 2 = svo, 3 = preferences
            random.shuffle(random_measure)
            random_pref = list(range(4, 16))

            random.shuffle(random_pref)

            random_pref = [3] + random_pref

            rounds = []
            for i in range(3):
                if random_measure[i] == 3:
                    rounds += random_pref
                else:
                    rounds.append(random_measure[i])
            print(rounds)

            p.participant.round_numbers = rounds


# PAGES HEXACO
class Transition_to_HEXACO(Page):
    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 1

class HEXACO(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 1

    random_hexaco_items = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13', 'h14',
                           'h15', 'h16', 'h17', 'h18', 'h19', 'h20', 'h21', 'h22', 'h23', 'h24', 'h25', 'h26',
                           'h27', 'h28', 'h29', 'h30', 'h31', 'h32', 'h33', 'h34', 'h35', 'h36', 'h37', 'h38',
                           'h39', 'h40', 'h41', 'h42', 'h43', 'h44', 'h45', 'h46', 'h47', 'h48', 'h49', 'h50',
                           'h51', 'h52', 'h53', 'h54', 'h55', 'h56', 'h57', 'h58', 'h59', 'h60', 'h61', 'h62',
                           'h63', 'h64', 'h65', 'h66', 'h67', 'h68', 'h69', 'h70', 'h71', 'h72', 'h73', 'h74',
                           'h75', 'h76', 'h77', 'h78', 'h79', 'h80', 'h81', 'h82', 'h83', 'h84', 'h85', 'h86',
                           'h87', 'h88', 'h89', 'h90', 'h91', 'h92', 'h93', 'h94', 'h95', 'h96', 'h97', 'h98',
                           'h99', 'h100', 'h101', 'h102', 'h103', 'h104']
    import random
    random.shuffle(random_hexaco_items)
    form_fields = random_hexaco_items


#PAGES Preference rating
class Transition_to_Preferences(Page):
    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 3

class Exercise_Preferences(Page):
    form_model = 'player'
    form_fields = ['pref_exa', 'pref_exb']

    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 3

class Transition_to_End_of_Exercise_Preferences(Page):
    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 3

class Preferences(Page):
    form_model = 'player'
    form_fields = ['pref_a', 'pref_b']

    @staticmethod
    def vars_for_template(player):
        objectA = str(player.participant.round_numbers[player.round_number - 1]-3) + "a.JPG"
        objectB = str(player.participant.round_numbers[player.round_number - 1]-3) + "b.JPG"

        player.object = player.participant.round_numbers[player.round_number - 1]-3

        return dict(
            objectA = objectA,
            objectB = objectB,
        )

    @staticmethod
    def is_displayed(player):
        return 4 <= player.participant.round_numbers[player.round_number - 1] <= 15

#PAGES svo slider
class Transition_to_SVO(Page):
    def before_next_page(player, timeout_happened):
        with open(player.session.config['svo_file']) as f:
            r = csv.reader(f, delimiter=";")
            c = [line for line in r]
            h = c[0]
            d = [dict(zip(h, l)) for l in c[1:]]
            for row in r:
                print(row)
            player.session.vars["SVO_Fullx11"] = [
                [[r, l["A" + str(i + 1)], l["B" + str(i + 1)]] for i in range(int(9))]
                for r, l in enumerate(d)]

    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 2

class SVO_items(Page):
    form_model = 'player'
    form_fields = ["svo_choice_1", "svo_choice_2", "svo_choice_3", "svo_choice_4", "svo_choice_5", "svo_choice_6", "svo_choice_7", "svo_choice_8", "svo_choice_9", "svo_choice_10", "svo_choice_11", "svo_choice_12", "svo_choice_13", "svo_choice_14", "svo_choice_15","svo_choice_1_self", "svo_choice_2_self", "svo_choice_3_self", "svo_choice_4_self", "svo_choice_5_self", "svo_choice_6_self", "svo_choice_7_self", "svo_choice_8_self", "svo_choice_9_self", "svo_choice_10_self", "svo_choice_11_self", "svo_choice_12_self", "svo_choice_13_self", "svo_choice_14_self", "svo_choice_15_self","svo_choice_1_other", "svo_choice_2_other", "svo_choice_3_other", "svo_choice_4_other", "svo_choice_5_other", "svo_choice_6_other", "svo_choice_7_other", "svo_choice_8_other", "svo_choice_9_other", "svo_choice_10_other", "svo_choice_11_other", "svo_choice_12_other", "svo_choice_13_other", "svo_choice_14_other", "svo_choice_15_other", "svo_tot_ego", "svo_tot_alter", "svo_mean_ego", "svo_mean_alter", "svo_ratio", "svo_angle"]

    @staticmethod
    def vars_for_template(player):
        SVO = player.session.vars["SVO_Fullx11"]
        return dict(
            SVO = SVO
        )

    @staticmethod
    def js_vars(player):
        SVO = player.session.vars["SVO_Fullx11"]
        return dict(
            SVO=SVO
        )

    @staticmethod
    def is_displayed(player):
        return player.participant.round_numbers[player.round_number - 1] == 2

    @staticmethod
    def before_next_page(player, timeout_happened):
        import csv

        filename = "payout_information/" + player.participant.personal_code + ".csv"

        header = ['personal_code', 'T1_SVO_payoff_self', 'T1_SVO_payoff_other']

        with open(filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)
            # write the data
            writer.writerow([player.participant.personal_code, player.svo_choice_1_self, player.svo_choice_1_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_2_self, player.svo_choice_2_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_3_self, player.svo_choice_3_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_4_self, player.svo_choice_4_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_5_self, player.svo_choice_5_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_6_self, player.svo_choice_6_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_7_self, player.svo_choice_7_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_8_self, player.svo_choice_8_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_9_self, player.svo_choice_9_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_10_self, player.svo_choice_10_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_11_self, player.svo_choice_11_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_12_self, player.svo_choice_12_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_13_self, player.svo_choice_13_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_14_self, player.svo_choice_14_other])
            writer.writerow([player.participant.personal_code, player.svo_choice_15_self, player.svo_choice_15_other])


#PAGESEQUENCE
page_sequence = [
    Transition_to_HEXACO,
    HEXACO,
    Transition_to_Preferences,
    Exercise_Preferences,
    Transition_to_End_of_Exercise_Preferences,
    Preferences,
    Transition_to_SVO,
    SVO_items
]
