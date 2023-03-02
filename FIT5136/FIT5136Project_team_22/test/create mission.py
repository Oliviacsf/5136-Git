from mission import Mission
import pandas as pd
def create_mission():
    """
        create mission
    """
    jobs_data = pd.read_csv('./database/jobs.csv')
    jobs_name_list = jobs_data['job_name'].to_list()
    emp_req_data = pd.read_csv('./database/emp_req.csv')
    emp_req_list = emp_req_data['emp_requirement_name'].to_list()
    cargo_data = pd.read_csv('./database/warehouse.csv')
    cargo_list = cargo_data['cargo'].to_list()

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

    job_list = []
    flag = True
    while flag:
        for index, name in enumerate(jobs_name_list, 1):
            print(str(index) + ':' + str(name))
        jobs_index = int(input('select jobs index'))
        jobs_name = jobs_name_list[jobs_index - 1]
        job_list.append(jobs_name)
        select_job = int(input('select successful! Press 1 to continue the selection, press 2 to insert next category'))
        if select_job == 1:
            continue
        elif select_job == 2:
            flag = False
    mission_list.append(job_list)
    # add employment requirement
    emp_dict = {}
    flag = True
    while flag:
        for index, name in enumerate(emp_req_list, 1):
            print(str(index) + ':' + str(name))
        emp_req_index = int(input('select employment index'))
        emp_name = emp_req_list[emp_req_index - 1]
        emp_number = int(input('please enter how many ' + emp_name + ' do you want to add'))
        emp_dict[emp_name] = emp_number
        select_emp = int(input('select successful! Press 1 to continue the selection, press 2 to insert next category'))
        if select_emp == 1:
            continue
        elif select_emp == 2:
            flag = False
    mission_list.append(emp_dict)
    # add cargo
    cargo_dict = {}
    flag = True
    while flag:
        for index, name in enumerate(cargo_list, 1):
            print(str(index) + ':' + str(name))
        cargo_index = int(input('please enter the cargo index that you want to add '))
        cargo_number = int(input('please enter how many ' + cargo_list[cargo_index - 1] + ' do you want to add'))
        if cargo_data['quantity available'][cargo_data['cargo'] == cargo_list[cargo_index - 1]].tolist()[0] > cargo_number:
            cargo_dict[cargo_list[cargo_index - 1]] = cargo_number
            select_cargo = int(input('select successful! Press 1 to continue the selection, press 2 to insert next category'))
            if select_cargo == 1:
                continue
            elif select_cargo == 2:
                flag = False
        else:
            print('sorry, the quantity of this cargo is not enough, please select again')
            inputs = input('press y to continue')
            continue
    mission_list.append(cargo_dict)

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

    has_shuttle = 0
    mission_list.append(has_shuttle)
    can_reject = False
    mission_list.append(can_reject)
    recruitment_status = False
    mission_list.append(recruitment_status)
    new_mission = Mission(mission_list[0], mission_list[1], mission_list[2], mission_list[3],
                          mission_list[4], mission_list[5], mission_list[6], mission_list[7],
                          mission_list[8], mission_list[9], mission_list[10], mission_list[11],
                          mission_list[12], mission_list[13], mission_list[14], mission_list[15])
    data = pd.read_csv('./database/mission_2.csv')
    row = data.shape[0]
    data.loc[row + 1] = mission_list
    data.to_csv('./database/mission_2.csv', index=False)

if __name__ == "__main__":
    create_mission()