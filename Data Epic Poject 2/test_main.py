import gspread
import pytest
from main import *

def gc_sheet():
    return gspread.service_account("gspread-sheet-2-4ebedcdae885.json")

def test_spreadsheet_title(gc_sheet):
    spreadsheet = open_spreadsheet("Price of Fish", gc_sheet)
    assert spreadsheet.title == "Price of Fish"

def test_worksheet_title(gc_sheet):
    worksheet = open_worksheet("Price of Fish", "Sheet1", gc_sheet)
    assert worksheet.title == "Sheet1"

def test_spreadsheet_does_not_exist(gc_sheet):
    with pytest.raises(gspread.exceptions.SpreadsheetNotFound):
        open_spreadsheet("NonExistentSpreadsheet", gc_sheet)
    assert str() == "Spreadsheet 'NonExistentSpreadsheet' not found."

def test_worksheet_does_not_exist(gc_sheet):
    with pytest.raises(gspread.exceptions.WorksheetNotFound):
        open_worksheet("Price of Fish", "NonExistentWorksheet", gc_sheet)
    assert str() == "Worksheet 'NonExistentWorksheet' not found in spreadsheet 'Price of Fish'."

def test_open_spreadsheet_success(gc_sheet):
    try:
        spreadsheet = open_spreadsheet("Price of Fish", gc_sheet)
        assert isinstance(spreadsheet, gspread.models.Spreadsheet)
    except Exception as e:
        pytest.fail(f"Failed to open spreadsheet: {e}")
