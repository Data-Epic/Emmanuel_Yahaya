
import gspread

gc = gspread.service_account("gspread-sheet-2-4ebedcdae885.json")

def open_spreadsheet(spread_sheet):
    sh = gc.open(spread_sheet)
    return sh

#print(spreadsheet.sheet1.get('A1'))#


# Select a specific worksheet within the spreadsheet (optional)
def open_worksheet(spread_sheet, work_sheet):
    ws = open_spreadsheet(spread_sheet).worksheet(work_sheet)
    return ws

# Your data to be uploaded (example data)
data = [
    ['Lagos', 'Abuja', 'Oyo', 'Rivers', 'Osun'],
    [1200, 2000, 1300, 1000, 1200],
    [1000, 1800, 1100, 800, 1000],
    [1300, 1500, 1400, 1200, 1200],
    [1000, 1800, 1100, 800, 1000],
    [1000, 1800, 1100, 800, 1000],
    [1000, 1800, 1100, 800, 1000],
    [1000, 1800, 1100, 800, 1000],
]

# Update the worksheet with the data
open_spreadsheet("Price of Fish")
worksheet = open_worksheet(work_sheet="Sheet1", spread_sheet="Price of Fish")

worksheet.update('B1:F8', data)

print('Data uploaded successfully!')
