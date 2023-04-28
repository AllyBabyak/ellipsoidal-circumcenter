# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:53:09 2023

@author: a.babyak
"""

import pandas as pd
from FinalForm import ErrorTestGiven, StringToCoord
from DifferentCenters import ArcCenters

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
        Cent = ArcCenters(P1, P2, P3, "Degrees")
        ErrorCP = ErrorTestGiven(P1, P2, P3, Cent[0], "Degrees")
        ErrorXYP = ErrorTestGiven(P1, P2, P3, Cent[1], "Degrees")
        ErrorXYCC = ErrorTestGiven(P1, P2, P3, Cent[2], "Degrees")
        
        Heading = tests.loc[i,'Approximate Center']
        if type(Heading) == str:
            print(Heading)
        
        Distance = tests.loc[i,'Approximate Distance']
        if type(Distance) == float:
            Distance = "N/A"
        Spaces = (11 - len(Distance))*' '
        SpacesCP = (24 - len(str(ErrorCP)))*' '
        SpacesXYP = (24 - len(str(ErrorXYP)))*' '
        print(Distance,Spaces, ErrorCP, SpacesCP, ErrorXYP,SpacesXYP,ErrorXYCC)
    return None

def ErrorSize():
    for i in range(200):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        Cent = ArcCenters(P1, P2, P3, "Degrees")
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

def BestVal():
    for i in range(200):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        Cent = ArcCenters(P1, P2, P3, "Degrees")
        ErrorCP = ErrorTestGiven(P1, P2, P3, Cent[0], "Degrees")
        ErrorXYP = ErrorTestGiven(P1, P2, P3, Cent[1], "Degrees")
        ErrorXYCC = ErrorTestGiven(P1, P2, P3, Cent[2], "Degrees")
        
        Heading = tests.loc[i,'Approximate Center']
        if type(Heading) == str:
            print(Heading)
            
        Distance = tests.loc[i,'Approximate Distance']
        if type(Distance) == float:
            Distance = "N/A"
        
        Least = min(ErrorCP,ErrorXYCC,ErrorXYP)
        if Least == ErrorCP:
            Type = "CPP"
        elif Least == ErrorXYCC:
            Type = "XYC"
        elif Least == ErrorXYP:
            Type = "XYP"
        Spaces = (11 - len(Distance))*' '
        
        if Type != "CPP":
            Diff = ErrorCP - Least
            print (Distance,Spaces, Type,Least, Diff)

RunTests()