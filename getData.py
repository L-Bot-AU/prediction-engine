import predictor as p
import json

def getData(term, week, day):
    """
    :param term: the term (1-4)
    :param week: the week (of each term)
    :param day: the weekday represented as an integer( 1 for Monday)
    :return: an array in the format: `[before school max, before school min, break 1 max, break 1 min, break 2 max, break 2 min]`
    """

    #First trys to get data from file, if not found calls generator function
    #Makes sure bad data is not given (probably not needed)
    if term > 4 or day > 5:
        return "Give me proper inputs you nong"
    f = open("days.json")
    days = json.load(f)
    dayID = str(term)+'-'+str(week)+'-'+str(day)
    for key in days:
        if key == dayID:
            return {"Jnr":p.callData(term, week, day)[dayID]["Jnr"],
            "Snr":p.callData(term, week, day)[dayID]["Snr"]}
    #This will get the data
    return {"Jnr":p.callData(term, week, day)[dayID]["Jnr"],
            "Snr":p.callData(term, week, day)[dayID]["Snr"]}