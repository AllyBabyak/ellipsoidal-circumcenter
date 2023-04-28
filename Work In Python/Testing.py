# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:57:37 2023

@author: a.babyak
"""

import pandas as pd
from FinalForm import ErrorTestGiven, StringToCoord, ArcCenter

tests = pd.read_excel(r'C:\Users\a.babyak\Downloads\CODE\Book13.xlsx')


'''
P1 = StringToCoord(tests.loc[95,'Point 1'])
P2 = StringToCoord(tests.loc[95,'Point 2'])
P3 = StringToCoord(tests.loc[95,'Point 3'])
'''

def RunTests():
    for i in range(200):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        Cent = ArcCenter(P1, P2, P3, "Degrees")
        Error = ErrorTestGiven(P1, P2, P3, Cent, "Degrees")
        
        Heading = tests.loc[i,'Approximate Center']
        if type(Heading) == str:
            print(Heading)
        
        Distance = tests.loc[i,'Approximate Distance']
        if type(Distance) == float:
            Distance = "N/A"
        Spaces = (11 - len(Distance))*' '
        print(Distance,Spaces, Error)
    return None

def ErrorSize():
    for i in range(199):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        Cent = ArcCenter(P1, P2, P3, "Degrees")
        Error = ErrorTestGiven(P1, P2, P3, Cent, "Degrees")
        Heading = tests.loc[i,'Approximate Center']
        if type(Heading) == str:
            print(Heading)
        if Error > 1:
            Distance = tests.loc[i,'Approximate Distance']
            if type(Distance) == float:
                Distance = "N/A"
            Spaces = (11 - len(Distance))*' '
            print(Distance,Spaces, Error)
    return None

RunTests()

'''
Cent = ArcCenter(P1, P2, P3, "Degrees")
Error = ErrorTestGiven(P1, P2, P3, Cent, "Degrees")
print(Cent)
print(Error)
'''