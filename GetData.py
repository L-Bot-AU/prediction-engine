import predictor as p
import json

def getData(term, week, day):
    if term > 4:
        return
    f = open("days.json")
    days = json.load(f)
    dayID = str(term)+'-'+str(week)+'-'+str(day)
    for key in days:
        if key == dayID:
            return days[dayID]
    
    return p.callData(term, week, day)