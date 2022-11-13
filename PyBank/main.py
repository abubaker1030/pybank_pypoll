import csv

months = []
profitLoss = []
with open("C:/Users/Personel/Desktop/Project1/PyBank/Resources/budget_data.csv", 'r') as file:
    data = csv.reader(file)
    for row in data:
        months.append(row[0])
        profitLoss.append(row[1])

profitLoss = [float(number) for number in profitLoss[1:]]
months = [single_date for single_date in months[1:]]
previousMonthProfit = 0
monthlyChanges = [0]
for index in range(1,len(profitLoss)):
    currentMonth = float(profitLoss[index])
    monthlyChange = currentMonth - previousMonthProfit
    monthlyChanges.append(monthlyChange)
    previousMonthProfit = currentMonth
print(len(monthlyChanges))
maxIndex = monthlyChanges.index(max(monthlyChanges))
minIndex = monthlyChanges.index(min(monthlyChanges))
print(monthlyChanges)
print('Financial Analysis')
print('-------------------------')
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profitLoss)}")
print(f"Average Change: ${(sum(monthlyChanges)-profitLoss[0])/len(months)}")
print(f"Greatest Increase in Profit: {months[maxIndex]} {max(monthlyChanges)}")
print(f"Greatest Decrease in Profit: {months[minIndex]} {min(monthlyChanges)}")

with open('C:/Users/Personel/Desktop/Project1/PyBank/Analysis/financial_analysis.txt', 'w') as text:
    text.write('Financial Analysis\n')
    text.write('-------------------------\n')
    text.write(f"Total Months: {len(months)}\n")
    text.write(f"Total: ${sum(profitLoss)}\n")
    text.write(f"Average Change: ${(sum(monthlyChanges)-profitLoss[0])/len(months)}\n")
    text.write(f"Greatest Increase in Profit: {months[maxIndex]} {max(monthlyChanges)}\n")
    text.write(f"Greatest Decrease in Profit: {months[minIndex]} {min(monthlyChanges)}\n")
