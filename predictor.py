import json
#Notes
#Data is either and equation or a specified uppper and lower bounds
#The equations are no more than degree 2. i.e. ax+c or ax^2+bx+c
#a and b are always written with one decimal place e.g. 9.8 6.0
#c is always a whole number
#This is as detailed as each of these numbers need to be for predictions to work
#days.json stores each days prediction the keys in it are t-w-d. (Term-week-day)
#Day here is represented by a numerical value 1-5 for Mon-Fri
#Variables for each function are named:
#(t|b)<year>(bs|b1|b2)
#year = 2018|2019
#t refers to maximum or top value
#b refers to minimum or bottom value
#bs, b1, b2 refer to before school, break 1, break 2 respectively 
#This is based on previous data

def Term1Mon(week):
    #2018
    t2018bs = 85
    b2018bs = 50
    t2018b1 = round(5.1*week+27)+25
    b2018b1 = round(5.1*week+27)-25
    t2018b2 = round(2.7*week+11)+10
    b2018b2 = round(2.7*week+11)-10
    #2019
    t2019bs = round(3.2*week+39)+20
    b2019bs = round(3.2*week+39)-20
    t2019b1 = round(8.4*week+26)+30
    b2019b1 = round(8.4*week+26)-30
    t2019b2 = round(1.5*week+26)+20
    b2019b2 = round(1.5*week+26)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term1Tue(week):
    #2018
    t2018bs = 75
    b2018bs = 30
    t2018b1 = 80
    b2018b1 = 30
    t2018b2 = 40
    b2018b2 = 20
    #2019
    t2019bs = round(1.3*week+45)+10
    b2019bs = round(1.3*week+45)-10
    t2019b1 = round(2.3*week+46)+20
    b2019b1 = round(2.3*week+46)-20
    t2019b2 = round(1.8*week+14)+15
    b2019b2 = round(1.8*week+14)-15

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict = {"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}
    
    return return_dict

def Term1Wed(week):
    #2018
    t2018bs = round(1.7*week+44)+30
    b2018bs = round(1.7*week+44)-30
    t2018b1 = round(2.0*week+12)+15
    b2018b1 = round(2.0*week+12)-15
    t2018b2 = round(3.4*week+24)+20
    b2018b2 = round(3.4*week+24)-20
    #2019
    t2019bs = round(5.4*week+27)+20
    b2019bs = round(5.4*week+27)-20
    t2019b1 = round(2.7*week+10)+10
    b2019b1 = round(2.7*week+10)-10
    t2019b2 = round(6.0*week+27)+20
    b2019b2 = round(6.0*week+27)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term1Thu(week):
    #2018
    t2018bs = round(3.3*week+12)+15
    b2018bs = round(3.3*week+12)-15
    t2018b1 = round(1.0*week+11)+15
    b2018b1 = round(1.0*week+11)-15
    t2018b2 = 25
    b2018b2 = 0
    #2019
    t2019bs = 80
    b2019bs = 40
    t2019b1 = round(1.7*week+6)+10
    b2019b1 = round(1.7*week+6)-10
    t2019b2 = 20
    b2019b2 = 0

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term1Fri(week):
    #2018
    t2018bs = round(3.1*week+83)+20
    b2018bs = round(3.1*week+83)-20
    t2018b1 = round(2.4*week+12)+10
    b2018b1 = round(2.4*week+12)-10
    t2018b2 = round(5.4*week+22)+20
    b2018b2 = round(5.4*week+22)-20
    #2019
    t2019bs = round(5.5*week+69)+20
    b2019bs = round(5.5*week+69)-20
    t2019b1 = round(3.6*week+11)+10
    b2019b1 = round(3.6*week+11)-10
    t2019b2 = round(3.4*week+37)+20
    b2019b2 = round(3.4*week+37)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term2Mon(week):
    #2018
    t2018bs = round(3.2*week+50)+10
    b2018bs = round(3.2*week+50)-10
    t2018b1 = round(-3.3*week+84)+10
    b2018b1 = round(-3.3*week+84)-10
    t2018b2 = 50
    b2018b2 = 30
    #2019
    if week <8:
        t2019bs = round(-13.4*week+108)+5
        b2019bs = round(-13.4*week+108)-5
    else:
        t2019bs = 90
        b2019bs = 80
    t2019b1 = 80
    b2019b1 = 40
    t2019b2 = 60
    b2019b2 = 20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term2Tue(week):
    #2018
    t2018bs = round(4.8*week+41)+10
    b2018bs = round(4.8*week+41)-10
    t2018b1 = round(-5.4*week+85)+10
    b2018b1 = round(-5.4*week+85)-10
    t2018b2 = 50
    b2018b2 = 20
    #2019
    if week <6:
        t2019bs = round(-13*week+113)+5
        b2019bs = round(-13*week+113)-5
    else:
        t2019bs = 90
        b2019bs = 80
    t2019b1 = 80
    b2019b1 = 40
    t2019b2 = 0
    b2019b2 = 50

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term2Wed(week):
    #2018
    t2018bs = round(3.4*week+56)+10
    b2018bs = round(3.4*week+56)-10
    t2018b1 = 70 #40 perhaps few outliers investiagate later
    b2018b1 = 20 
    t2018b2 = 80
    b2018b2 = 40
    #2019
    t2019bs = round(6.0*week+25)+15
    b2019bs = round(6.0*week+25)-15
    t2019b1 = round(3.2*week+8)+15
    b2019b1 = round(3.2*week+8)-15
    t2019b2 = round(7.9*week+24)+20
    b2019b2 = round(7.9*week+24)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term2Thu(week):
    #2018
    t2018bs = round(5.2*week+35)+15
    b2018bs = round(5.2*week+35)-15
    t2018b1 = 20
    b2018b1 = 40
    t2018b2 = 25
    b2018b2 = 0
    #2019
    t2019bs = round(4.4*week+32)+20
    b2019bs = round(4.4*week+32)-20
    t2019b1 = round(2.4*week+4)+10
    b2019b1 = round(2.4*week+4)-10
    t2019b2 = 20
    b2019b2 = 0

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term2Fri(week):
    #2018
    t2018bs = round(8.8*week+51)+20
    b2018bs = round(8.8*week+51)-20
    t2018b1 = round(-1.8*week*week+18*week+12)+10
    b2018b1 = round(-1.8*week*week+18*week+12)-10
    t2018b2 = 65
    b2018b2 = 40
    #2019
    t2019bs = 100  #120 outlier
    b2019bs = 60
    t2019b1 = 40
    b2019b1 = 20
    t2019b2 = round(-5.5*week+67)+20
    b2019b2 = round(-5.5*week+67)-20
    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term3Mon(week):
    #2018
    t2018bs = 100
    b2018bs = 60
    t2018b1 = 80
    b2018b1 = 70
    t2018b2 = round(-6.3*week+78)+15
    b2018b2 = round(-6.3*week+78)-15
    #2019
    t2019bs = 90
    b2019bs = 50
    t2019b1 = 90
    b2019b1 = 60
    t2019b2 = round(4.3*week+23)+15
    b2019b2 = round(4.3*week+23)-15

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term3Tue(week):
    #2018
    t2018bs = round(3.9*week+54)+15
    b2018bs = round(3.9*week+54)-15
    t2018b1 = 90
    b2018b1 = 20
    t2018b2 = round(-3.6*week+56)+15
    b2018b2 = round(-3.6*week+56)-15

    #2019
    t2019bs = 100
    b2019bs = 60
    t2019b1 = round(6.6*week+22)+10
    b2019b1 = round(6.6*week+22)-10
    t2019b2 = 70
    b2019b2 = 20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term3Wed(week):
    #2018
    t2018bs = 90
    b2018bs = 50
    t2018b1 = 50
    b2018b1 = 30
    t2018b2 = round(1.6*week+47)+20
    b2018b2 = round(1.6*week+47)-20
    #2019
    t2019bs = 70
    b2019bs = 50
    t2019b1 = 30
    b2019b1 = 0
    t2019b2 = round(6.7*week+34)+20
    b2019b2 = round(6.7*week+34)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term3Thu(week):
    #2018
    t2018bs = round(0.9*week+57)+10
    b2018bs = round(0.9*week+57)-10
    t2018b1 = 40
    b2018b1 = 20
    t2018b2 = 20
    b2018b2 = 0
    #2019
    t2019bs = round(3.2*week+34)+20
    b2019bs = round(3.2*week+34)-20
    t2019b1 = 50
    b2019b1 = 20
    t2019b2 = 20
    b2019b2 = 0

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term3Fri(week):
    #2018
    t2018bs = 120
    b2018bs = 60
    t2018b1 = round(4.3*week+51)+20
    b2018b1 = round(4.3*week+51)-20
    t2018b2 = 80
    b2018b2 = 40
    #2019
    t2019bs = round(-2.7*week*week+36.6*week+-22)+5
    b2019bs = round(-2.7*week*week+36.6*week+-22)-5
    t2019b1 = round(3.6*week+10)+10
    b2019b1 = round(3.6*week+10)-10
    t2019b2 = round(-2.0*week*week+26.6*week+4)+20
    b2019b2 = round(-2.0*week*week+26.6*week+4)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term4Mon(week):
    #2018
    t2018bs = round(-2.6*week+85)+15
    b2018bs = round(-2.6*week+85)-15
    t2018b1 = round(-4.2*week+94)+30
    b2018b1 = round(-4.2*week+94)-30
    t2018b2 = round(-4.6*week+69)+10
    b2018b2 = round(-4.6*week+69)-10
    #2019
    t2019bs = round(-4.3*week+83)+15
    b2019bs = round(-4.3*week+83)-15
    t2019b1 = round(-5.7*week+105)+20
    b2019b1 = round(-5.7*week+105)-20
    t2019b2 = round(-2.1*week+53)+10
    b2019b2 = round(-2.1*week+53)-10

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term4Tue(week):
    #2018
    t2018bs = round(-5.2*week+101)+20
    b2018bs = round(-5.2*week+101)-20
    t2018b1 = round(-11.4*week+136)+20
    b2018b1 = round(-11.4*week+136)-20
    t2018b2 = 40
    b2018b2 = 0

    #2019
    t2019bs = round(-2.0*week+73)+20
    b2019bs = round(-2.0*week+73)-20
    t2019b1 = round(-4.3*week+88)+20
    b2019b1 = round(-4.3*week+88)-20
    t2019b2 = 60
    b2019b2 = 30

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term4Wed(week):
    #2018
    t2018bs = round(-3.5*week+89)+20
    b2018bs = round(-3.5*week+89)-20
    t2018b1 = round(-4.3*week+56)+20
    b2018b1 = round(-4.3*week+56)-20
    t2018b2 = round(-6.2*week+88)+30
    b2018b2 = round(-6.2*week+88)-30
    #2019
    t2019bs = round(-4.4*week+76)+20
    b2019bs = round(-4.4*week+76)+20
    t2019b1 = 20
    b2019b1 = 0
    t2019b2 = round(-6.1*week+97)+20
    b2019b2 = round(-6.1*week+97)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term4Thu(week):
    #2018
    t2018bs = round(-6.6*week+109)+20
    b2018bs = round(-6.6*week+109)-20
    t2018b1 = 40
    b2018b1 = 20
    t2018b2 = 20
    b2018b2 = 0
    #2019
    t2019bs = round(-5.4*week+78)+20
    b2019bs = round(-5.4*week+78)-20
    t2019b1 = 50
    b2019b1 = 10
    t2019b2 = 20
    b2019b2 = 0

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def Term4Fri(week):
    #2018
    t2018bs = round(-5.2*week+119)+30
    b2018bs = round(-5.2*week+119)-30
    t2018b1 = round(-3.3*week+47)+10
    b2018b1 = round(-3.3*week+47)-10
    t2018b2 = round(-6.6*week+101)+20
    b2018b2 = round(-6.6*week+101)-20
    #2019
    t2019bs = round(-7.7*week+129)+5
    b2019bs = round(-7.7*week+129)-5
    t2019b1 = round(-4.3*week+61)+10
    b2019b1 = round(-4.3*week+61)-10
    t2019b2 = round(-8.9*week+119)+20
    b2019b2 = round(-8.9*week+119)-20

    maxbs = max(t2018bs,t2019bs)
    minbs = min(b2018bs,b2019bs)
    maxb1 = max(t2018b1,t2019b1)
    minb1 = min(b2018b1,b2019b1)
    maxb2 = max(t2018b2,t2019b2)
    minb2 = min(b2018b2,b2019b2)
    
    return_dict ={"Overall": [maxbs, minbs, maxb1, minb1, maxb2, minb2] ,
            "2018":[t2018bs, b2018bs, t2018b1, b2018b1, t2018b2, b2018b2],
            "2019":[t2019bs, b2019bs, t2019b1, b2019b1, t2019b2, b2019b2]}

    return return_dict

def callData(term, week, day):
    #Read existing file so do not write over
    f = open("days.json")
    days = {}
    days = json.load(f)
    f.close()
    #Data for a day to give if not generated
    pred = {}
    if term == 1:
        if day == 1:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term1Mon(week)
        elif day == 2:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term1Tue(week)
        elif day == 3:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term1Wed(week)
        elif day == 4:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term1Thu(week)
        elif day == 5:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term1Fri(week)
    elif term == 2:
        if day == 1:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term2Mon(week)
        elif day == 2:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term2Tue(week)
        elif day == 3:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term2Wed(week)
        elif day == 4:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term2Thu(week)
        elif day == 5:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term2Fri(week)
    elif term == 3:
        if day == 1:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term3Mon(week)
        elif day == 2:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term3Tue(week)
        elif day == 3:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term3Wed(week)
        elif day == 4:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term3Thu(week)
        elif day == 5:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term3Fri(week)
    elif term == 4:
        if day == 1:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term4Mon(week)
        elif day == 2:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term4Tue(week)
        elif day == 3:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term4Wed(week)
        elif day == 4:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term4Thu(week)
        elif day == 5:
            pred[str(term)+'-'+str(week)+'-'+str(day)] = Term4Fri(week)
    #Put generated data with everything else 
    days[str(term)+'-'+str(week)+'-'+str(day)] = pred[str(term)+'-'+str(week)+'-'+str(day)]
    #Save new data
    with open("days.json", 'w') as f:
        json.dump(days, f)
    
    return pred