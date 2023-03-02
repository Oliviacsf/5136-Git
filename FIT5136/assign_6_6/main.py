from administrator import Administrator
from candidate import Candidate
from coordinator import Coordinator
from resource import Resource
from pprint import  pprint
from mission import Mission
import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore")

def start_screen():

    id_count = 0
    while id_count < 3:
        id = input('''*********************************************************************
                        Welcome to Mission to Mars System:
                        Please choose 1.log in 2. register candidate : ''')

        if int(id) < 0 or int(id) > 2:
            print('please input 1 or 2!')
            id_count += 1
        else:
            break
    if id_count >=3:
        print('error 3 times ! choose failed !')
    return int(id)
'''
    print start screen 
    input: 
    :return:username, password
'''
def print_start_screen():
    print('''*********************************************************************
                Welcome to Mission to Mars System:
                Please input your username and password''')
    username = input("Username:")
    passwd = input("Password:")
    return username,passwd

'''
    indentify username and password
    input: username, passwd
    :return str: if it is successful
'''
def user_log_in(username, passwd):
    log_admin = Administrator()
    log_coor = Coordinator()
    log_can = Candidate()
    log_count = 0
    while log_count < 3:
        if username == log_admin.get_username() and passwd == log_admin.get_passwd():
            print("log in administrator successfully!" + "\n")
            indentify_admin = 'admin_success'
            return indentify_admin
        elif username in log_coor.get_username() and passwd == log_coor.get_passwd():
            print("log in coordinator successfully!" + "\n")
            indentify_coor = 'coor_success'
            return indentify_coor
        elif username in log_can.candidate_id_list and passwd == log_can.get_passwd():
            print("log in candidate successfully!" + "\n")
            indentify_can = 'can_success'
            return indentify_can
        else:
            print("usrname or password error! please input again!")
            username = input('Username:')
            passwd = input("Password:")
            log_count += 1

    print("error 3 times ! log in failed!")
    sys.exit(1)

'''
    admin choose a shuttle
    input:
    :return: 
'''
def select_shuttle():
    resource = Resource()
    shuttle_list = resource.get_shuttle_list_name()
    pprint(shuttle_list)
    shuttle_id = input('please input shuttle id: ')
    selected_shuttle = resource.get_shuttle_entity(int(shuttle_id))
    print("your shuttle information is: ")
    print( 'id: ' + str(selected_shuttle.get_shuttle_id()) + '\n',
           'name: ' + selected_shuttle.get_name() + '\n',
           'manufacturing_year: '+  selected_shuttle.get_man_year()+'\n',
           'fuel_capacity: ' +  selected_shuttle.get_fuel_capacity() + '\n',
           'passenger_capacity: ' + str(selected_shuttle.get_passenger_capacity()) + '\n',
           'cargo_capacity: ' +  str(selected_shuttle.get_cargo_capacity()) + '\n',
           'travel_speed: ' +  str(selected_shuttle.get_travel_speed()) + '\n',
           'origin: ' + selected_shuttle.get_origin())
    return selected_shuttle.get_shuttle_id()

'''
    admin select to edit mission:
    input:
    :return:
'''
def edit_mission():

    mission_data = pd.read_csv('./database/mission_2.csv')
    mission_id_list = mission_data['mission_id'].to_list()
    decision = input('if you want to view, please input 1 , if you want to edit ,please input 2 ')
    edit_miss_id = ''
    edit_miss_id_count = 0
    while edit_miss_id_count < 3:
        for index, id in enumerate(mission_id_list):
            print(str(index) + ':' + str(id))
        edit_miss_id =  input('please select mission id: input -1 to quit')
        if int(edit_miss_id) < -1 or int(edit_miss_id) > len(mission_id_list):
            print("please input 1 or 2 or 3!")
            edit_miss_id_count += 1
        elif int(edit_miss_id) == -1:
            break
        else:
            data_value = mission_data.loc[mission_data['mission_id'] == mission_id_list[int(edit_miss_id)]].to_dict()
            print('1: mission_id: ' + str(data_value['mission_id'][int(edit_miss_id)]))
            print('2: mission_name: ' + str(data_value['mission_name'][int(edit_miss_id)]))
            print('3: mission_description: ' + str(data_value['mission_description'][int(edit_miss_id)]))
            print('4: country_of_origin: ' + str(data_value['country_of_origin'][int(edit_miss_id)]))
            print('5: countries_allowed_list: ' + str(data_value['mission_id'][int(edit_miss_id)]))
            print('6: coor_name: ' + str(data_value['coor_name'][int(edit_miss_id)]))
            print('7: jobs: ' + str(data_value['jobs'][int(edit_miss_id)]))
            print('8: employees_require: ' + str(data_value['employees_require'][int(edit_miss_id)]))
            print('9: cargo_require: ' + str(data_value['cargo_require'][int(edit_miss_id)]))
            print('10: launch_date: ' + str(data_value['launch_date'][int(edit_miss_id)]))
            print('11: destination_location: ' + str(data_value['destination_location'][int(edit_miss_id)]))
            print('12: mission_duration: ' + str(data_value['mission_duration'][int(edit_miss_id)]))
            print('13: mission_status: ' + str(data_value['mission_status'][int(edit_miss_id)]))
            break

    if edit_miss_id_count >= 3:
        print("error 3 times ! choose in failed!")
        sys.exit(1)

    if int(decision) == 1 or int(edit_miss_id) == -1:
        return
    elif int(decision) == 2:
        select_mission_id = mission_id_list[int(edit_miss_id)]
        mission_list = mission_data.columns.to_list()
        while True:
            choose_id = input('please input index that you want to edit, input -1 to quit: ')
            # for index, name in enumerate(mission_list):
            #     print(str(index) + ':' + name)
            if int(choose_id) < -1 or int(choose_id) > 14:
                print('please select in 0 and 14!')
            elif int(choose_id) == -1:
                break
            else:
                content =  input('please input your' + ' ' + mission_list[int(choose_id)] + ': ')
                mission_data[mission_list[int(choose_id)]][mission_data['mission_id'] == select_mission_id] = content
                print('edit successful !')
                mission_data.to_csv('./database/mission_2.csv', index=False)




'''
    find a replace candidate
'''
def find_replace_can(mission_name):
    res_can = Resource()
    pprint(res_can.get_candidate_name_list())
    replace_can_id = input("please choose one candidate id for replacement: ")
    replace_can = Candidate(int(replace_can_id))
    replace_can.set_received_offer(mission_name)
    print('successful send!')


'''
    admin view mission have two tasks
'''
def admin_view_mission():
    mission_data = pd.read_csv('./database/mission_2.csv')
    edit_miss_id_count = 0
    edit_miss_id = ''
    miss_id_list = mission_data['mission_id'].tolist()
    while edit_miss_id_count < 3:

        for index, id in enumerate(miss_id_list):
            print(str(index) +' :'+ str(id))
        edit_miss_id =  input("please choose mission index that you want to view: ")
        if int(edit_miss_id) < 0 or int(edit_miss_id) > len(miss_id_list)-1:
            print('please input in these id!')
            edit_miss_id_count += 1
        else:
             break
    if edit_miss_id_count >= 3:
        print("error 3 times ! view  failed!")
        sys.exit(1)
    edit_miss_entity_count = 0
    while edit_miss_entity_count < 3:
        #edit_miss_entity = edit_res.get_mission_entity(int(edit_miss_id))
        next_move = input("please choose from this two selection: "+'\n' +
                          '1. see if mission has a shuttle' + '\n'+
                           '2: if candidate reject selection: ')
        if int(next_move) == 1:
            if mission_data['has_shuttle'][mission_data['mission_id'] == miss_id_list[int(edit_miss_id)]].tolist()[0] == 0:
                print("this mission doesnt have a shuttle, please select one")
                select_id = select_shuttle()
                mission_data['has_shuttle'][mission_data['mission_id'] == miss_id_list[int(edit_miss_id)]] = int(select_id)
                print('select successful!')
                mission_data.to_csv('./database/mission_2.csv',index=False)
                break
            else:
                print('this mission already have a shuttle!')
                break
        elif int(next_move) == 2:
            if mission_data['can_reject'][mission_data['mission_id'] == miss_id_list[int(edit_miss_id)]].tolist()[0] == True:
                print('your mission is rejected by candidate,please find a replacement candidate')
                can_data = pd.read_csv('./database/candidates.csv')
                can_id_list = can_data['identification'].to_list()
                for index, id in enumerate(can_id_list):
                    print(str(index) + ':' + str(id))
                choose_id = input('please choose candidate that you want')
                mission_name =mission_data['mission_name'][mission_data['mission_id'] == miss_id_list[int(edit_miss_id)]].to_list()[0]
                can_data['received_offer'][can_data['identification'] == can_id_list[int(choose_id)]] += ',' + mission_name
                can_data.to_csv('./database/candidates.csv',index=False)
                print('send successful !!')
                break
            else:
                print('candidate accept your mission')
                break
        else:
            print('please choose between 1 and 2!' + '\n')
            edit_miss_entity_count += 1
    if edit_miss_entity_count > 3:
        print("error 3 times ! choose failed!")
        sys.exit(1)

'''
    admin choose to view mission or edit mission
'''
def select_mission():

    select_count = 0
    while select_count < 3:
        print('welcome to administrator screen ! ')
        mission_index = input("pleas choose view mission or edit mission"+ "\n" +
                              "1. view mission" + "2. edit mission " + "3 .quit ")
        if int(mission_index) == 1:
            admin_view_mission()
        elif int(mission_index) == 2:
            edit_mission()
        elif int(mission_index) == 3:
            sys.exit(1)
        else:
            print("please input 1 or 2!")
            select_count += 1
    print("error 3 times ! select in failed!")
    sys.exit(1)


'''
    it is the function of administrator
    input: identity of admin
    return:
'''
def admin_screen():
    #if identity == 'admin_success':
        select_mission()

def create_mission():

    mission_list = []
    id = input('please input your mission id: ')
    mission_list.append(int(id))
    print('create successful!')

    miss_name = input('please input your mission name: ')
    mission_list.append(miss_name)
    print('create successful!')

    mission_description = input('please input your mission mission_description: ')
    mission_list.append(mission_description)
    print('create successful!')

    country_of_origin = input('please input your mission country_of_origin: ')
    mission_list.append(country_of_origin)
    print('create successful!')

    countries_allowed_list = input('please input your mission countries_allowed: ')
    mission_list.append(countries_allowed_list)
    print('create successful!')

    coor_name = input('please input your mission coor_name: ')
    mission_list.append(coor_name)
    print('create successful!')

    jobs = input('please input your mission jobs: ')
    mission_list.append(jobs)
    print('create successful!')

    employees_require = input('please input your mission employees_require: ')
    mission_list.append(employees_require)
    print('create successful!')

    cargo_require = input('please input your mission cargo_require: ')
    mission_list.append(cargo_require)
    print('create successful!')


    launch_date = input('please input your mission launch_date: ')
    mission_list.append(launch_date)
    print('create successful!')

    destination_location = input('please input your mission destination_location: ')
    mission_list.append(destination_location)
    print('create successful!')

    mission_duration = input('please input your mission mission_duration: ')
    mission_list.append(mission_duration)
    print('create successful!')

    mission_status = input('please input your mission mission_status: ')
    mission_list.append(mission_status)
    print('create successful!')


    mission_list.append(0)
    mission_list.append(False)
    data = pd.read_csv('./database/mission_2.csv')
    row = data.shape[0]
    data.loc[row + 1] = mission_list
    data.to_csv('./database/mission_2.csv', index=False)
'''
    coordinate screen
'''
def coor_screen():
    coor_id_count = 0
    while coor_id_count < 3:
        print('welcome to coordinate screen ! ')
        coor_id = input("1.create mission 2. view mission or edit mission 3. quit")
        if int(coor_id) == 1:
            create_mission()

        elif int(coor_id) == 2:
            edit_mission()
        elif int(coor_id) == 3:
            sys.exit(1)
        else:
            print('please input 1 or 2!')
            coor_id_count += 1
    print('error 3 times! select failed !')
    sys.exit(1)


'''
    edit profile
'''
def edit_profile(username):
    candidate_data = pd.read_csv('./database/candidates.csv')
    select_id = ''
    while True:
        select_id = input('input 1 to view profile, input 2 to edit profile, input -1 to quit: ')
        if int(select_id) == -1:
            break
        else:
            index = int(candidate_data.index[candidate_data['identification'] == int(username)][0])
            data_value = candidate_data.loc[candidate_data['identification'] == int(username)].to_dict()
            print('1: ' + 'identification: ' + str(data_value['identification'][index]))
            print('2: ' + 'name: ' + str(data_value['name'][index]))
            print('3: ' + 'date of birth: ' + str(data_value['date of birth'][index]))
            print('4: ' + 'street: ' + str(data_value['street'][index]))
            print('5: ' + 'country: ' + str(data_value['country'][index]))
            print('6: ' + 'identification type: ' + str(data_value['identification type'][index]))
            print('7: ' + 'gender: ' + str(data_value['gender'][index]))
            print('8: ' + 'allergies: ' + str(data_value['allergies'][index]))
            print('9: ' + 'food preferences: ' + str(data_value['food preferences'][index]))
            print('10: ' + 'qualifications: ' + str(data_value['qualifications'][index]))
            print('11: ' + 'years of work experience: ' + str(data_value['years of work experience'][index]))
            print('12: ' + 'occupation: ' + str(data_value['occupation'][index]))
            print('13: ' + 'computer skills: ' + str(data_value['computer skills'][index]))
            print('14: ' + 'languages known: ' + str(data_value['languages known'][index]))
            if int(select_id) == 2:
                break

    if int(select_id) == 1 or int(select_id) == -1:
        return

    elif int(select_id) == 2:

        select_id_text_count = 0
        while select_id_text_count < 3:
            select_id_text = input('please select number that you want to edit, input -1 to quit')
            if int(select_id_text) >=1 and int(select_id_text) <= 14:
                column_name = ['identification','name','date of birth','street','country','identification type',
                               'gender','allergies','food' 'preferences','qualifications','years of work experience',
                               'occupation','computer skills','languages known']
                edit_value = input('please input your' + ' ' + column_name[int(select_id_text)-1]+' ')
                candidate_data[column_name[int(select_id_text)-1]][candidate_data['identification'] == int(username)] = edit_value
                candidate_data.to_csv('./database/candidates.csv',index=False)
                print('edit successful !')
            elif int(select_id_text) == -1:
                break
            else:
                print('please select between 1 and 14!')
                select_id_text_count += 1
        if select_id_text_count >= 3:
            print('error 3 times !, select failed!')
            sys.exit(1)

'''
    select offer
'''
def select_offers(username):
    candidate_data_offer = pd.read_csv('./database/candidates.csv')
    str_miss = candidate_data_offer['received_offer'][candidate_data_offer['identification'] == username].to_list()[0]
    offer_list = str_miss.split(',')
    offer_list = set(offer_list)
    offer_list = list(offer_list)
    print('your received offer is ')
    for index, offer in enumerate(offer_list):
        print(str(index) + ": "  + offer)
    while True:
        receive_offer = input('please input your reveived offer, input -1 to quit: ')
        if int(receive_offer) == -1:
            break
        else:
            mission_reveive = pd.read_csv('./database/mission_2.csv')
            mission_reveive['can_reject'][mission_reveive['mission_name'] == offer_list[int(receive_offer)]] = False
            print('receive successful!')
            mission_reveive.to_csv('./database/mission_2.csv',index=False)

    while True:
        reject_offer = input('please input your reject offer, input -1 to quit: ')
        if int(reject_offer) == -1:
            break
        else:
            mission_reveive = pd.read_csv('./database/mission_2.csv')
            mission_reveive['can_reject'][mission_reveive['mission_name'] == offer_list[int(reject_offer)]] = True
            print('reject successful!')
            mission_reveive.to_csv('./database/mission_2.csv', index=False)

    #reject_offer = input('please input your reject offer')

'''
    candidate screen
'''
def can_screen(username):
    can_id_count = 0
    while can_id_count < 3:
        print('welcome to candidate screen ! ')
        coor_id = input("1.view or edit profile 2. select offers 3. quit: ")
        if int(coor_id) == 1:
            edit_profile(username)

        elif int(coor_id) == 2:
            select_offers(username)
        elif int(coor_id) == 3:
            sys.exit(1)
        else:
            print('please input 1 or 2!')
            can_id_count += 1
    print('error 3 times! select failed !')
    sys.exit(1)

def add_column():
    column_name = ['identification', 'name', 'date of birth', 'street', 'country', 'identification type',
                   'gender', 'allergies', 'food' 'preferences', 'qualifications', 'years of work experience',
                   'occupation', 'computer skills', 'languages known']
    can_reg = []
    for name in column_name:
        temp = input('please input your ' + name + ': ')
        can_reg.append(temp)
    return can_reg
'''
    candidate register
'''
def register_can():
    name_list = add_column()
    name_list.append('False')
    name_list.append('False')
    name_list.append('')

    can_data = pd.read_csv('./database/candidates.csv')
    row = can_data.shape[0]
    can_data.loc[row + 1] = name_list
    can_data.to_csv('./database/candidates.csv',index=False)
    print('register successful !')

    while True:
        choose = input('please choose 1. edit or view profile 2. quit')
        if int(choose) == 1:
            edit_profile(name_list[0])
        elif int(choose) == 2:
            sys.exit(1)
        else:
            print('Please input between 1 or 2!')




if __name__ == "__main__":

    number = start_screen()
    if number == 1:
        log_usrname, log_passwd = print_start_screen()
        log_in_identity = user_log_in(log_usrname,log_passwd)

        if log_in_identity == 'admin_success':
            admin_screen()
        elif log_in_identity == 'coor_success':
            coor_screen()
        elif log_in_identity == 'can_success':
            can_screen(int(log_usrname))
    elif number == 2:
        register_can()