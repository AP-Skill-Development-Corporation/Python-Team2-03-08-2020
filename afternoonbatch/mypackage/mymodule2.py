def Leapyear(low,upp):
    for year in range(low,upp+1):
        if year%400==0  or (year%100!=0 and year%4==0 ):
            print(year,"leapyear")
        else:
            print(year,"non leapyear")
            
            
            
            
            
class classname:
    def Leapyear(low,upp):
        for year in range(low,upp+1):
            if year%400==0  or (year%100!=0 and year%4==0 ):
                print(year,"leapyear")
            else:
                print(year,"non leapyear")
            
            