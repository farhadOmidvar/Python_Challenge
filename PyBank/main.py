#PyBank
#Import Dependencies
import os
import csv

#Open CSV file to read and a text file to write
csv_path = os.path.join('Resources','budget_data.csv')
with open (csv_path, 'r') as csv_file,\
	open('financial_analysis.txt', 'w') as text_file:
	
	#Read CSV file
	budget_data = csv.reader(csv_file, delimiter=",")
	
	#Skip header
	budget_data_header = next(budget_data)
	
	#Creat empty lists and dictionary
	months = list()
	profit_loss = list()
	profit_loss_date = dict()
	i = 0
	
	#Loop throught each row of CSV file
	for row in budget_data:
		#Store months and revenue in a list
		months.append(row[0])
		profit_loss.append(int(row[1]))
		#Store revenue changes per month as key:value in a dictionary
		if i == 0:
			profit_loss_date[0] = months[i]
		else:
			profit_loss_date[profit_loss[i] - profit_loss[i-1]] = months[i]
		i += 1
	
	#Find The total number of months	
	total_months = len(months)
	#Find The total net amount of "Profit/Losses" over the entire period
	total_profit_loss = sum(profit_loss)
	#Find the average change in "Profit/Losses" between months over the entire period
	average_change = round((sum(profit_loss_date)/(total_months - 1)),2)
	#Find the greatest increase in profits (date and amount) over the entire period
	greatest_inc = max(profit_loss_date)
	greatest_inc_date = profit_loss_date.get(greatest_inc,0)
	#Find the greatest decrease in losses (date and amount) over the entire period
	greatest_dec = min(profit_loss_date)
	greatest_dec_date = profit_loss_date.get(greatest_dec,0)

	analysis =f"""
	Financial Analysis
	-------------------------
	Total Months: {total_months}
	Total: ${total_profit_loss}
	Average Change: ${average_change}
	Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})
	Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})
	"""
	#Write the Financial Analysis as a text file
	text_file.write(analysis)
	
	#Print the Financial Analysis to the terminal
	print(analysis)

	

