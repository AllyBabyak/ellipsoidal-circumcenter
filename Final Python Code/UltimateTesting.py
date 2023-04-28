# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:02:20 2023

@author: a.babyak
"""

from ForTesting import VincentyForward, ErrorTest
import random
from math import pi
from CoordinateConversions import DegreesToRadians
from Center import ArcCenter

## Parameters
MinimumDistance = 100000
MaximumDistance = 500000
MinimumLatitude = 60
MaximumLatitude = 65
MinimumLongitude = 0
MaximumLongitude = 360

def UltraTest():
    a = 0
    largest = 0
    for i in range(10000):
        ApproximateDistance = random.uniform(MinimumDistance,MaximumDistance)
        Latitude = random.uniform(MinimumLatitude, MaximumLatitude)
        Longitude = random.uniform(0, 360)

        Azimuth1 = random.uniform(0,2*pi)
        Azimuth2 = random.uniform(0,2*pi)
        Azimuth3 = random.uniform(0,2*pi)

        EstimatedCenter = DegreesToRadians((Latitude,Longitude))
        P1 = VincentyForward(EstimatedCenter, Azimuth1, ApproximateDistance)
        P2 = VincentyForward(EstimatedCenter, Azimuth2, ApproximateDistance)
        P3 = VincentyForward(EstimatedCenter, Azimuth3, ApproximateDistance)

        Center = ArcCenter(P1, P2, P3, "Radians")
        Error = ErrorTest(P1, P2, P3, Center, "Radians")
        
        if Error > 1e-3:
            if Error > largest:
                largest = Error
            a = a + 1
            SpacesA = (4 - len(str(a)))*' '
            SpacesP1 = (42 - len(str(P1)))*' '
            SpacesP2 = (42 - len(str(P2)))*' '
            SpacesP3 = (42 - len(str(P3)))*' '
            print(a,SpacesA,P1,SpacesP1,P2,SpacesP2,P3,SpacesP3,Error)
    print(largest)
    print("Done!")

def UltraTestV2():
    a = 0
    largest = 0
    for j in range(11):
        for i in range(10000):
            ApproximateDistance = random.uniform(MinimumDistance,MaximumDistance)
            Latitude = random.uniform(MinimumLatitude, MaximumLatitude)
            Longitude = random.uniform(0, 360)
    
            Azimuth1 = random.uniform(0,2*pi)
            Azimuth2 = random.uniform(0,2*pi)
            Azimuth3 = random.uniform(0,2*pi)
    
            EstimatedCenter = DegreesToRadians((Latitude,Longitude))
            P1 = VincentyForward(EstimatedCenter, Azimuth1, ApproximateDistance)
            P2 = VincentyForward(EstimatedCenter, Azimuth2, ApproximateDistance)
            P3 = VincentyForward(EstimatedCenter, Azimuth3, ApproximateDistance)
    
            Center = ArcCenter(P1, P2, P3, "Radians")
            Error = ErrorTest(P1, P2, P3, Center, "Radians")
            
            if Error > 10**(-j):
                if Error > largest:
                    largest = Error
                a = a + 1
        spacesj = (2-len(str(j)))*' '
        spacesa = (5-len(str(a)))*' '
        print("10 ^ -",j,spacesj,a,spacesa,largest)
        a = 0
    print("Done!")
    
def UltraTestVar(MinDis,MaxDis,MinLat,MaxLat):
    withError = 0
    largest = 0
    for j in range(11):
        for i in range(10000):
            ApproxDis = random.uniform(MinDis,MaxDis)
            Latitude = random.uniform(MinLat,MaxLat)
            Longitude = random.uniform(0, 360)
    
            Azimuth1 = random.uniform(0,2*pi)
            Azimuth2 = random.uniform(0,2*pi)
            Azimuth3 = random.uniform(0,2*pi)
    
            EstimatedCenter = DegreesToRadians((Latitude,Longitude))
            P1 = VincentyForward(EstimatedCenter, Azimuth1, ApproxDis)
            P2 = VincentyForward(EstimatedCenter, Azimuth2, ApproxDis)
            P3 = VincentyForward(EstimatedCenter, Azimuth3, ApproxDis)
            
            Center = ArcCenter(P1, P2, P3, "Radians")
            Error = ErrorTest(P1, P2, P3, Center, "Radians")
            
            if Error > 10**(-j):
                if Error > largest:
                    largest = Error
                    print(P1,P2,P3)
                withError = withError + 1
        spacesj = (2-len(str(j)))*' '
        spacesWE = (5-len(str(withError)))*' '
        print("10 ^ -",j,spacesj,withError,spacesWE,largest)
        withError = 0
    print("Done!")
    
def TestAllDis(MinLat,MaxLat):
    MinDis = 1
    MaxDis = 5
    while MinDis < 1000000:
        print(MinDis,'-',MaxDis)
        UltraTestVar(MinDis, MaxDis, MinLat, MaxLat)
        MinDis = MaxDis
        if str(MaxDis)[0] == '1':
            MaxDis = MaxDis * 5
        else:
            MaxDis = MaxDis * 2
    
TestAllDis(10,20)
