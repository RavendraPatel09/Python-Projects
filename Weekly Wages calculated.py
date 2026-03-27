hours=int(input('Enter the number of hours worked: '))#Input number of hours worked
days=int(input('Enter the days works: '))#Input number of days worked
wages_per_hour=int(input('Enter the wage per hour: '))#Input wage per hour
total_wages=sum(hours*wages_per_hour for _ in range(days))#Calculate total wages
if hours <=40:
    total_wages=hours*total_wages
print(total_wages)# this is used to cal the total amount of money for the working hours
#this is the program to calculate weekly wages based on hours worked, days worked, and wage per hour