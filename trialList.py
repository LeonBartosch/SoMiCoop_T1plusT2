
import random


class TrialObject:

    id = ""
    name = ""
    value = ""
    url = ""

    def __init__(self, htmlid, name, value, url):
        self.id = htmlid
        self.name = name
        self.value = value
        self.url = url


class TrialList:

    def __init__(self):
        self.initializeTrialsList()
        pass

    def randomize(self, arr, n):
        # Start from the last element and swap one by one. We don't
        # need to run for the first element that's why i > 0
        for i in range(n - 1, 0, -1):
            # Pick a random index from 0 to i
            j = random.randint(0, i)

            # Swap arr[i] with the element at random index
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    # Strukturierte Liste aller Trials
    # Jedes Listenelement beinhaltet die Objektdaten von Trial und Complementary Trial.
    # Beim Randomisieren der Liste ist so sichergestellt, dass Trial und Complementary Trial
    # nicht voneinander getrennt werden.
    trials = [
                [
                    [   # Trial Objekte
                        TrialObject(htmlid="id01", name="trial_1a", value="double", url="img/SoMiPu/Alarm_green.png"),
                        TrialObject(htmlid="id02", name="trial_1a", value="single", url="img/SoMiPu/Alarm_silver.png"),
                        TrialObject(htmlid="id03", name="trial_1a", value="double", url="img/SoMiPu/Alarm_green.png")
                    ],
                    [   # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id11", name="trial_1b", value="double", url="img/SoMiPu/Alarm_silver.png"),
                        TrialObject(htmlid="id12", name="trial_1b", value="single", url="img/SoMiPu/Alarm_green.png"),
                        TrialObject(htmlid="id13", name="trial_1b", value="double", url="img/SoMiPu/Alarm_silver.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id21", name="trial_2a", value="double", url="img/SoMiPu/Apple_green.png"),
                        TrialObject(htmlid="id22", name="trial_2a", value="single", url="img/SoMiPu/Apple_red.png"),
                        TrialObject(htmlid="id23", name="trial_2a", value="double", url="img/SoMiPu/Apple_green.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id31", name="trial_2b", value="double", url="img/SoMiPu/Apple_red.png"),
                        TrialObject(htmlid="id32", name="trial_2b", value="single", url="img/SoMiPu/Apple_green.png"),
                        TrialObject(htmlid="id33", name="trial_2b", value="double", url="img/SoMiPu/Apple_red.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id41", name="trial_3a", value="double", url="img/SoMiPu/Blanket_blue.png"),
                        TrialObject(htmlid="id42", name="trial_3a", value="single", url="img/SoMiPu/Blanket_yellow.png"),
                        TrialObject(htmlid="id43", name="trial_3a", value="double", url="img/SoMiPu/Blanket_blue.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id51", name="trial_3b", value="double", url="img/SoMiPu/Blanket_yellow.png"),
                        TrialObject(htmlid="id52", name="trial_3b", value="single", url="img/SoMiPu/Blanket_blue.png"),
                        TrialObject(htmlid="id53", name="trial_3b", value="double", url="img/SoMiPu/Blanket_yellow.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id61", name="trial_4a", value="double", url="img/SoMiPu/Cap_blue.png"),
                        TrialObject(htmlid="id62", name="trial_4a", value="single", url="img/SoMiPu/Cap_orange.png"),
                        TrialObject(htmlid="id63", name="trial_4a", value="double", url="img/SoMiPu/Cap_blue.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id71", name="trial_4b", value="double", url="img/SoMiPu/Cap_orange.png"),
                        TrialObject(htmlid="id72", name="trial_4b", value="single", url="img/SoMiPu/Cap_blue.png"),
                        TrialObject(htmlid="id73", name="trial_4b", value="double", url="img/SoMiPu/Cap_orange.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id81", name="trial_5a", value="double", url="img/SoMiPu/Chocolate_dark.png"),
                        TrialObject(htmlid="id82", name="trial_5a", value="single", url="img/SoMiPu/Chocolate_nut.png"),
                        TrialObject(htmlid="id83", name="trial_5a", value="double", url="img/SoMiPu/Chocolate_dark.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id91", name="trial_5b", value="double", url="img/SoMiPu/Chocolate_nut.png"),
                        TrialObject(htmlid="id92", name="trial_5b", value="single", url="img/SoMiPu/Chocolate_dark.png"),
                        TrialObject(htmlid="id93", name="trial_5b", value="double", url="img/SoMiPu/Chocolate_nut.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id101", name="trial_6a", value="double", url="img/SoMiPu/Cup_green.png"),
                        TrialObject(htmlid="id102", name="trial_6a", value="single", url="img/SoMiPu/Cup_red.png"),
                        TrialObject(htmlid="id103", name="trial_6a", value="double", url="img/SoMiPu/Cup_green.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id111", name="trial_6b", value="double", url="img/SoMiPu/Cup_red.png"),
                        TrialObject(htmlid="id112", name="trial_6b", value="single", url="img/SoMiPu/Cup_green.png"),
                        TrialObject(htmlid="id113", name="trial_6b", value="double", url="img/SoMiPu/Cup_red.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id121", name="trial_7a", value="double", url="img/SoMiPu/Cupcake_pink.png"),
                        TrialObject(htmlid="id122", name="trial_7a", value="single", url="img/SoMiPu/Cupcake_white.png"),
                        TrialObject(htmlid="id123", name="trial_7a", value="double", url="img/SoMiPu/Cupcake_pink.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id131", name="trial_7b", value="double", url="img/SoMiPu/Cupcake_white.png"),
                        TrialObject(htmlid="id132", name="trial_7b", value="single", url="img/SoMiPu/Cupcake_pink.png"),
                        TrialObject(htmlid="id133", name="trial_7b", value="double", url="img/SoMiPu/Cupcake_white.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id141", name="trial_8a", value="double", url="img/SoMiPu/Pen_blue.png"),
                        TrialObject(htmlid="id142", name="trial_8a", value="single", url="img/SoMiPu/Pen_silver.png"),
                        TrialObject(htmlid="id143", name="trial_8a", value="double", url="img/SoMiPu/Pen_blue.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id151", name="trial_8b", value="double", url="img/SoMiPu/Pen_silver.png"),
                        TrialObject(htmlid="id152", name="trial_8b", value="single", url="img/SoMiPu/Pen_blue.png"),
                        TrialObject(htmlid="id153", name="trial_8b", value="double", url="img/SoMiPu/Pen_silver.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id161", name="trial_9a", value="double", url="img/SoMiPu/Present_green.png"),
                        TrialObject(htmlid="id162", name="trial_9a", value="single", url="img/SoMiPu/Present_red.png"),
                        TrialObject(htmlid="id163", name="trial_9a", value="double", url="img/SoMiPu/Present_green.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id171", name="trial_9b", value="double", url="img/SoMiPu/Present_red.png"),
                        TrialObject(htmlid="id172", name="trial_9b", value="single", url="img/SoMiPu/Present_green.png"),
                        TrialObject(htmlid="id173", name="trial_9b", value="double", url="img/SoMiPu/Present_red.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id181", name="trial_10a", value="double", url="img/SoMiPu/Sweet_red.png"),
                        TrialObject(htmlid="id182", name="trial_10a", value="single", url="img/SoMiPu/Sweet_purple.png"),
                        TrialObject(htmlid="id183", name="trial_10a", value="double", url="img/SoMiPu/Sweet_red.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id191", name="trial_10b", value="double", url="img/SoMiPu/Sweet_purple.png"),
                        TrialObject(htmlid="id192", name="trial_10b", value="single", url="img/SoMiPu/Sweet_red.png"),
                        TrialObject(htmlid="id193", name="trial_10b", value="double", url="img/SoMiPu/Sweet_purple.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id201", name="trial_11a", value="double", url="img/SoMiPu/Tulips_red.png"),
                        TrialObject(htmlid="id202", name="trial_11a", value="single", url="img/SoMiPu/Tulips_yellow.png"),
                        TrialObject(htmlid="id203", name="trial_11a", value="double", url="img/SoMiPu/Tulips_red.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id211", name="trial_11b", value="double", url="img/SoMiPu/Tulips_yellow.png"),
                        TrialObject(htmlid="id212", name="trial_11b", value="single", url="img/SoMiPu/Tulips_red.png"),
                        TrialObject(htmlid="id213", name="trial_11b", value="double", url="img/SoMiPu/Tulips_yellow.png")
                    ]
                ],
                [
                    [  # Trial Objekte
                        TrialObject(htmlid="id221", name="trial_12a", value="double", url="img/SoMiPu/Umbrella_yellow.png"),
                        TrialObject(htmlid="id222", name="trial_12a", value="single", url="img/SoMiPu/Umbrella_blue.png"),
                        TrialObject(htmlid="id223", name="trial_12a", value="double", url="img/SoMiPu/Umbrella_yellow.png")
                    ],
                    [  # Trial Objekte Complementary Trial
                        TrialObject(htmlid="id231", name="trial_12b", value="double", url="img/SoMiPu/Umbrella_blue.png"),
                        TrialObject(htmlid="id232", name="trial_12b", value="single", url="img/SoMiPu/Umbrella_yellow.png"),
                        TrialObject(htmlid="id233", name="trial_12b", value="double", url="img/SoMiPu/Umbrella_blue.png")
                    ]
                ]
    ]


    def initializeTrialsList(self):
        self.trials = self.randomize(self.trials, self.trials.__len__())

        for i in range(0, self.trials.__len__(), 1):
            self.trials[i][0] = self.randomize(self.trials[i][0], 3)
            self.trials[i][1] = self.randomize(self.trials[i][1], 3)
            #print("id:" + self.trials[i][0][0].id + " name:" + self.trials[i][0][0].name + " url:" + self.trials[i][0][0].url)
            #print("id:" + self.trials[i][0][1].id + " name:" + self.trials[i][0][1].name + " url:" + self.trials[i][0][1].url)
            #print("id:" + self.trials[i][0][2].id + " name:" + self.trials[i][0][2].name + " url:" + self.trials[i][0][2].url)
            #print("id:" + self.trials[i][1][0].id + " name:" + self.trials[i][1][0].name + " url:" + self.trials[i][1][0].url)
            #print("id:" + self.trials[i][1][1].id + " name:" + self.trials[i][1][1].name + " url:" + self.trials[i][1][1].url)
            #print("id:" + self.trials[i][1][2].id + " name:" + self.trials[i][1][2].name + " url:" + self.trials[i][1][2].url)


    def getTrial(self, index, subindex):
        return self.trials[index][subindex]
