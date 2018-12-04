import matplotlib.pyplot as plt
import pandas as pd
import datetime
from configparser import ConfigParser
cfg = ConfigParser()

cfg['Dhivakar Kanagaraj'] = {'inr': 500, 'dollar': 7.05}
cfg['Harshvardhan Suresh'] = {'inr': 700, 'dollar': 9.87}
cfg['Senthil Palanisamy'] = {'inr': 800, 'dollar': 11.28}
cfg['Shivaraj Magadi'] = {'inr': 950, 'dollar': 13.39}
with open('config.ini', 'w') as configfile:
    cfg.write(configfile)


class Employee:
    def __init__(self, employees, tags, duration, project, cfg, data):
            self.employees = employees
            self.tags = tags
            self.duration = duration
            self.project = project
            self.cfg = cfg
            self.data = data

    def calculate_acitivity_summary(self):  # Dictionary - /
                                                # {tag: hours_spent}
            index_tags = []
            index_employees = []
            temp_dict = {}
            main_dict = {}
            for i in range(0, self.data, 1):
                if self.tags[i] not in index_tags:
                    index_tags.append(self.tags[i])
                if self.employees[i] not in index_employees:
                    index_employees.append(self.employees[i])
            list1 = []
            for i in range(0, len(index_employees), 1):
                for j in range(0, len(index_tags), 1):
                    for k in range(0, self.data, 1):
                        if (self.tags[k] == index_tags[j]) and \
                           (self.employees[k] == index_employees[i]):
                            list1.append(self.duration[k])
                    timeList = list1
                    sum = datetime.timedelta()
                    for e in timeList:
                        (h, m, s) = e.split(':')
                        d = datetime.timedelta(hours=int(h),
                                               minutes=int(m), seconds=int(s))
                        sum += d
                    temp_dict[index_tags[j]] = str(sum)
                    list1 = []
                main_dict[index_employees[i]] = temp_dict
                temp_dict = {}
            return main_dict

    def calculate_project_summary(self, option):
            index_project = []
            index_employees = []
            list1 = []
            temp_dict = {}
            main_dict = {}
            if(option == 1):
                print("Enter the employee name")
                emp_name = input()
                index_employees = []
                for i in range(0, self.data, 1):
                    if self.employees[i] not in index_employees:
                        index_employees.append(self.employees[i])
                    if self.project[i] not in index_project:
                        index_project.append(self.project[i])
                for i in range(0, 1, 1):
                    for j in range(0, len(index_project), 1):
                        for k in range(0, self.data, 1):
                            if (self.project[k] == index_project[j]) and\
                               (self.employees[k] == emp_name):
                                list1.append(self.duration[k])
                        timeList = list1
                        sum = datetime.timedelta()
                        for e in timeList:
                            (h, m, s) = e.split(':')
                            d = datetime.timedelta(hours=int(h),
                                                   minutes=int(m),
                                                   seconds=int(s))
                            sum += d
                        if(str(sum) == ' 0:00:00'):
                            temp_dict[index_project[j]] = "-"
                        else:
                            temp_dict[index_project[j]] = str(sum)
                        list1 = []
                    main_dict[emp_name] = temp_dict
                    temp_dict = {}
                return main_dict
            elif(option == 2):
                for i in range(0, self.data, 1):
                    if self.employees[i] not in index_employees:
                        index_employees.append(self.employees[i])
                    if self.project[i] not in index_project:
                        index_project.append(self.project[i])
                    
                for i in range(0, len(index_employees), 1):
                    for j in range(0, len(index_project), 1):
                        for k in range(0, self.data, 1):
                            if (self.project[k] == index_project[j]) and\
                               (self.employees[k] == index_employees[i]):
                                list1.append(self.duration[k])
                        timeList = list1
                        sum = datetime.timedelta()
                        for e in timeList:
                            (h, m, s) = e.split(':')
                            d = datetime.timedelta(hours=int(h), 
                                                   minutes=int(m),
                                                   seconds=int(s))
                            sum += d
                        if(str(sum) == '0:00:00'):                            
                            temp_dict[index_project[j]] = "-"
                        else:
                            temp_dict[index_project[j]] = str(sum)
                        list1 = []
                    main_dict[index_employees[i]] = temp_dict
                    temp_dict = {}
                return main_dict
                
    def display_bar_chart(self, emp_name):  
            index_employees = []  
            index_project = []
            list1 = []
            main_dict = {}
            dollar_dict = {}
            temp_dict1 = {}
            for i in range(0, self.data, 1):    
                if self.employees[i] not in index_employees:
                    index_employees.append(self.employees[i])
                if self.project[i] not in index_project:
                    index_project.append(self.project[i])   
            temp_dict = {}
 
            for i in range(0, len(index_employees), 1):
                for j in range(0, len(index_project), 1):
                    for k in range(0, self.data, 1):                        
                        if (self.project[k] == index_project[j]) and\
                           (self.employees[k] == emp_name):              
                            list1.append(self.duration[k])
                    timeList = list1
                    totalSecs = 0
                    for tm in timeList:
                        timeParts = [int(s) for s in tm.split(':')]
                        totalSecs += (timeParts[0] * 60 + 
                                      timeParts[1]) * 60 + timeParts[2]
                    totalSecs, s = divmod(totalSecs, 60)
                    h, m = divmod(totalSecs, 60)
                    result = int(h) * 3600 + int(m) * 60 + int(s)
                    bill_amount_per_hour_inr = cfg.getfloat(index_employees[i], 
                                                            'inr')

                    bill_amount_pr_hr_dollar = cfg.getfloat(index_employees[i], 
                                                            'dollar')

                    bill_amount_inr = round((result/3600) 
                                            * bill_amount_pr_hr_inr, 2)

                    bill_amount_dollar = round((result/3600) 
                                               * bill_amount_pr_hr_dollar, 2)

                    temp_dict[index_project[j]] = bill_amount_inr

                    temp_dict1[index_project[j]] = bill_amount_dollar
                    list1 = []
                main_dict[emp_name] = temp_dict
                dollar_dict[emp_name] = temp_dict1
                temp_dict = {}
                temp_dict1 = {}
            print("PROJECT VS BILLING AMOUNT IN DOLLAR ")
            res = pd.DataFrame(dollar_dict)
            res.plot(kind='bar')
            plt.show()
            return main_dict