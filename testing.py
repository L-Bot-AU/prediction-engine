import getData

term = int(input("Term: "))
week = int(input("Week: "))
day = int(input("Day: "))
while term:
    print(getData.getData(term,week,day))

    term = int(input("Term: "))
    week = int(input("Week: "))
    day = int(input("Day: "))