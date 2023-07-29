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

    # Step 4: Write the data to each sheet (excluding "Week", "Plan", and "SS" columns)
    for week in unique_weeks:
        week_sheet = output_wb["Week {}".format(week)]
        week_data = df[df["Week"] == week].drop(columns=["Week", "Plan", "SS?"])
        for row in pd.DataFrame(week_data).itertuples(index=False, name=None):
            week_sheet.append(row)

    # Step 5: Save the output Excel file
    output_wb.save(output_file)

def repeat_lines_per_sets(week_data, sets):
    


# Example usage:
#create_output_spreadsheet("Creator.xlsx", "Output.xlsx")

# Read the data from the original Excel file
df = pd.read_excel("Creator.xlsx")

# Apply the parse_plan function to the "Plan" column and print the results
for plan in df["Plan"]:
    parsed_value = parse_plan_for_sets(plan)
    print(f"Plan: {plan} -> Parsed Value: {parsed_value}")
