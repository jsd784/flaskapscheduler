from datetime import date

# today = date.today()
# curr_year = int(today.strftime("%Y"))
# curr_month = int(today.strftime("%m"))

curr_month = 5
curr_year = 2021

for year in range(curr_year,curr_year+2):
    if year == curr_year:
        for month in range(curr_month,13):
            exec_date = date(year, month, 1)
            print(exec_date)
    else:
        for month in range(1,13):
            exec_date = date(year, month, 1)
            print(exec_date)
