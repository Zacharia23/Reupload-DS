import pandas as pd

read_file = pd.read_excel(r'SMS Report-21.xlsx')
read_file.columns("Message", "Sent To", "SMS Size", "Delivery Status", "Sent At")
read_file.to_csv(r'outupt_report.csv', index=None, header=True)
