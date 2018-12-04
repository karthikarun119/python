import json
from configparser import ConfigParser
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import os
import sys
from Project import Project
from Employee import Employee


cfg = ConfigParser()

cfg['Dhivakar Kanagaraj'] = {'inr': 500, 'dollar': 7.05}
cfg['Harshvardhan Suresh'] = {'inr': 700, 'dollar': 9.87}
cfg['Senthil Palanisamy'] = {'inr': 800, 'dollar': 11.28}
cfg['Shivaraj Magadi'] = {'inr': 950, 'dollar': 13.39}

with open('config.ini', 'w') as configfile:
    cfg.write(configfile)
emp_file = pd.read_csv(
                     'C:/Users/arunkarthik.p/Downloads/time_entry_weekly.csv'
                      )
employees = emp_file['User']
data = len(emp_file)
tags = emp_file['Tags']
duration = emp_file['Duration']
client = emp_file['Client']

project = emp_file['Project']
p = Project(employees, tags, duration, project, cfg, data)
E = Employee(employees, tags, duration, project, cfg, data)
print("================Project Weekly Billing====================")
while True:
    print("ENTER THE OPTIONS")
    print("1) PROJECT SUMMARY 2) EMPLOYEE SUMMARY  3) EXIT ")
    option = int(input())
    if(option == 1):
        while True:
            try:
                print("1) Activity summary of total \
                       time spent in EACH project (tags vs employee)\
                     \n2) Bar Chart for particular project\
                      (employee vs billing amount)\
                     \n3) Employee summary of total time spent\
                      in each project (project vs employee)\
                     \n4) Generate Report For Project in JSON FORMAT\
                     \n5) Back \n6) EXIT")
                print("Enter the option")
                option2 = int(input())
                if(option2 == 1):
                    print("Activity summary of total time\
                     spent in EACH project (tags vs employee)")
                    result_dict = p. calculate_acitivity_summary()
                    if(result_dict is False):
                        print("INVALID PROJECT ID")
                        break

                    new_dict = {}
                    for x in result_dict:
                        new_dict = result_dict[x]
                        print("PROJECT ID--------------------------->%s" % x)
                        res = pd.DataFrame(new_dict)
                        print(res)
                elif(option 2 == 2):
                    print("Enter the project id")
                    project_id = input()
                    print(" Bar Chart for particular project\
                            (employee vs billing amount)")
                    main_dict = p.display_bar_chart(project_id)
                    res = pd.DataFrame(main_dict)
                    res.plot(kind='bar')
                    plt.show()
                elif option2 == 3:
                    main_dict = p.calculate_employee_summary()
                    res = pd.DataFrame(main_dict)
                    print(res)
                elif option2 == 4:
                    p.project_report_json(
                        p.calculate_acitivity_summary(), client)

                elif option2 == 5:
                    break
                elif option2 == 6:
                    os._exit(0)
                else:
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXX\
                    ---InValid option---XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    pass
            except SystemExit:
                print("bye")
    elif option == 2:
        while True:
            try:
                print("1) Activity summary of total time spent\
                       in ALL Employee (tags vs employee) \
                      \n2) Bar Chart for particular Employee\
                        (project vs billing amount)\
                      \n3) project summary of total time spent\
                         by each Employee (project vs employee)\
                        \n4) back\n5) EXIT")
                print("Enter the option")
                option2 = int(input())
                if(option2 == 1):
                    main_dict = E.calculate_acitivity_summary()
                    print("\t\tTotal Hours spend by Employee in each Tags ")
                    for x in main_dict:
                        print(x)
                        for y in main_dict[x]:
                            print(f"\t { y : 25}-------------------->\
                                   {main_dict[x][y]:50} ")
                elif(option2 == 2):
                    print("Enter the employee name")
                    emp_name = input()
                    main_dict = E.display_bar_chart(emp_name)
                    print("PROJECT VS BILLING AMOUNT IN RUPEES ")

                    res = pd.DataFrame(main_dict)
                    res.plot(kind='bar')
                    plt.show()
                elif option2 == 3:
                    print("Enter the option  \n \
                          1)FOR PARTICULAR EMPLOYEE \
                          2) FOR ALL EMPLOYEE")
                    option3 = int(input())
                    main_dict = E.calculate_project_summary(option3)
                    for x in main_dict:
                        print(x)
                        for y in main_dict[x]:
                            print(f"\t {y : 25}-------------------->\
                                  {main_dict[x][y]:50} ")
                elif option2 == 5:
                    break
                elif option2 == 6:
                    os._exit(0)
                else:
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXX\
                         ---InValid option---\
                          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    pass
            except SystemExit:
                print("bye")
    elif option == 3:
        os._exit(0)
    else:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXX\
              ---InValid option---\
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        pass
