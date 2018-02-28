#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:50:33 2018
Purpose: Create a random team generator
Authors: Brock Freeland
"""

import random

def selectionSort(keys,data):
    '''
    Sorts parallel lists of keys and data values in ascending order
    using the selection sort algorithm
    
    Parameters:
        Keys: a list of keys
        data: a list of data values corresponding to the keys 

    Return Value: None
    '''
    n = len(keys)
    for start in range(n-1):  
        minIndex = start #sets minIndex equal to start value in range each iteration
        for index in range(start + 1,n): #starts comparing the second position to the first position and travels the length of the list
            if keys[index] < keys[minIndex]: #if the number is less than the one it’s comparing, it reassigns
                minIndex = index
        swap(keys,start,minIndex) #calls swap function in order to swap positions start and minIndex
        swap(data,start,minIndex) #swaps with keys so that the lists stay parallel 

def swap(data,start,minIndex):
    '''
    Swaps positions start and minIndex

    Parameters:
        data: a list of data values corresponding to the keys
        start:position in data
        minIndex: position in data different from start

    Return Value: None
    '''
    temp = data[start] #assigns temp as data[start] value
    data[start] = data[minIndex] #assigns data[start] value to data[minIndex] value
    data[minIndex] = temp # assigns data[minIndex] value to temp value.
#effectively swapping the values of the two positions in the list


def positionsDictionary():
    """
    Creates a dictionary with corresponding names and their positions
   
    Return Value: the ordered dictionary
    """

    stats = open('volleyball_stats.csv', 'r', encoding="utf-8") #imports csv file 
    names = [] #creates empty lists
    positions = []
    line = stats.readline() #removes headers
    for line in stats: #iterates through each line of the csv file 
        field = line.split(",") #splits them by commas in order to read individual data entries 
        names.append(field[0]) #appends specific column to assigned list
        positions.append(field[2])   
    Names_Pos = dict(zip(names,positions)) # creates dictionary with parallel lists
    return Names_Pos

def totalDictionary():
    """
    Creates a dictionary with Names with their corresponding total score
   
    Return Value: the ordered dictionary
    """
    #same process as positionsDictionary
    stats = open('volleyball_stats.csv', 'r', encoding="utf-8")
    names = []
    total = []
    line = stats.readline()
    for line in stats:
        field = line.split(",")
        names.append(field[0]) #appends specific column to assigned list
        total.append(float(field[3])+float(field[4])+float(field[5]) + \
                     float(field[6])+float(field[7])+float(field[8])+ \
                     float(field[9])+ float(field[10]) + float(field[11])) #adds up each skill ranking in the dataset, to create a total score for volleyball ability
    selectionSort(total,names) #calls selection sort function to sort the players based on total computed skill
    Names_Total = dict(zip(names,total)) # creates dictionary with parallel lists
    return Names_Total

def genderDictionary():
    stats = open('volleyball_stats.csv', 'r', encoding="utf-8") #imports csv file 
    names = [] #creates empty lists
    gender = []
    line = stats.readline() #removes headers
    for line in stats: #iterates through each line of the csv file 
        field = line.split(",") #splits them by commas in order to read individual data entries 
        names.append(field[0]) #appends specific column to assigned list
        gender.append(field[1])   
    Names_Gen = dict(zip(names,gender)) # creates dictionary with parallel lists
    return Names_Gen


def rankedPositions(team1,team2):
    """
    Creates ranked lists of player based on position
    
    Parameters:
        team1: team one list
        team2: team two list

    Return Value: None
    """
#imports created dictionaries earlier in program
    Names_Pos = positionsDictionary()
    Names_Total = totalDictionary()
    Names_Gen = genderDictionary()
    Ordered_Total = dict(Names_Total)   
    
#creates empty lists
    M_Hitters = []
    F_Hitters = []
    M_Setters = []
    F_Setters = []
    M_Passers = []
    F_Passers = []
    
        
    Ranked_M_Hitters = []
    Ranked_F_Hitters = []
    Ranked_M_Setters = []
    Ranked_F_Setters = []
    Ranked_M_Passers = []
    Ranked_F_Passers = []
    
    
#iterates through position dictionary to make lists of names broken down by position 
    for index in Names_Pos:
        if Names_Pos[index] == "Hitter":
                if Names_Gen[index] == "M":
                    M_Hitters.append(index)
                else:
                    F_Hitters.append(index)
   
               
#iterates through ordered dictionary, if name is found in position dictionary, appends to ranked positional list. This ensures that the ranked list will be based on sorted total values for each player
    for index in Ordered_Total:
        if index in M_Hitters:
            Ranked_M_Hitters.append(index)
   
    for index in Ordered_Total:
        if index in F_Hitters:
            Ranked_F_Hitters.append(index)   
           
    print(Ranked_F_Hitters)
    #breakup(Ranked_M_Hitters,team1,team2) #calls breakup function with ranked list, and the two team lists
    breakup(Ranked_F_Hitters,team1,team2)

##same process as previous segment, just a different position
#    for index in Names_Pos:
#        if Names_Pos[index] == "Setter":
#                if Names_Gen[index] == "M":
#                    M_Setters.append(index)
#
#                else:
#                    F_Setters.append(index)
#    for index in Ordered_Total:
#        if index in M_Setters:
#            Ranked_M_Setters.append(index)
#        else:
#            Ranked_F_Setters.append(index)
#    print(Ranked_M_Setters,Ranked_F_Setters)
#    breakup(Ranked_M_Setters,team1,team2)
#    breakup(Ranked_F_Setters,team1,team2)

#same process as previous segment, just a different position
#    for index in Names_Pos:
#        if Names_Pos[index] == "Passer":
#                if Names_Gen[index] == "M":
#                    M_Passers.append(index)
#                else:
#                    F_Passers.append(index)
#            
#    for index in Ordered_Total:
#        if index in M_Passers:
#            Ranked_M_Passers.append(index)
#        else:
#            Ranked_F_Passers.append(index)
#    breakup(Ranked_M_Passers,team1,team2)
#    breakup(Ranked_F_Passers,team1,team2)


def breakup(data,team1,team2):
    """
    Creates sublists for each positional list
    
    Parameters:
        data: the ranked positional list
        team1: team one list
        team2: team two list

    Return Value: None
    """

    n = len(data)
    mid = n //2 #creates a midway point of the list
#creates empty lists
    bottom = [] #bottom half of the players
    top = [] #top half of the players
    for index in range(n): 
        if index < mid: #if position is less than the midway point,
            bottom.append(data[index]) #append the positional value to the list 
        else:
            top.append(data[index])

#creates empty lists
    top_top = [] #highest ranking players of top list
    top_bottom = [] # lowest ranking players of top list
    bottom_top = [] #highest ranking players of bottom list
    bottom_bottom = [] #lowest ranking players of bottom list

    if len(data) >= 8: #if length of data is greater than or equal 8 (largest possible value that could be divided into fourths, and randomized later in program)
        for index in range(len(top)):
            if index < len(top)//2: # if position is less than the midpoint of the list, append to list
                top_bottom.append(top[index])
            else:
                top_top.append(top[index])

        for index in range(len(bottom)):
            if index >= len(top)//2: #if position is greater than the midpoint of the list, append to list
                bottom_bottom.append(bottom[index])
            else:
                bottom_top.append(bottom[index])

# calls distribute function with created sub lists, and the two team lists

        distribute(top_top,team1,team2) 
        distribute(top_bottom,team1,team2) 
        distribute(bottom_bottom,team1,team2) 
        distribute(bottom_top,team1,team2) 

    else: 
# calls distribute function with created sub lists, and the two team lists
        distribute(top,team1,team2)
        distribute(bottom,team1,team2)

def distribute(data,team1,team2):
    """
    Appends players to team1 or team2 based on the randomly selected position
    within the imported list
    
    Parameters:
        data: the ranked positional sublist
        team1: team one list
        team2: team two list

    Return Value: None
    """
    count = 0 #keeps track of number of appended values 
    if len(data)%2 ==1: #if length of data is odd
        while count<=len(data)//2+1: #runs while count is less than half the length of the list, + 1 (since it rounds down)
            n = random.randint(0,len(data)-1) #creates a random integer within the length of the list
            if data[n] not in team1 and data[n] not in team2: #if the random position value in the list is not in team 1 or team 2
                if len(team1) <= len(team2): 
                    team1.append(data[n])
                    count = count +1 
                else:
                    team2.append(data[n])
                    count = count +1
                
    
    else: #if length of data is even
#same process as previous loop 
         while count<len(data)//2+1:
            n = random.randint(0,len(data)-1)
            if data[n] not in team1 and data[n] not in team2:
                if len(team1) <= len(team2):
                    team1.append(data[n])
                    count = count +1
                else:
                    team2.append(data[n])
                    count = count +1


def main():

#creates empty lists to represent teams
    team1 = []
    team2 = []
    rankedPositions(team1,team2) #calls rankedPositions function to initiate random team generator
 #prints teams in an organized way
    print("Team 1: ",team1) 
    print("Team 2: ",team2)
    


main()