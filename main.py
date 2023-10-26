'''

This program creates csv files of the raw data for the class project
in BSA 3620 Database Modeling, Design, & Analysis at Belmont University

By Zachary Patchen
Last Modified: 10/25/2023
'''
from faker import Faker
import random
import csv
import os
from datetime import datetime, timedelta
fake = Faker('en_US')
fake.seed_locale('en_US', 8998135)
# Specify the download folder
download_folder = '/Users/zacharypatchen/Desktop/Belmont/Databasedesign/rawData'
tenant_ids = []
property_ids = []
email_choices = ['@gmail.com', '@aol.com', '@yahoo.com', '@outlook.com']
num_properties = 100
num_maintenance_types = 10
num_occupations = 20
num_agreements = 10000
num_maintenance_statuses = 5
num_employees = 200
num_pay_methods = 3
num_pay_statuses = 3
num_maintenance_statuses = 5
payment_status_names = ['Pending', 'Paid', 'Overdue']
random.shuffle(payment_status_names)
occupation_names = [
    'Software Developer', 'Doctor', 'Teacher', 'Graphic Designer', 'Nurse', 'Engineer',
    'Writer', 'Artist', 'Architect', 'Accountant', 'Lawyer', 'Chef', 'Scientist',
    'Photographer', 'Musician', 'Entrepreneur', 'Police Officer', 'Pilot', 'Dentist',
    'Marketing Specialist', 'Real Estate Agent', 'Electrician', 'Plumber', 'Mechanic',
    'Journalist', 'Librarian', 'Carpenter', 'Interior Designer', 'Web Developer',
    'Social Worker', 'Fitness Trainer', 'Financial Advisor', 'Veterinarian', 'Actor',
    'Flight Attendant', 'Biologist', 'Geologist', 'Meteorologist', 'Pharmacist', 'Economist'
]
random.shuffle(occupation_names)  # Shuffle the list to randomize the order
property_status_names = ['Available', 'Occupied', 'Under Maintenance', 'Sold', 'Vacant', 'Leased', 'In Progress']
random.shuffle(property_status_names)
employee_type_names = ['Civil Engineer', 'Interior Designer', 'Architect', 'Safety Inspector',
                       'Site Supervisor', 'Labor', 'Clerk', 'Project Manager', 'Accountant']
random.shuffle(employee_type_names)
maintenance_status_names = ['Pending', 'Scheduled', 'In Progress', 'Completed', 'Cancelled']
random.shuffle(maintenance_status_names)
maintenance_type_names = ['Electrical', 'Plumbing', 'HVAC', 'Appliance', 'Roofing',
                          'Flooring', 'Painting', 'Carpentry', 'Pest Control', 'General Maintenance']
random.shuffle(maintenance_type_names)
payment_method_names = ['Cash', 'Credit Card', 'Check']
random.shuffle(payment_method_names)
tenants_fieldnames = ['TenantID', 'TenantFirstName', 'TenantLastName', 'TenantEmail', 'TenantPhoneNumber',
                  'TenantDOB', 'TenantSex', 'TenantCreditScore', 'TenantOccupationID']

occupations_fieldnames = ['OccupationID', 'OccupationName']

properties_fieldnames = ['PropID', 'PropName', 'PropStreet', 'PropCity', 'PropState', 'PropZip', 'PropOfficePhone',
                  'PropDateStarted', 'PropDateCompleted', 'PropSqFeet', 'PropTotalCost', 'PropValuation', 'ProStatID']

employees_fieldnames = ['EmpID', 'EmpFirstName', 'EmpLastName', 'EmpDOB', 'EmpSex', 'EmpStartDate', 'EmpEndDate', 'EmpTypeID']
prop_statuses_fieldnames = ['PropStatID', 'PropStatName']
emp_types_fieldnames = ['EmpTypeID', 'EmpTypeName']

maintenances_fieldnames = ['MaintID', 'AgmtID', 'MTypeID', 'MStatusID', 'MainReportDate', 'MaintSchedDate',
                  'MaintCompleteDate', 'MaintTotalCost', 'MaintNotes', 'EmpID']

maintenance_statuses_fieldnames = ['MStatusID', 'MStatusName']

maintenance_types_fieldnames = ['MTypeID', 'MTypeName']

rental_agreements_fieldnames = ['AgmtID', 'PUnitID', 'TenantID', 'AgmtStartDate', 'AgmtEndDate', 'AgmtMonthRentAmt',
                  'AgmtSecurityDepAmt', 'EmpID']

rental_payments_fieldnames = ['RPayID', 'TenantID', 'AgmtID', 'RPayDueDate', 'RPayAmtDue', 'RPayAmtPaid', 'PayStatusID',
                  'PayMethodID', 'PayLateFees']
payment_statuses_fieldnames = ['PayStatusID', 'PayStatusName']
payment_methods_fieldnames = ['PayMethodID', 'PayMethodName']

property_unit_fieldnames = ['PUnitID', 'PropID', 'PUnitNumber', 'PUnitSqFeet', 'PUnitNumBdrms', 'PUnitNumBaths',
                  'PUnitMonthRentAmt']
# Write property unit data to CSV file
def write_to_csv(data, fieldnames, filename):
    file_path = os.path.join(download_folder, filename)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f'{filename} data written to {file_path}')
# Function to generate fake tenant data
def generate_fake_tenant(tenant_id):
    tenant_id += random.randint(100000000000, 899999999999)
    tenant_ids.append(tenant_id)
    tenant_first_name = fake.first_name()
    tenant_last_name = fake.last_name()
    tenant_email = tenant_first_name + "."+tenant_last_name+random.choice(email_choices)
    tenant_phone_number = fake.phone_number()
    tenant_dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
    tenant_sex = random.choice(['Male', 'Female'])
    tenant_credit_score = random.randint(300, 850)
    tenant_occupation_id = random.randint(1, 20)

    return {
        'TenantID': tenant_id,
        'TenantFirstName': tenant_first_name,
        'TenantLastName': tenant_last_name,
        'TenantEmail': tenant_email,
        'TenantPhoneNumber': tenant_phone_number,
        'TenantDOB': tenant_dob,
        'TenantSex': tenant_sex,
        'TenantCreditScore': tenant_credit_score,
        'TenantOccupationID': tenant_occupation_id
    }
def generate_fake_property_unit(punit_id):
    punit_number = fake.building_number()
    punit_sq_feet = random.randint(800, 2500)
    punit_num_bdrms = random.randint(1, 5)
    punit_num_baths = random.randint(1, 3)
    punit_month_rent_amt = round(random.uniform(800, 3000), 2)
    prop_id = random.choice(property_ids)
    return {
        'PUnitID': punit_id,
        'PropID': prop_id,
        'PUnitNumber': punit_number,
        'PUnitSqFeet': punit_sq_feet,
        'PUnitNumBdrms': punit_num_bdrms,
        'PUnitNumBaths': punit_num_baths,
        'PUnitMonthRentAmt': punit_month_rent_amt
    }
def generate_fake_payment_method(pay_method_id):
    pay_method_name = payment_method_names[pay_method_id - 1]  # Assign names in order based on pay_method_id

    return {
        'PayMethodID': pay_method_id,
        'PayMethodName': pay_method_name
    }
# Function to generate fake payment status data
def generate_fake_payment_status(pay_status_id):
    pay_status_name = payment_status_names[pay_status_id - 1]  # Assign names in order based on pay_status_id

    return {
        'PayStatusID': pay_status_id,
        'PayStatusName': pay_status_name
    }
# Function to generate fake rental payment data
def generate_fake_rental_payment(rpay_id, num_pay_statuses, num_pay_methods):
    tenant_id = random.choice(tenant_ids)  # Choose tenant ID from the list
    agmt_id = random.randint(1, num_agreements)
    rpay_due_date = fake.date_this_year().strftime('%Y-%m-%d')
    rpay_amt_due = round(random.uniform(500, 9500), 2)
    rpay_amt_paid = round(random.uniform(0, rpay_amt_due), 2)
    pay_status_id = random.randint(1, num_pay_statuses)
    pay_method_id = random.randint(1, num_pay_methods)
    pay_late_fees = None if random.random() < 0.8 else round(random.uniform(10, 100),
                                                             2)  # 80% chance of having null late fees

    return {
        'RPayID': rpay_id,
        'TenantID': tenant_id,
        'AgmtID': agmt_id,
        'RPayDueDate': rpay_due_date,
        'RPayAmtDue': rpay_amt_due,
        'RPayAmtPaid': rpay_amt_paid,
        'PayStatusID': pay_status_id,
        'PayMethodID': pay_method_id,
        'PayLateFees': pay_late_fees
    }
# Function to generate fake rental agreement data
def generate_fake_rental_agreement(agmt_id, num_agreements, num_maintenance_types, num_maintenance_statuses,
                                   num_employees):
    agmt_start_date = fake.date_this_decade().strftime('%Y-%m-%d')
    end_date = fake.date_between(start_date='today', end_date='+2y')
    agmt_end_date = (end_date + timedelta(days=random.randint(1, 365 * 2))).strftime('%Y-%m-%d')
    agmt_month_rent_amt = round(random.uniform(800, 9500), 2)  # Assuming monthly rent between $800 and $9500
    agmt_security_dep_amt = round(random.uniform(500, 2000), 2)  # Assuming security deposit between $500 and $2000
    punit_id = random.randint(1, num_properties)
    tenant_id = random.choice(tenant_ids)
    emp_id = 8

    return {
        'AgmtID': agmt_id,
        'PUnitID': punit_id,
        'TenantID': tenant_id,
        'AgmtStartDate': agmt_start_date,
        'AgmtEndDate': agmt_end_date,
        'AgmtMonthRentAmt': agmt_month_rent_amt,
        'AgmtSecurityDepAmt': agmt_security_dep_amt,
        'EmpID': emp_id
    }
# Function to generate fake maintenance type data
def generate_fake_maintenance_type(mtype_id):
    mtype_name = maintenance_type_names[mtype_id - 1]  # Assign names in order based on mtype_id

    return {
        'MTypeID': mtype_id,
        'MTypeName': mtype_name
    }
# Function to generate fake maintenance status data
def generate_fake_maintenance_status(mstatus_id):
    mstatus_name = maintenance_status_names[mstatus_id - 1]  # Assign names in order based on mstatus_id

    return {
        'MStatusID': mstatus_id,
        'MStatusName': mstatus_name
    }
# Generate fake maintenance data
def generate_fake_maintenance(maint_id, num_agreements, num_maintenance_types, num_maintenance_statuses, num_employees):
    agmt_id = random.randint(1, num_agreements)
    mtype_id = random.randint(1, num_maintenance_types)
    mstatus_id = random.randint(1, num_maintenance_statuses)
    report_date = datetime.now() - timedelta(days=random.randint(1, 365 * 2))  # up to 2 years old records
    sched_date = report_date + timedelta(
        days=random.randint(1, 14))  # assuming max 14 days between report and scheduled date
    complete_date = sched_date + timedelta(days=random.randint(1, 14))  # assuming max 14 days to complete maintenance
    total_cost = round(random.uniform(50, 50000), 2)  # assuming maintenance cost between $50 and $500
    notes = fake.text() if random.random() < 0.8 else None  # 80% chance of having notes, 20% chance of being None
    emp_id = random.randint(1, num_employees)

    return {
        'MaintID': maint_id,
        'AgmtID': agmt_id,
        'MTypeID': mtype_id,
        'MStatusID': mstatus_id,
        'MainReportDate': report_date.strftime('%Y-%m-%d'),
        'MaintSchedDate': sched_date.strftime('%Y-%m-%d'),
        'MaintCompleteDate': complete_date.strftime('%Y-%m-%d'),
        'MaintTotalCost': total_cost,
        'MaintNotes': notes,
        'EmpID': emp_id
    }
# Function to generate fake employee type names
def generate_fake_emp_type(emp_type_id):
    emp_type_name = employee_type_names[emp_type_id - 1]  # Assign names in order based on emp_type_id

    return {
        'EmpTypeID': emp_type_id,
        'EmpTypeName': emp_type_name
    }
# Function to generate fake employee data
def generate_fake_employee(emp_id):
    emp_first_name = fake.first_name()
    emp_last_name = fake.last_name()
    emp_dob = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
    emp_sex = random.choice(['Male', 'Female'])
    emp_start_date = fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
    emp_end_date = random.choice([fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'), None])
    emp_type_id = random.randint(1, 9)  # Assuming you have EmpTypeID values from 1 to 9

    return {
        'EmpID': emp_id,
        'EmpFirstName': emp_first_name,
        'EmpLastName': emp_last_name,
        'EmpDOB': emp_dob,
        'EmpSex': emp_sex,
        'EmpStartDate': emp_start_date,
        'EmpEndDate': emp_end_date,
        'EmpTypeID': emp_type_id
    }
#Generates fake prop status
def generate_fake_prop_status(prop_stat_id):
    prop_stat_name = property_status_names[prop_stat_id - 1]  # Assign names in order based on prop_stat_id

    return {
        'PropStatID': prop_stat_id,
        'PropStatName': prop_stat_name
    }
# Function to generate fake property data
def generate_fake_property(prop_id):
    prop_id += random.randint(100000000000, 899999999999)
    property_ids.append(prop_id)
    prop_name = fake.company()
    prop_street = fake.street_address()
    prop_city = fake.city()
    prop_state = fake.state()
    prop_zip = fake.zipcode()
    prop_office_phone = fake.phone_number()
    prop_date_started = fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
    prop_date_completed = random.choice(
        [fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'), None])
    prop_sq_feet = random.randint(1000, 5000)
    prop_total_cost = round(random.uniform(50000, 500000), 2)
    prop_valuation = round(prop_total_cost * random.uniform(1.1, 1.5), 2)
    prop_stat_id = random.randint(1, 7)

    return {
        'PropID': prop_id,
        'PropName': prop_name,
        'PropStreet': prop_street,
        'PropCity': prop_city,
        'PropState': prop_state,
        'PropZip': prop_zip,
        'PropOfficePhone': prop_office_phone,
        'PropDateStarted': prop_date_started,
        'PropDateCompleted': prop_date_completed,
        'PropSqFeet': prop_sq_feet,
        'PropTotalCost': prop_total_cost,
        'PropValuation': prop_valuation,
        'ProStatID': prop_stat_id,
    }
# Function to generate fake occupation names
def generate_fake_occupation(occupation_id):
    occupation_name = occupation_names[occupation_id - 1]  # Assign names in order based on occupation_id

    return {
        'OccupationID': occupation_id,
        'OccupationName': occupation_name
    }

# Generate 1500 tenants
tenants = [generate_fake_tenant(i) for i in range(1, 1501)]
write_to_csv(tenants, tenants_fieldnames, 'TENANTS.csv')
#Generate fake occupations
occupations = [generate_fake_occupation(i) for i in
               range(1, num_occupations + 1)]  # Assuming occupation_id values from 1 to 20
write_to_csv(occupations, occupations_fieldnames, 'OCCUPATIONS.csv')
# Generate 1500 properties
properties = [generate_fake_property(i) for i in range(1, 1501)]
write_to_csv(properties, properties_fieldnames, 'PROPERTIES.csv')
# Generate fake property status data
prop_statuses = [generate_fake_prop_status(i) for i in range(1, 8)]  # Assuming prop_stat_id values from 1 to 7
write_to_csv(prop_statuses, prop_statuses_fieldnames, 'PROP_STATUSES.csv')
# Generate 200 employees
employees = [generate_fake_employee(i) for i in range(1, 201)]
write_to_csv(employees, employees_fieldnames, 'EMPLOYEES.csv')
# Generate fake employee type data
emp_types = [generate_fake_emp_type(i) for i in range(1, 10)]  # Assuming emp_type_id values from 1 to 9
write_to_csv(emp_types, emp_types_fieldnames, 'EMP_TYPES.csv')
# Generate 5000 maintenance records
maintenances = [
    generate_fake_maintenance(i, num_agreements, num_maintenance_types, num_maintenance_statuses, num_employees) for i
    in range(1, 5001)]
write_to_csv(maintenances, maintenances_fieldnames, 'MAINTENANCE.csv')
# Generate fake maintenance status data
maintenance_statuses = [generate_fake_maintenance_status(i) for i in range(1, num_maintenance_statuses + 1)]
write_to_csv(maintenance_statuses, maintenance_statuses_fieldnames, 'MAINTENANCE_STATUS.csv')
# Generate fake maintenance type data
maintenance_types = [generate_fake_maintenance_type(i) for i in range(1, num_maintenance_types + 1)]
write_to_csv(maintenance_types, maintenance_types_fieldnames, 'MAINTENANCE_TYPE.csv')
# Generate fake rental agreement data
rental_agreements = [
    generate_fake_rental_agreement(i, num_agreements, num_maintenance_types, num_maintenance_statuses, num_employees)
    for i in range(1, num_agreements + 1)]
write_to_csv(rental_agreements, rental_agreements_fieldnames, 'RENTAL_AGREEMENT.csv')
# Generate fake rental payment data
rental_payments = [generate_fake_rental_payment(i, num_pay_statuses, num_pay_methods) for i in
                   range(1, num_agreements + 1)]
write_to_csv(rental_payments, rental_payments_fieldnames, 'RENTAL_PAYMENTS.csv')
# Generate fake payment status data
payment_statuses = [generate_fake_payment_status(i) for i in range(1, num_pay_statuses + 1)]
write_to_csv(payment_statuses, payment_statuses_fieldnames, 'PAYMENT_STATUSES.csv')
# Generate fake payment method data
payment_methods = [generate_fake_payment_method(i) for i in range(1, num_pay_methods + 1)]
write_to_csv(payment_methods, payment_methods_fieldnames, 'PAYMENT_METHODS.csv')
# Generate fake property unit data
property_units = [generate_fake_property_unit(i) for i in range(1, num_properties + 1)]
write_to_csv(property_units, property_unit_fieldnames, 'PROPERTY_UNITS.csv')