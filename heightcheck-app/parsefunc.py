def parse(feet_inches):
    """ user enters a string and returns a dictionary """
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
