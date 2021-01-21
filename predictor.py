import json

def Term1Mon(week):
    #2018
    t2018bs = 85
    b2018bs = 50
    t2018b1 = round(5.13*week+27.32)+25
    b2018b1 = round(5.13*week+27.32)-25
    t2018b2 = round(2.71*week+10.7)+10
    b2018b2 = round(2.71*week+10.7)-10
    #2019
    t2019bs = round(3.2*week+38.82)+20
    b2019bs = round(3.2*week+38.82)-20
    t2019b1 = round(8.36*week+25.54)+30
    b2019b1 = round(8.36*week+25.54)-30
    t2019b2 = round(1.52*week+26.49)+20
    b2019b2 = round(1.52*week+26.49)-20

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
    t2019bs = round(1.26*week+44.66)+10
    b2019bs = round(1.26*week+44.66)-10
    t2019b1 = round(2.26*week+45.87)+20
    b2019b1 = round(2.26*week+45.87)-20
    t2019b2 = round(1.77*week+13.69)+15
    b2019b2 = round(1.77*week+13.69)-15

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
    t2018bs = round(1.73*week+44)+30
    b2018bs = round(1.73*week+44)-30
    t2018b1 = round(1.98*week+12.3)+15
    b2018b1 = round(1.98*week+12.3)-15
    t2018b2 = round(3.43*week+23.5)+20
    b2018b2 = round(3.43*week+23.5)-20
    #2019
    t2019bs = round(5.44*week+26.69)+20
    b2019bs = round(5.44*week+26.69)-20
    t2019b1 = round(2.7*week+9.8)+10
    b2019b1 = round(2.7*week+9.8)-10
    t2019b2 = round(6.07*week+26.69)+20
    b2019b2 = round(6.07*week+26.69)-20

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
    t2018bs = round(3.34*week+12.3)+15
    b2018bs = round(3.34*week+12.3)-15
    t2018b1 = round(1.06*week+11.44)+15
    b2018b1 = round(1.06*week+11.44)-15
    t2018b2 = 25
    b2018b2 = 0
    #2019
    t2019bs = 80
    b2019bs = 40
    t2019b1 = round(1.68*week+6.45)+10
    b2019b1 = round(1.68*week+6.45)-10
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
    t2018bs = round(3.1*week+82.5)+20
    b2018bs = round(3.1*week+82.5)-20
    t2018b1 = round(2.44*week+11.72)+10
    b2018b1 = round(2.44*week+11.72)-10
    t2018b2 = round(5.41*week+21.89)+20
    b2018b2 = round(5.41*week+21.89)-20
    #2019
    t2019bs = round(5.47*week+69.4)+20
    b2019bs = round(5.47*week+69.4)-20
    t2019b1 = round(3.59*week+10.73)+10
    b2019b1 = round(3.59*week+10.73)-10
    t2019b2 = round(3.35*week+37.27)+20
    b2019b2 = round(3.35*week+37.27)-20

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
    t2018bs = round(3.17*week+50.39)+10
    b2018bs = round(3.17*week+50.39)-10
    t2018b1 = round(-3.3*week+84.78)+10
    b2018b1 = round(-3.3*week+84.78)-10
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
    t2018bs = round(4.82*week+41)+10
    b2018bs = round(4.82*week+41)-10
    t2018b1 = round(-5.39*week+84.78)+10
    b2018b1 = round(-5.39*week+84.78)-10
    t2018b2 = 50
    b2018b2 = 20
    #2019
    if week <6:
        t2019bs = round(-14.3*week+112.7)+15
        b2019bs = round(-14.3*week+112.7)-15
    else:
        t2019bs = 100
        b2019bs = 60
    t2019b1 = 110
    b2019b1 = 40
    t2019b2 = 50
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

def Term2Wed(week):
    #2018
    t2018bs = round(3.4*week+56)+10
    b2018bs = round(3.4*week+56)-10
    t2018b1 = 70 #40 perhaps few outliers investiagate later
    b2018b1 = 20 
    t2018b2 = 80
    b2018b2 = 40
    #2019
    t2019bs = round(6.03*week+24.53)+15
    b2019bs = round(6.03*week+24.53)-15
    t2019b1 = round(3.2*week+7.8)+15
    b2019b1 = round(3.2*week+7.8)-15
    t2019b2 = round(7.89*week+24.2)+20
    b2019b2 = round(7.89*week+24.2)-20

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
    t2018bs = round(5.16*week+35)+15
    b2018bs = round(5.16*week+35)-15
    t2018b1 = 20
    b2018b1 = 40
    t2018b2 = 25
    b2018b2 = 0
    #2019
    t2019bs = round(4.42*week+32.02)+20
    b2019bs = round(4.42*week+32.02)-20
    t2019b1 = round(2.35*week+3.72)+10
    b2019b1 = round(2.35*week+3.72)-10
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
    t2018bs = round(8.75*week+51.46)+20
    b2018bs = round(8.75*week+51.46)-20
    t2018b1 = round(-1.76*week*week+18.3*week+11.72)+10
    b2018b1 = round(-1.76*week*week+18.3*week+11.72)-10
    t2018b2 = 65
    b2018b2 = 40
    #2019
    t2019bs = 100  #120 outlier
    b2019bs = 60
    t2019b1 = 40
    b2019b1 = 20
    t2019b2 = round(-5.47*week+66.67)+20
    b2019b2 = round(-5.47*week+66.67)-20
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
    t2018b2 = round(-6.32*week+77.67)+15
    b2018b2 = round(-6.32*week+77.67)-15
    #2019
    t2019bs = 90
    b2019bs = 50
    t2019b1 = 90
    b2019b1 = 60
    t2019b2 = round(4.31*week+23.24)+15
    b2019b2 = round(4.31*week+23.24)-15

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
    t2018bs = round(3.9*week+54.26)+15
    b2018bs = round(3.9*week+54.26)-15
    t2018b1 = 90
    b2018b1 = 20
    t2018b2 = round(-3.6*week+56)+15
    b2018b2 = round(-3.6*week+56)-15

    #2019
    t2019bs = 100
    b2019bs = 60
    t2019b1 = round(6.61*week+22.2)+10
    b2019b1 = round(6.61*week+22.2)-10
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
    t2018b2 = round(1.6*week+46.6)+20
    b2018b2 = round(1.6*week+46.6)-20
    #2019
    t2019bs = 70
    b2019bs = 50
    t2019b1 = 30
    b2019b1 = 0
    t2019b2 = round(6.71*week+34.4)+20
    b2019b2 = round(6.71*week+34.4)-20

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
    t2018bs = round(0.93*week+57.2)+10
    b2018bs = round(0.93*week+57.2)-10
    t2018b1 = 40
    b2018b1 = 20
    t2018b2 = 20
    b2018b2 = 0
    #2019
    t2019bs = round(3.23*week+34.4)+20
    b2019bs = round(3.23*week+34.4)-20
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
    t2018b1 = round(4.25*week+50.6)+20
    b2018b1 = round(4.25*week+50.6)-20
    t2018b2 = 80
    b2018b2 = 40
    #2019
    t2019bs = round(-2.69*week*week+36.6*week+-22)+5
    b2019bs = round(-2.69*week*week+36.6*week+-22)-5
    t2019b1 = round(3.59*week+10.73)+10
    b2019b1 = round(3.59*week+10.73)-10
    t2019b2 = round(-2.04*week*week+26.6*week+4.4)+20
    b2019b2 = round(-2.04*week*week+26.6*week+4.4)-20

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
    t2019bs = round(-4.44*week+76)+20
    b2019bs = round(-4.44*week+76)+20
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
    t2018bs = round(-6.6*week+109.4)+20
    b2018bs = round(-6.6*week+109.4)-20
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
    t2018b1 = round(-3.25*week+47)+10
    b2018b1 = round(-3.25*week+47)-10
    t2018b2 = round(-6.61*week+101)+20
    b2018b2 = round(-6.61*week+101)-20
    #2019
    t2019bs = round(-7.72*week+128.93)+5
    b2019bs = round(-7.72*week+128.93)-5
    t2019b1 = round(-4.32*week+60.89)+10
    b2019b1 = round(-4.32*week+60.89)-10
    t2019b2 = round(-8.9*week+118.5)+20
    b2019b2 = round(-8.9*week+118.5)-20

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

def generateData(term, week, day):
    #Get data for a specific day
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
    return pred

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