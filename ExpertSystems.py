from pyknow import *
import itertools


class plant(Fact):
    pass


class tuber(Fact):
    pass


class plant_diagnoses(KnowledgeEngine):
    @Rule(AND(plant(temprature='high'), plant(humidity='normal'),
              tuber(color='reddish-brown'), tuber(shape='spots')))
    def black(self):
        print('Plant has black heart')

    @Rule(AND(plant(temprature='low'), plant(humidity='high'),
              tuber(color='normal'), tuber(shape='spots')))
    def late(self):
        print('Plant has late blight')

    @Rule(AND(plant(temprature='high'), plant(humidity='normal'),
              tuber(color='dry'), tuber(shape='circles')))
    def rot(self):
        print('Plant has dry rot')

    @Rule(AND(plant(temprature='normal'), plant(humidity='normal'),
              tuber(color='brown'), tuber(shape='wrinkles')))
    def early(self):
        print('Plant has early blight')


class Symptoms(Fact):
    pass


class Patient(Fact):
    pass


low_sugar_list = ["shakiness", "hunger", "sweating", "headache", "pale"]
high_sugar_list = ["thirst", "blurred vision", "headache", "dry mouth",
                   "smelly breath", "shortness of breath"]

permutation_high_sugar = []
permutation_low_sugar = []
first_time = [1]
first_t = [1]


def low_sugar_function(symptoms_list, s1, s2, s3, s4, s5):
    counter = 0

    user_symptoms = [s1, s2, s3, s4, s5]
    user_symptoms = set(user_symptoms)
    for sy in user_symptoms:
        if sy in symptoms_list:
            counter += 1
    if counter > 2:#and user_symptoms not in x:  # ana msh 3rfa ely b3d el and da leh
        first_time[0] = 0
        return True
    else:
        return False


def high_sugar_function(symptoms_list, s1, s2, s3, s4, s5, s6):
    counter = 0
    user_symptoms = [s1, s2, s3, s4, s5, s6]
    user_symptoms = set(user_symptoms)
    for sy in user_symptoms:
        if sy in symptoms_list:
            counter += 1
    if counter > 2:  # and user_symptoms not in x:  # ana msh 3rfa ely b3d el and da leh
        first_time[0] = 0
        return True
    else:
        return False


class MedicalExpertSystem(KnowledgeEngine):

    @Rule(Symptoms(MATCH.f1), Symptoms(MATCH.f2), Symptoms(MATCH.f3), Symptoms(MATCH.f4), Symptoms(MATCH.f5),
          TEST(lambda f1, f2, f3, f4, f5: low_sugar_function(low_sugar_list, f1, f2, f3, f4, f5)))
    def match_low_sugar(self):
        self.declare(Symptoms(low_sugar=True))

    @Rule(Symptoms(MATCH.f1), Symptoms(MATCH.f2), Symptoms(MATCH.f3), Symptoms(MATCH.f4), Symptoms(MATCH.f5)
         ,Symptoms(MATCH.f6),
          TEST(lambda f1, f2, f3, f4, f5, f6: high_sugar_function(high_sugar_list, f1, f2, f3, f4, f5, f6)))
    def match_high_sugar(self):
        self.declare(Symptoms(high_sugar=True))

    @Rule(AND(Symptoms("runny nose"), Symptoms("harsh cough")))
    def match_cold(self):
        self.declare(Symptoms(cold=True))

    @Rule(Symptoms(cold=True))
    def print_cold(self):
        print("You have cold.")

    @Rule(AND(Symptoms(low_sugar=True), Symptoms(Diabetic_Parents=True)))
    def match_diabetes(self):
        self.declare(Symptoms(diabetic_parents=True))

    @Rule(AND(Symptoms("conjunctives"), Symptoms("strong body aches"),
          Symptoms("weakness"), Symptoms("vomiting"), Symptoms("sore throat"), Symptoms("sneezing")))
    def match_flu(self):
        self.declare(Symptoms(flu_list=True))

    @Rule(AND(Symptoms("brownish-pink rash"), Symptoms("high and fast temperature"),
          Symptoms("bloodshot eyes"), Symptoms("white spots inside cheek")))
    def match_measles_list(self):
        self.declare(Symptoms(measles_list=True))

    @Rule(AND(Symptoms("moderate temperature"), Symptoms("saliva is not normal"),
          Symptoms("swollen lymph nodes in neck"), Symptoms("mouth is dry")))
    def match_mumps_list(self):
        self.declare(Symptoms(mumps_list=True))

    @Rule(AND(Patient(is_child=True), Symptoms(cold=True), Symptoms(measles_list=True)))
    def match_measles(self):
        print("You have measles.")

    @Rule(AND(Patient(is_child=True), Symptoms(mumps_list=True)))
    def match_mumps(self):
        print("You have mumps.")

    @Rule(AND(Patient(is_child=True), Symptoms(flu_list=True), Symptoms(cold=True)))
    def match_child_flu(self):
        print("You have child flu.")

    @Rule(AND(Patient(is_child=False), Symptoms(flu_list=True), Symptoms(cold=True)))
    def match_adult_flu(self):
        print("You have adult flu.")

    @Rule(Symptoms(high_sugar=True))
    def print_highsugar(self):
        print("You have signs of high sugar.")

    @Rule(Symptoms(low_sugar=True))
    def print_lowsugar(self):
        print("You have signs of low sugar.")

    @Rule(AND(Symptoms(diabetic_parents=True)))
    def print_diab_parents(self):
        print("You could be diabetic.")


def medical_fun():
    my_engine = MedicalExpertSystem()
    my_engine.reset()
    print("Enter your age")
    patient_age = int(input())
    if patient_age <= 5:
        my_engine.declare(Patient(is_child=True))
    else:
        my_engine.declare(Patient(is_child=False))
    while True:
        my_engine.declare(Symptoms(input("Enter a symptom: ")))
        answer = input("Do you have another symptom?(Y/N)").lower()
        if answer == "n":
            break

    a1 = input("Do you have a diabetic parent?(Y/N)").lower()
    if a1 == 'n':
        my_engine.declare(Symptoms(Diabetic_Parents=False))
    else:
        my_engine.declare(Symptoms(Diabetic_Parents=True))
    my_engine.run()
    '''#-------------------------------------------------------------------------cold sypmtoms
    print("Enter Yes if you have runny nose, No if you don't.")
    q1 = input()

    if q1 == "Yes" or q1 == "yes":
        my_engine.declare(Symptoms("runny nose"))

    print("Enter Yes if you have a harsh cough or No if you don't.")
    q1 = input()

    if q1 == "Yes" or q1 == "yes":
        my_engine.declare(Symptoms("harsh cough"))

    #------------------------------------------------------------------------------------------------------measles
    print("Enter yes if you have brownish-pink rash or No if you don't")
    q2 = input()
    if q2 == "Yes" or q2 == "yes":
        my_engine.declare(Symptoms("brownish-pink rash"))

    print("Enter yes if you have high and fast temperature or No if you don't")
    q2 = input()
    if q2 == "Yes" or q2 == "yes":
        my_engine.declare(Symptoms("high and fast temperature"))

    print("Enter yes if you have bloodshot eyes or No if you don't")
    q2 = input()
    if q2 == "Yes" or q2 == "yes":
        my_engine.declare(Symptoms("bloodshot eyes"))

    print("Enter yes if you have white spots inside cheek or No if you don't")
    q2 = input()
    if q2 == "Yes" or q2 == "yes":
        my_engine.declare(Symptoms("white spots inside cheek"))
    #-------------------------------------------------------------------------------------------------mumps
    print("Enter yes if you have moderate temperature or no if you don't")
    q3 = input()
    if q3 == "Yes" or q3 == "yes":
        my_engine.declare(Symptoms("moderate temperature"))

    print("Enter yes if your saliva is not normal or no if you don't")
    q3 = input()
    if q3 == "Yes" or q3 == "yes":
        my_engine.declare(Symptoms("saliva is not normal"))

    print("Enter yes if you have swollen lymph nodes in neck or no if you don't")
    q3 = input()
    if q3 == "Yes" or q3 == "yes":
        my_engine.declare(Symptoms("swollen lymph nodes in neck"))

    print("Enter yes if your mouth is dry or no if not")
    q3 = input()
    if q3 == "Yes" or q3 == "yes":
        my_engine.declare(Symptoms("mouth is dry"))
    #-------------------------------------------------------------------------flu
    print("Enter yes if you have conjunctives or no if you don't")
    q4 = input()
    if q4 == "Yes" or q4 == "yes":
        my_engine.declare((Symptoms("conjunctives")))

    print("Enter yes if you have strong body aches or no if you don't")
    q4 = input()
    if q4 == "Yes" or q4 == "yes":
        my_engine.declare(Symptoms("strong body aches"))

    print("Enter yes if you have weakness or no if you don't")
    q4 = input()

    if q4 == "Yes" or q4 == "yes":
        my_engine.declare(Symptoms("weakness"))

    print("Enter yes if you have vomiting or no if you don't")
    q4 = input()

    if q4 == "Yes" or q4 == "yes":
        my_engine.declare(Symptoms("vomiting"))

    print("Enter yes if you have sore throat or no if you don't")
    q4 = input()

    if q4 == "Yes" or q4 == "yes":
        my_engine.declare(Symptoms("sore throat"))

    print("Enter yes if you have sneezing or no if you don't")
    q4 = input()

    if q4 == "Yes" or q4 == "yes":
        my_engine.declare(Symptoms("sneezing"))
    #-------------------------------------------------------------------------low sugar
    print("Are you feeling hungry")
    q5 = input()
    if q5 == 'yes' or q5 == 'Yes':
        my_engine.declare(Symptoms("hunger"))

    print("Are you shaky")
    q6 = input()
    if q6 == 'yes' or q6 == 'Yes':
        my_engine.declare(Symptoms("shakiness"))

    print("Are you pale?")
    q7 = input()
    if q7 == 'yes' or q7 == 'Yes':
        my_engine.declare(Symptoms("pale"))

    print("Do you have a headache?")
    q8 = input()
    if q8 == 'yes' or q8 == 'Yes':
        my_engine.declare(Symptoms("headache"))

    print("Are you feeling sweaty?")
    q9 = input()
    if q9 == 'yes' or q9 == 'Yes':
        my_engine.declare(Symptoms("sweating"))

    #---------------------------------------------

    print("Do you have blurred vision")
    q5 = input()
    if q5 == 'yes' or q5 == 'Yes':
        my_engine.declare(Symptoms("blurred vision"))

    print("is your mouth dry?")
    q6 = input()
    if q6 == 'yes' or q6 == 'Yes':
        my_engine.declare(Symptoms("dry mouth"))

    print("Do you have smelly breath")
    q7 = input()
    if q7 == 'yes' or q7 == 'Yes':
        my_engine.declare(Symptoms("smelly breath"))

    print("Do you have shortness of breath")
    q8 = input()
    if q8 == 'yes' or q8 == 'Yes':
        my_engine.declare(Symptoms("shortness of breath"))

    print("Are you thirsty?")
    q8 = input()
    if q8 == 'yes' or q8 == 'Yes':
        my_engine.declare(Symptoms("thirst"))'''


def plant_fun():
    print("Enter Plant Temperature: ")
    temp = input()
    print("Enter Plant Humidity: ")
    hum = input()
    print("Enter Tuber Colour: ")
    col = input()
    print("Enter Tuber shape: ")
    tub_shape = input()
    engine = plant_diagnoses()
    engine.reset()
    engine.declare(plant(temprature=temp), plant(humidity=hum), tuber(color=col), tuber(shape=tub_shape))
    engine.run()


def main_function():
    print("Enter 1 for running the Medical Expert System")
    print("or 2 running the Plant Diagnoses Expert System")
    choice = int(input())
    if choice == 2:
        plant_fun()
    elif choice == 1:
        medical_fun()


main_function()

