import random
import  math
from matplotlib import pyplot as plt
import numpy as np

# simulation of service
def formula(employees):  
    potential_customers = np.random.binomial(n=175200, p=0.2)     

    capacity = (employees * 5) * 365                 
    line = max(0, potential_customers - capacity)    
    if capacity > 0:
        wait_time = (line / capacity)                   
    else:                                             
        wait_time = 60
 
    k = 0.05 # impatience factor
    satisfaction = 100 * math.exp(-k * wait_time)  
    customer_retention = math.exp(-k * wait_time)  

    actual_customers = potential_customers * customer_retention    

    revenue = actual_customers * 50                        
    daily_wage = 15 * 8                                    
    payroll_cost = (employees * daily_wage) * 365          
    profit = revenue - payroll_cost                      
    
    return wait_time, revenue, payroll_cost, profit, satisfaction


for employees in range(1, 21):
    wait_time, revenue, payroll_cost, profit, satisfaction = formula(employees)
    print(f"{employees:<9} | {wait_time:<8.3f}mins | ${revenue:<11,} | ${payroll_cost:<11,} | ${profit:<11,}| %{satisfaction:<12}")




employees_list = [] #                          
profits_list = [] #                            
satisfaction_list = [] #                      


#monte carlo averaging:
for employees in range (1,21):
    runtimes = 10000            
    sum_profit = 0
    sum_satisfaction = 0

    for x in range(runtimes):
        wait_time, revenue, payroll_cost, profit,satisfaction = formula(employees)  
        sum_profit += profit
        sum_satisfaction += satisfaction

    avg_profit = sum_profit / runtimes                         
    avg_satisfaction = sum_satisfaction / runtimes                       

    employees_list.append(employees)
    profits_list.append(avg_profit)
    satisfaction_list.append(avg_satisfaction)


plt.plot(employees_list, profits_list,)  #  employees vs profit grpah
plt.title('Employees vs Profit')
plt.xlabel("Employees")
plt.xticks(range(1,21))
plt.ylabel ('Profit')
plt.show()

plt.plot(satisfaction_list, employees_list)  # satisfaction vs employees graph
plt.title('Satisfaction vs Employees')
plt.xlabel("Satisfaction")
plt.yticks(range(1,21))
plt.ylabel ('Employees')
plt.show()

plt.plot(satisfaction_list, profits_list)  #   satisfaction vs profits graph
plt.title('Satisfaciton vs Profit')
plt.xlabel("Satisfaciton")
plt.ylabel ('Profit')
plt.show()
