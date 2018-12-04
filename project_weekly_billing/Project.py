import matplotlib.pyplot as plt
import pandas as pd
import json
import datetime
from configparser import ConfigParser

cfg = ConfigParser()
cfg['Dhivakar Kanagaraj'] = {'inr': 500, 'dollar': 7.05}
cfg['Harshvardhan Suresh'] = {'inr': 700, 'dollar': 9.87}
cfg['Senthil Palanisamy'] = {'inr': 800, 'dollar': 11.28}
cfg['Shivaraj Magadi'] = {'inr': 950, 'dollar': 13.39}

with open('config.ini', 'w') as configfile:
    cfg.write(configfile)


class Project:

    def __init__(self, employees, tags, duration, project, cfg, data):
            self.employees = employees
            self.tags = tags
            self.duration = duration
            self.project = project
            self.cfg = cfg
            self.data = data

    def calculate_acitivity_summary(self):
            index_tags = []
            index_employees = []
            temp_dic = {}
            main_dict = {}
            index_project = []
            result_dict = {}
            for i in range(0, self.data, 1):
                if self.tags[i] not in index_tags:
                    index_tags.append(self.tags[i])
                if self.project[i] not in index_project:
                    index_project.append(self.project[i])
                if self.employees[i] not in index_employees:
                    index_employees.append(self.employees[i])
            list1 = []
            for r in range(0, len(index_project)):
                for i in range(0, len(index_employees)):
                    for j in range(0, len(index_tags)):
                        for k in range(0, self.data):
                            if (self.tags[k] == index_tags[j]) and\
                               (self.employees[k] == index_employees[i])and\
                               (self.project[k] == index_project[r]):
                                list1.append(self.duration[k])
                            else:
                                pass
                        timeList = list1
                        sum = datetime.timedelta()
                        for e in timeList:
                            (h, m, s) = e.split(':')
                            d = datetime.timedelta(hours=int(h),
                                                   minutes=int(m),
                                                   seconds=int(s))
                            sum += d
                        if(str(sum) == '0:00:00'):
                            temp_dict[index_tags[j]] = "-"
                        else:
                            temp_dict[index_tags[j]] = str(sum)
                        list1 = []
                    main_dict[index_employees[i]] = temp_dict
                    temp_dict = {}
                result_dict[index_project[r]] = main_dict
                main_dict = {}
            return result_dict

    def calculate_employee_summary(self):
            index_project = []
            index_employees = []
            temp_dict = {}
            main_dict = {}
            for i in range(0, self.data, 1):
                if self.project[i] not in index_project:
                    index_project.append(self.project[i])
                if self.employees[i] not in index_employees:
                    index_employees.append(self.employees[i])    
            list1 = []           
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

    def display_bar_chart(self, project_id):
            index_employees = [] 
            index_project = []
            try:
                for i in range(0, self.data, 1):
                    if self.employees[i] not in index_employees:
                        index_employees.append(self.employees[i])
                    if self.project[i] not in index_project:
                        index_project.append(self.project[i])
                if project_id not in index_project:
                    return False
                print(len(self.cfg))
                list1 = []
                temp_dict = {}
                temp_dict1 = {}
                dollar_dict = {}
                main_dict = {}
                for i in range(0, len(index_employees), 1):
                    for j in range(0, len(index_project), 1):
                        for k in range(0, self.data, 1):
                            if (self.project[k] == project_id) and\
                               (self.employees[k] == index_employees[i]):
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
                        bill_amount_pr_hr_inr = cfg.getfloat(index_employees[i], 'inr')
                        bill_amount_inr = round((result / 3600) *
                                                bill_amount_pr_hr_inr, 2)
                        bill_amount_pr_hr_dollar = cfg.getfloat(index_employees[i], 'dollar')
                        bill_amount_dollar = round((result/3600) * 
                                                   bill_amount_pr_hour_dollar, 2)                  
                        temp_dict[project_id] = bill_amount_inr
                        temp_dict1[project_id] = bill_amount_dollar
                        list1 = []
                    main_dict[index_employees[i]] = temp_dict  
                    dollar_dict[index_employees[i]] = temp_dict1 
                    temp_dict = {}
                    temp_dict1 = {}
                print("EMPLOYEES VS BILLING AMOUNT IN DOLLAR ")
                res = pd.DataFrame(dollar_dict)
                res.plot(kind='bar')
                plt.show()

                return main_dict
            except Exception:
                print("INVALID PROJECT ID")

    def project_report_json(self, main_dict, client):        
        print("Enter the PROJECT ID TO GENERATE REPORT")
        project_id = input()
        list1 = []
        cli = ''
        index_tags = []
        index_employees = []
        temp_dict = {}
        main_dict = {}
        index_project = []
        result_dict = {}
        for i in range(0, self.data, 1):    
            if self.tags[i] not in index_tags:
                index_tags.append(self.tags[i])
            if self.project[i] not in index_project:
                index_project.append(self.project[i])
            if self.employees[i] not in index_employees and\
               self.project[i] == project_id:
                index_employees.append(self.employees[i])
            if self.project[i] == project_id:
                cli = client[i]
        for r in range(0, len(index_project)):                
            for i in range(0, len(index_employees)):
                for j in range(0, len(index_tags)):
                    for k in range(0, self.data):                        
                        if (self.tags[k] == index_tags[j]) and\
                           (self.employees[k] == index_employees[i])and\
                           (self.project[k] == project_id):              
                            list1.append(self.duration[k])
                        else:
                            pass
                    timeList = list1
                    sum = datetime.timedelta()
                    for e in timeList:
                        (h, m, s) = e.split(':')                           
                        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        sum += d
                    if(str(sum) == '0:00:00'):                            
                        temp_dict[index_tags[j]] = "-"
                    else:
                        temp_dict[index_tags[j]] = str(sum)
                    list1 = []
                main_dict[index_employees[i]] = temp_dict  
                temp_dict = {}
            result_dict[project_id] = main_dict
            main_dict = {}
        timelist1 = []
        emp = {}
        final_list = []
        project_duration = []
        for x in result_dict:
            project_name = x
            for y in result_dict[x]:
                for z in result_dict[x][y]:
                    if result_dict[x][y][z] == '-':
                        pass
                    else:
                        timelist1.append(result_dict[x][y][z])
                        project_duration.append(result_dict[x][y][z])
                timeList = timelist1
                totalSecs = 0
                for tm in timeList:
                    timeParts = [int(s) for s in tm.split(':')]
                    totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
                totalSecs, s = divmod(totalSecs, 60)
                h, m = divmod(totalSecs, 60)
                result = int(h) * 3600 + int(m) * 60 + int(s)
                total_time = str(h)+':'+str(m)+':'+str(s)
                bill_amount_per_hour_inr = cfg.getfloat(y, 'inr')
                bill_amount_inr = round((result/3600) * bill_amount_per_hour_inr, 2)
                bill_amount_per_hour_dollar = cfg.getfloat(y, 'dollar')
                bill_amount_dollar = round((result/3600) * bill_amount_per_hour_dollar, 2)
                emp['NAME'] = y
                emp['HOURS SPENT'] = total_time
                emp['BILLING_AMOUNT_INR'] = bill_amount_inr
                emp['BILLING_AMOUNT_DOLLAR'] = bill_amount_dollar
                timelist1 = []
                final_list.append(emp)
                emp = {}
        timeList2 = project_duration
        sum = datetime.timedelta()
        for e in timeList2:
            (h, m, s) = e.split(':')                           
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d            
        project_dur = str(sum)          
        report = {}
        report['Project ID'] = project_name
        report['TOTAL PROJECT DURATION'] = project_dur
        report['Client'] = cli
        report['Employees'] = final_list
        with open('data.json', 'w') as outfile:
            json.dump(report, outfile, indent=2)
            outfile.write('\n')