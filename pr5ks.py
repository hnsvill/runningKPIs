import json

def currentYearPRs(userID, minDistance, jsonData):
    """Inputs:
    userID: string
    minDistance: integer, the minimum number of kilometers to count a run toward bettering their pace
    jsonData: json data. If data is stored in a directory, open and load the data before passing it to this function.
    
    Outputs:
    An integer representing the number of times the user broke their record for fastest pace for minDistance kilometer runs"""

    import pandas
    from datetime import timedelta

    # Load json into dataframe and format
    df = pandas.DataFrame(jsonData, columns=["user_id", "start", "distance", "pace"]) #only import the needed columns
    df["date"] = pandas.to_datetime(df["start"]) #convert start date to date. Assume the start date/time is when the run counts toward a certain day.
    df["month"] = df["date"].dt.month #get the months separated to group by later

    # narrow down to only runs that were logged by the specified user and longer than 5km. Sort the dataframe.
    df = df.loc[df["user_id"] == userID]
    df = df.loc[df["distance"] > minDistance]
    df = df.sort_values(by="date", ascending=True)

    # get last year's PR
    prevYearDf = df.loc[df["date"].dt.year == (pandas.to_datetime("today") - timedelta(days=365)).year]
    prevYearMaxPace = round(prevYearDf["pace"].max(), 2)
    if pandas.isnull(prevYearMaxPace):
        prevYearMaxPace = 0

    # Return list of monthly PR's for the current year
    df = df.loc[df["date"].dt.year == pandas.to_datetime("today").year]
    temp = df.groupby("month").max().add_prefix("max_")
    paceArr = temp["max_pace"].tolist()
    paceArr = [round(num, 2) for num in paceArr] #round to the second decimal. Rounding keeps the user from displaying they PR'd when they only beat the last pace by .0000005

    # Loop through the current year's PR's to count how many were made, somewhat similar to bubblesort. Loop is simple enough to keep in this function for this exersize.
    # To prepare for production, this function could be separated into many different functions that could be refactored for more robustness and reusability.
    #       One to return the dataframe of the user's data (maybe includes filter for distance),
    #       One to take the dataframe and return a list of max pace per month for the current year,
    #       One to take the dataframe and return the max pace for a given timeframe
    #       And finally, one to return the number of PR's
    currentMax = prevYearMaxPace
    timesPRd = 0

    for pace in paceArr:
        if pace > currentMax:
            timesPRd = timesPRd + 1
    
    return timesPRd

def wrapper(userID):
    """Inputs:
    userID: string
    
    Wrapper to add arguments that weren't specified as needing to be arguments. Keeping this separate from main() allows unit testing
    
    Outputs:
    JSON to stdout"""
    jData = json.load(open("mainJSON.json")) #import the json file with the running data
    #load up values that the assignment did not specify to have as arguments
    minDist = 10

    qtyPRs = currentYearPRs(userID, minDist, jData)

    return json.dumps({"user_id": userID, "current_year_5k_PRs_pace": qtyPRs})

def main():
    userID = input("Please provide a userID: ") #takes standard input from the command line
    print(wrapper(userID)) #prints the json returned as standard output from the wrapper function

if __name__ == "__main__":
    main()