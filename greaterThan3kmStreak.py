import pandas
import json
from datetime import timedelta
import numpy

def getListOfDates(userID, minDistance, jsonData):
    """Inputs:
    userID: string
    minDistance: integer, the minimum (or equal) distance required to count an entry towards a long-distance streak
    consecutiveDaysLen: integer, the number of days required to count consecutive days as part of a long-distance streak
    jsonData: json data. If data is stored in a directory, open and load the data before passing it to this function.
    
    Outputs:
    A list of sorted, unique dates the defined user met the specified constraints"""

    # Load json into dataframe and format
    df = pandas.DataFrame(jsonData, columns=["user_id", "start", "distance"]) #only import the needed columns
    df["reformattedStart"] = pandas.to_datetime(df["start"]) #convert start date to date. Assume the start date/time is when the run counts toward a certain day.
    df["date"] = df["reformattedStart"].dt.date #drop time, keep date only

    # narrow down to only runs that were logged by the specified user and longer than 1km.
    df = df.loc[df["user_id"] == userID]
    df = df.loc[df["distance"] >= minDistance] #**the prompt said >1km, but changing it to >= is something I would clarify if I could change it to.

    #It matters more to the numberOfTimesDistanceContinued function that the returned list is sorted and contains only unique values,
    #doing this now returns a cleaner, smaller output for alternative uses
    df = df.drop_duplicates()
    df = df.sort_values(by="date", ascending=True)

    return df["date"].tolist()


def numberOfTimesDistanceContinued(consecutiveDaysLen, daysDistanceMet):
    """Inputs:
    consecutiveDaysLen: integer, the number of days required to count consecutive days as part of a long-distance streak
    daysDistanceMet: list, an array of dates to find how many times a sequence of consecutiveDaysLen-number of consecutive days occured

    Outputs:
    An integer representing the number of times a sequence of consecutiveDaysLen-number of consecutive days occured"""

    if not daysDistanceMet: #return 0 if the daysDistanceMet is nothing
        return 0

    streakSizes = [] #array to keep the length of running streaks
    numDaysInCurrentStreak = 1 #start the counter at one to count the current day being tested in the streak
    daysDistanceMet = list(set(daysDistanceMet))
    daysDistanceMet.sort()
    for i in range(len(streakDates)-1):  #this loop cmpares the current item with the next item, and will throw an error if you try to call a non-existent item
        if streakDates[i+1] - timedelta(days=1) == streakDates[i]:  #if the next date is only one day ahead of the current item
            numDaysInCurrentStreak = numDaysInCurrentStreak + 1
        elif streakDates[i+1] - timedelta(days=1) != streakDates[i]:  #if the next date is more than one day ahead of the current item
            streakSizes.append(numDaysInCurrentStreak) #append the current value to the streakSizes array
            numDaysInCurrentStreak = 1 #reset the counter

    return sum([int(streak/consecutiveDaysLen) for streak in streakSizes if streak >= consecutiveDaysLen]) #3 could be changed into an argument to find streaks of different lengths
    
        


jData = json.load(open("mainJSON.json")) #import the json file with the running data
userID = "d77908482ed2505ebbf17ef72be2f080"
consecDays = 3
minDist = 1

qualifyingDates = getListOfDates(userID, minDist, jData)
print(numberOfTimesDistanceContinued(consecDays, qualifyingDates))



