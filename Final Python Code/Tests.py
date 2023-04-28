# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:07:13 2023

@author: a.babyak
"""

import pandas as pd
from Center import ArcCenter
from ForTesting import ErrorTest, StringToCoord
from SphericalCenter import RadiusNearEquator, RadiusNearPoles, AverageRadius, SphericalCenter

tests = pd.read_excel(r'C:\Users\a.babyak\Downloads\CODE\Book13.xlsx')

def RunTests():
    for i in range(200):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        Cent = ArcCenter(P1, P2, P3, "Degrees")
        Error = ErrorTest(P1, P2, P3, Cent, "Degrees")
        
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
        Error = ErrorTest(P1, P2, P3, Cent, "Degrees")
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

def RunAllTests():
    for i in range(28,200):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        
        EllipticalCenter = ArcCenter(P1, P2, P3, "Degrees")
        EquatorSphereCenter = SphericalCenter(P1, P2, P3, "Degrees", RadiusNearEquator)
        PolarSphereCenter = SphericalCenter(P1, P2, P3, "Degrees", RadiusNearPoles)
        AverageSphereCenter = SphericalCenter(P1, P2, P3, "Degrees", AverageRadius)
        
        ErrorEC = ErrorTest(P1, P2, P3, EllipticalCenter, "Degrees")
        ErrorESC = ErrorTest(P1, P2, P3, EquatorSphereCenter, "Degrees")
        ErrorPSC = ErrorTest(P1, P2, P3, PolarSphereCenter, "Degrees")
        ErrorASC = ErrorTest(P1, P2, P3, AverageSphereCenter, "Degrees")
        
        Heading = tests.loc[i,'Approximate Center']
        if type(Heading) == str:
            print(Heading)
        
        Distance = tests.loc[i,'Approximate Distance']
        if type(Distance) == float:
            Distance = "N/A"
        Spaces = (11 - len(Distance))*' '
        SpacesEC = (24 - len(str(ErrorEC)))*' '
        SpacesESC = (24 - len(str(ErrorESC)))*' '
        SpacesPSC = (24 - len(str(ErrorPSC)))*' '
        print(Distance,Spaces, ErrorEC, SpacesEC, ErrorESC,SpacesESC,ErrorPSC,SpacesPSC,ErrorASC)
    return None

def ErrorCompare():
    for i in range(200):
        P1 = StringToCoord(tests.loc[i,'Point 1'])
        P2 = StringToCoord(tests.loc[i,'Point 2'])
        P3 = StringToCoord(tests.loc[i,'Point 3'])
        
        EllipticalCenter = ArcCenter(P1, P2, P3, "Degrees")
        EquatorSphereCenter = SphericalCenter(P1, P2, P3, "Degrees", RadiusNearEquator)
        PolarSphereCenter = SphericalCenter(P1, P2, P3, "Degrees", RadiusNearPoles)
        AverageSphereCenter = SphericalCenter(P1, P2, P3, "Degrees", AverageRadius)
        
        ErrorEC = ErrorTest(P1, P2, P3, EllipticalCenter, "Degrees")
        ErrorESC = ErrorTest(P1, P2, P3, EquatorSphereCenter, "Degrees")
        ErrorPSC = ErrorTest(P1, P2, P3, PolarSphereCenter, "Degrees")
        ErrorASC = ErrorTest(P1, P2, P3, AverageSphereCenter, "Degrees")
        
        Heading = tests.loc[i,'Approximate Center']
        if type(Heading) == str:
            print(Heading)
            
        Distance = tests.loc[i,'Approximate Distance']
        if type(Distance) == float:
            Distance = "N/A"
        
        Least = min(ErrorEC,ErrorESC,ErrorPSC,ErrorASC)
        if Least == ErrorEC:
            Type = "EC"
        elif Least == ErrorESC:
            Type = "ESC"
        elif Least == ErrorPSC:
            Type = "PSC"
        elif Least == ErrorASC:
            Type = "ASC"
        Spaces = (11 - len(Distance))*' '
        
        if Type != "EC":
            Diff = ErrorEC - Least
            print (Distance,Spaces, Type,Least, Diff)
        
        return None
    