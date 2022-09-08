
"""
busStop, a 2D array representing the IDs of the bus stations having a bus operating between them.
Input 

4 2
2 6
3 7
8 12
11 15

op - 12
"""
import itertools
def distanceCovered(busStops):
    busStops_list = [item for sublist in busStops for item in sublist]
    result_list = []

    #Iterate over the input route
    for each_list in busStops:
        #Get each route. Since it is a straight road we are considering first stop is less than second stop
        if each_list[0] < each_list[1]:
            #Get the distance between two station using while loop
            while not each_list[0] == each_list[1]:
                result_list.append([each_list[0], each_list[0]+1])
                each_list[0] += 1

    result_list.sort()
    result_list_final = list(l for l, _ in itertools.groupby(result_list))
    return {"Total Distance covered" : len(result_list_final), \
            "Station Route" : result_list_final}

def main():
    #input for busStops
    busStops = []
    busStops_rows,busStops_cols = map(int, input().split())

    for idx in range(busStops_rows):
        busStops.append(list(map(int, input().split())))

    result = distanceCovered(busStops)
    print(result)

if __name__ == "__main__":
    main()
