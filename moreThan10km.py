import json

def getDistanceReps(userID, distanceCheckedFor, jsonData):
    """Inputs:
    userID: string
    distanceCheckedFor: integer, the minimum (or equal) distance required to count an entry towards a long-distance streak
    jsonData: json data. If data is stored in a directory, open and load the data before passing it to this function.
    
    Outputs:
    An integer"""

    import pandas
    import datetime

    df = pandas.DataFrame(jsonData, columns=["user_id", "start", "distance"])
    df["reformattedStart"] = pandas.to_datetime(df["start"]) #convert to date/time
    df["dayOfWeekStart"] = pandas.Series(df["reformattedStart"]).dt.dayofweek #find how many days to subtract from the date to get back to Monday
    df["weekStartingOn"] = (df["reformattedStart"]-pandas.to_timedelta(df["dayOfWeekStart"], unit="d")).dt.strftime("%m/%d/%y") #given the start day, find the day the same week starts on
    df = df.loc[df["user_id"] == userID]
    table = df.pivot_table(values="distance", index=["user_id","weekStartingOn"], aggfunc="sum") #get the aggregate distance ran for the week
    return int(table[table.distance > distanceCheckedFor].count())


def wrapper(userID):
    jData = json.load(open("mainJSON.json")) #import the json file with the running data
    #load up values that the assignment did not specify to have as arguments
    dist = 10

    weeks10kReached = getDistanceReps(userID, dist, jData)
    return json.dumps({"user_id": userID, "weeks_10k_aggregated": weeks10kReached})

def main():
    userID = input("Please provide a userID: ") #takes standard input from the command line
    print(wrapper(userID)) #prints the json returned as standard output from the wrapper function

if __name__ == "__main__":
    main()