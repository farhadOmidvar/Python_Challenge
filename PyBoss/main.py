# PyBoss
# Import Dependencies
import csv
import os
from datetime import datetime

us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA',
    'Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI',
    'Idaho': 'ID','Illinois': 'IL','Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS',
    'Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM',
    'New York': 'NY','North Carolina': 'NC','North Dakota': 'ND', 'Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT',
    'Virginia': 'VA','Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',}
# Open CSV file to read and a CSV file to write
csv_path = os.path.join('employee_data.csv')
with open(csv_path, 'r') as csv_file,\
	open('new_employee_data.csv', 'w' , newline='') as out_csv_file:

	employee_data = csv.reader(csv_file, delimiter=',')
	new_employee_data = csv.writer(out_csv_file)
	employee_data_header = next(employee_data)
	# Write new header
	new_employee_data.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

	for row in employee_data:
		emp_id,name,dob,ssn,state = row
		# The Name column split into separate First Name and Last Name columns.
		first_name = name.split()[0]
		last_name = name.split()[1]
		# The DOB data be re-written into MM/DD/YYYY format.
		date_of_birth = datetime.strptime(dob,'%Y-%m-%d').strftime('%m/%d/%Y')
		# The SSN data re-written such that the first five numbers are hidden from view.
		s_s_n = '***-**-'+ ssn.split('-')[2]
		# The State data be re-written as simple two-letter abbreviations.
		n_state = us_state_abbrev[state]
		# Write new rows
		new_employee_data.writerow([emp_id,first_name,last_name,date_of_birth,s_s_n,n_state])


	




