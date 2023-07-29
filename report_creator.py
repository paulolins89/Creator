import pandas as pd
from openpyxl import Workbook
from plan_parser import parse_plan_for_sets

def create_output_spreadsheet(df, output_file):
    # Step 1: Get unique week values and create new sheets
    unique_weeks = df["Week"].unique()

    # Step 2: Create the output Excel file and sheets
    output_wb = Workbook()
    output_wb.remove(output_wb.active)  # Remove the default first sheet

    for week in unique_weeks:
        output_wb.create_sheet(title="Week {}".format(week))

    #for week in unique_weeks:
    #    #makes it focus on one for a specific week
    #    week_data = df[df["Week"] == week]
    #
    #    # Repeat lines per sets for the current week_data
    #    sets = repeat_lines_per_sets(week_data)
    #
    #    # Get the corresponding sheet for the current week
    #    week_sheet = output_wb["Week {}".format(week)]
    #
    #    # Write each row from 'sets' DataFrame to the sheet
    #    for _, row in sets.iterrows():
    #        week_sheet.append(row)

    # Step 3: Save the output Excel file
    output_wb.save(output_file)

def populate_worksheets(df, output_wb):
    output_wb = "Output.xlsx"
    for index, row in df.iterrows():
        week_sheet = output_wb["Week {}".format(week)]
        print(row)

# Example usage:
df = pd.read_excel("Creator.xlsx")
populate_worksheets(df)
create_output_spreadsheet(df, "Output.xlsx")
