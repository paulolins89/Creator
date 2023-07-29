import pandas as pd
from openpyxl import Workbook
from plan_parser import parse_plan_for_sets

def create_output_spreadsheet(input_file, output_file):
    # Step 1: Read the data from the input file
    df = pd.read_excel(input_file)

    # Step 2: Get unique week values and create new sheets
    unique_weeks = df["Week"].unique()

    # Step 3: Create the output Excel file and sheets
    output_wb = Workbook()
    output_wb.remove(output_wb.active)  # Remove the default first sheet

    for week in unique_weeks:
        output_wb.create_sheet(title="Week {}".format(week))

    for week in unique_weeks:
        #makes it focus on one for a specific week
        week_data = df[df["Week"] == week]

        # Repeat lines per sets for the current week_data
        sets = repeat_lines_per_sets(week_data)

        # Get the corresponding sheet for the current week
        week_sheet = output_wb["Week {}".format(week)]

        # Write each row from 'sets' DataFrame to the sheet
        for _, row in sets.iterrows():
            week_sheet.append(row)

    # Step 5: Save the output Excel file
    output_wb.save(output_file)

def repeat_lines_per_sets(week_data):
    repeated_data = pd.DataFrame()
    for _, row in week_data.iterrows():
        repeated_data = pd.concat([repeated_data] + [row] * parse_plan_for_sets(row["Plan"]), ignore_index=True)
    return repeated_data
    
# Example usage:
create_output_spreadsheet("Creator.xlsx", "Output.xlsx")
