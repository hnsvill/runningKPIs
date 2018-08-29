import pandas
import json
import datetime

def getDistanceReps(userID):
    jData = json.load(open("mainJSON.json")) #import the json file with the running data
    df = pandas.DataFrame(jData, columns=["user_id", "activity_id", "start", "end", "distance", "speed", "pace"])
    df["reformattedStart"] = pandas.to_datetime(df["start"])
    df["reformattedEnd"] = pandas.to_datetime(df["end"])
    df["elapsed"] = df["reformattedEnd"] - df["reformattedStart"]
    df["dayOfWeekStart"] = pandas.Series(df["reformattedStart"]).dt.dayofweek
    df["weekStartingOn"] = (df["reformattedStart"]-pandas.to_timedelta(df["dayOfWeekStart"], unit="d")).dt.strftime("%m/%d/%y")
    tempDf = df.loc[df["user_id"] == userID]
    table = tempDf.pivot_table(values="distance", index=["user_id","weekStartingOn"], aggfunc="sum")
    return table[table.distance > 10].count()

print(getDistanceReps("d77908482ed2505ebbf17ef72be2f080"))