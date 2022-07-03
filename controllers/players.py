from datetime import datetime, date
from models.players import Player


def create_player():
    list_player = []
    stop = False
    while not stop :
        try:

            nb_player = int(input("Please enter the number of players you want to create: "))
            stop = True
        except:
            print("Please enter a number ")
        else:
            for i in range(nb_player):
                stop_rank = False
                stop_score = False
                stop_dob = False
                last_name = input("Please enter player {} last name: ".format(i+1))
                first_name = input("Please enter player {} first name: ".format(i+1))
                while not stop_dob:
                    try:
                        dob = datetime.strptime(input("Please enter player {} date of birth in (DD/MM/YYYY): ".format(i+1)), "%d/%m/%Y").strftime("%d/%m/%Y")# a travailler
                        stop_dob = True
                    except:
                        print("Please enter player's date of birth in format (DD/MM/YYYY")
                sex = input("Please enter player {} sex: ".format(i+1))
                while not stop_rank:
                    try:
                        rank = int(input("Please enter player {} rank: ".format(i+1)))
                        stop_rank = True
                    except:
                        print("Attributed rank should be a number")
                while not stop_score:
                    try:
                        score = int(input("Please enter player {} score: ".format(i+1)))
                        stop_score = True
                    except:
                        print("Attributed score should be a number")

                p = Player(i, last_name, first_name, dob, sex, rank, score)
                print(p)
                list_player.append(p)
            return list_player

def save_player_in_db(list_player, player_table):
    choice = input('Would you like to eraze the content of this table? Type Y for yes ')
    if choice == 'Y':
        player_table.truncate()
    for p in list_player:
        player_table.insert({'Last name':p.last_name, 'First name': p.first_name, 'Date of birth': p.dob, 'Sex':p.sex, 'Rank':p.rank, 'Score':p.score})

def ordre(ditc_player):
    return ditc_player ['Rank']

    
def player_classment(list_player):
    if len(list_player) != 8:
        return "We are sorry we can't start a tournament, the number of players has to be 8 and not {}".format(len(list_player))
    else:
        return sorted(list_player,key = ordre)


def make_match(list_player_ranking):
    if isinstance(list_player_ranking, list):
        return list(zip(list_player_ranking[:4], list_player_ranking[4:]))
