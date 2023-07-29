import re

# Parses the text for either "/", "x", or a tag (like Myo-Reps)
def parse_plan_for_sets(plan_str):
    plan_str = plan_str.replace(" ", "")  # Remove any spaces in the plan string
    if "/" in plan_str and "x" in plan_str:
        pattern = re.compile(r"(\d+)x")
        match = pattern.search(plan_str)
        return plan_str.count("/") + int(match.group(1))
    elif "Myo-Reps" in plan_str:
        return 6
    elif "/" in plan_str:
        return plan_str.count("/") + 1
    elif "x" in plan_str:
        pattern = re.compile(r"(\d+)x")
        match = pattern.search(plan_str)
        if match:
            return int(match.group(1))
    return int(plan_str) if plan_str.isdigit() else 1

#TODO: Parses the text for either "@", "% of E1RM"
def parse_plan_for_intensity():
    return 1