hours=int(input('Enter the number of hours worked: '))#Input number of hours worked
days=int(input('Enter the days works: '))#Input number of days worked
wages_per_hour=int(input('Enter the wage per hour: '))#Input wage per hour
total_wages=sum(hours*wages_per_hour for _ in range(days))
if hours <=40:
    total_wages=hours*total_wages
print(total_wages)
