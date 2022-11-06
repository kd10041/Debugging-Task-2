# Print result after every function to check
# Read the info in every functions to get the proper understanding of desired output

import json
from multiprocessing.sharedctypes import Value

filepaths = r'C:\Users\kumar\OneDrive\Desktop\Devsoc Task\3_Debugging_Task\2\data.json'
# def read_data(filepaths):
with open(filepaths) as json_file:
    data = json.load(json_file)
# Read data from filepath
# data = read_data(filepaths)
# print(data)
def get_oldest(data):
        oldest=[]
        max = 0
        #c = 0

        for i in data["AVENGERS"]:
            if (data["AVENGERS"][i]['age'] >= max):
                max = data["AVENGERS"][i]['age']
                # oldest = data["AVENGERS"][i]

        for i in data["DC"]:
            if (data["DC"][i]['age'] >=max):
                max=data["DC"][i]['age']
                #oldest=data["DC"][i]
        for i in data["AVENGERS"]:
            if data["AVENGERS"][i]['age'] == max:
                oldest.append(data["AVENGERS"][i])
                #c+=1
        for i in data["DC"]:
            if data["DC"][i]['age'] == max:
                oldest.append(data["DC"][i])
                #c+=1

        
    # Return all info of the oldest superheroes
    # Return all info of the oldest superheroes
        return oldest
    #print(get_oldest(data))
# returns info: Thor and Wonder Woman


def get_oldest_avenger(data):
    max=0
    for i in data["AVENGERS"]:
        if (data["AVENGERS"][i]['age'] >max):
            max=data["AVENGERS"][i]['age']
            oldest_avenger=data["AVENGERS"][i]
    # Return all info of the oldest avenger
    return oldest_avenger
print(get_oldest_avenger(data))
# returns info: Thor 


def get_total_points(data):
    total_points={}
    for i in data["AVENGERS"]:
        key=data["AVENGERS"][i]["name"]
        total_points[key] = 0
        for j in data["AVENGERS"][i]['points']:
            total_points[key]+=data["AVENGERS"][i]['points'][j]
    for i in data["DC"]:
        key=data["DC"][i]["name"]
        total_points[key] = 0
        for j in data["DC"][i]['points']:
            total_points[key]+=data["DC"][i]['points'][j]
    # Return a dictionary
    # Key: superhero name
    # Value: total points
    return total_points
# returns info: Dict of superhero name and total points
print(get_total_points(data))

def get_more_than_average(data):
    more_than_average=[]
    avg_mcu=0
    avg_dc=0
    for i in data["AVENGERS"]:
        avg_mcu+=data["AVENGERS"][i]["points"]["stealth"]
    avg_mcu=avg_mcu/len(data["AVENGERS"])
    c=0
    for i in data["AVENGERS"]:
        if(data["AVENGERS"][i]['points']['stealth']>avg_mcu):
            more_than_average.append(data["AVENGERS"][i])
    for i in data["DC"]:
        avg_dc+=data["DC"][i]['points']['strength']
    avg_dc=avg_dc/len(data["DC"])
    for i in data["DC"]:
        if(data["DC"][i]['points']['strength']>avg_dc):
            more_than_average.append(data["DC"][i])
    '''
    Return list of superheroes with stealth more than average in MCU 
    and list of superheroes with strength more than average in DCU
    '''
    return more_than_average
    #returns info: Steve Rogers and Superman
    #print(get_more_than_average(data))
def get_names(data):
    names=[]
    c=0
    for i in data["AVENGERS"]:
        names.insert(c,data["AVENGERS"][i]["name"])
        c+=1
    for j in data["DC"]:
        names.insert(c,data["DC"][j]["name"])
    # Return a list of superhero names
    return names
#returns a list 
print(get_names(data))
