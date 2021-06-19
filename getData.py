import predictor
import json

def getData(term, week, day):
    """
    :param term: the term (1-4)
    :param week: the week (of each term)
    :param day: the weekday represented as an integer( 1 for Monday)
    :return: an array in the format: `[before school max, break 1, break 2]`
    """

    #Makes sure bad data is not given (probably not needed)
    if term > 4 or day > 5 or week > 13:
         raise Exception("Data provided out of range")
    dayID = str(term)+'-'+str(week)+'-'+str(day)
    #This will get the data
    return predictor.callData(term, week, day)
