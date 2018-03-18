# Importing the libraries which are used in the program

import csv
import sys
import os
import heapq

# Initialization of the global variables

nw_matrix = []
link_cost = {}
nw_edge = []
node_int = {}
path = []
enter_comm = 0

# Menu for the user from which they can select the operation to be performed

print("\n")
print("**************************************************************************")
print("*########################################################################*")
print("*########################################################################*")
print("*###########   Welcome to CS542 Link State Routing Simulator  ###########*")
print("*########################################################################*")
print("*########################################################################*")
print("*                                                                        *")      
print("*########################################################################*")
print("*###### Select the operation to be performed from the below option ######*")
print("*########################################################################*")
print("*                                                                        *")
print("*########################################################################*")
print("*###### (1) Create a Network Topology                              ######*")
print("*###### (2) Build a forward Table                                  ######*")
print("*###### (3) Shortest Path to Destination Router                    ######*")
print("*###### (4) Change the status of the Router                        ######*")
print("*###### (5) Best Router for Broadcast                              ######*")
print("*###### (6) Exit                                                   ######*")
print("*########################################################################*")
print("**************************************************************************")
#print("\n")
      
# Dijkstra algorithm implementation starts here

def dijkstra(root):
    # Variables are declared which are used to implementation
    global link_cost
    global unVisi
    global lastNode
    global visitedNode
    global node_int
    unVisi = {}
    visitedNode = {}
    lastNode = {}
    node_int = {}
    index_n = root
    currentDistance = 0
    
    # Interate through each vertex
    
    for v in nw_edge:
        unVisi[v] = float('inf')
        visitedNode[v] = None
        lastNode[v] = None
        node_int[v] = []
    unVisi[index_n] = currentDistance
    
    # As long as the un-visited nodes are greater than 0 perform the below
    
    while len(unVisi) > 0:
        for Node_n, cost in link_cost[index_n].items():
            if Node_n not in unVisi: continue
            newCost = currentDistance + cost
            if newCost < unVisi.get(Node_n, float('inf')):
                lastNode[Node_n] = index_n
                unVisi[Node_n] = newCost
                if node_int[index_n]:
                    node_int[Node_n] = list(node_int[index_n])
                else:
                    node_int[Node_n] = [Node_n]
        visitedNode[index_n] = currentDistance
        del unVisi[index_n]
        if not unVisi: break
        currentStatus = []
        for v in unVisi.items():
            if v[1]:
                currentStatus.append(v)
        index_n, currentDistance = sorted(currentStatus, key=lambda x: x[1])[0]

# Validating the user choice. There are six options for the user to choose.
# If the user choose anything other than option 1, 2, 3, 4 ,5 and 6 then the 
# message to enter the number which available to the user
        
while enter_comm !=6 :
    print("\n")
    print("**************************************************************************")
    print("Enter Choice: ")
    enter_comm = input()
    print("**************************************************************************")
    
    # Validating if the choice is digit or not
    
    if not enter_comm.isdigit():
        print ("Please re-enter a number from given choices.")
    else:
        enter_comm = int(enter_comm)
        
        # Validating if the user enter the number between 1 and 6
        
        if enter_comm > 6 or enter_comm < 1 :
            print ("Please re-enter a valid number from given choices.")
            
    # If the user enter the choice 1 then user need to input the topology
    # matrix data file in the (.txt) format
    
    if enter_comm == 1:
        print("\n")
        print("**************************************************************************")
        print("\nInput original network topology matrix data file in (.txt) format: ")
        file = input()
        print("**************************************************************************")
        nw_matrix = []
        link_cost = {}
        nw_edge = []
        
        # Valdating the format of the file
        
        if os.path.exists(file) and os.path.getsize(file) > 0 and file.endswith('.txt'):
            
            # Printing the Original Topology Matrix
            
            print("\n")
            print("**************************************************************************")
            print("*########################################################################*")
            print("*##########              Original Topology Matrix              ##########*")
            print("*########################################################################*")
            nwMatrix = open(file,"r")
            nw_matrix = []
            for x in nwMatrix:
                nw_matrix.append(list(map(int, x.split())))
            for line in nw_matrix:
                for item in line:
                    print(item, end='    ')
                print()
            print("**************************************************************************")
            print("\n")
            nOfN = len(nw_matrix)
            
            # Printing the number of nodes present in the topology matrix
            
            print("**************************************************************************")
            print("Total number of nodes present in the topology matrix: ", nOfN)
            print("**************************************************************************")
            
            # Creating the matrix dictionary
            
            for i in range(nOfN):
                link_cost[i + 1] = {j + 1 : nw_matrix[i][j] for j in range(nOfN) if i != j and nw_matrix[i][j] != -1}
                nw_edge.append(i + 1)
                
            # Printing the matrix dictionary
            
            print("\n")
            print("**************************************************************************")
            print("Final topology matrix dictionary --> ", link_cost)
            print("**************************************************************************")
            
            root = 0
            end_res = 0
            down_router=0
            
        # Printing to insert the filename again if the format is not proper
        
        else:
            print("Please check the format of the file and insert it again.")
            
    # If the user enter the choice 2 then user need to input the source router
    
    elif enter_comm == 2:
        print("\n")
        print("**************************************************************************")
        print("Enter the source router:")
        root = input()
        print("**************************************************************************")
        
        # Validating the Source router
        
        if root.isdigit() and int(root) > 0 and int(root) <= len(nw_matrix):
            root = int(root)
            dijkstra(root)
            print("\n")
            print("**************************************************************************")
            print("Router %s Connection Table:"%root)
            print("Destination Router\tInterface")
            for key in node_int:
                print("\t",key, "\t\t", node_int[key])
            print("**************************************************************************")
                
        # Validating if the source router is 0 then enter the valid source router
        
        else:
            root = 0
            print ("\nPlease enter a valid source router.")
            
    # If the user enter the choice 3 then user need to input the destination router
    
    elif enter_comm == 3:
        print("\n")
        print("**************************************************************************")
        print("Enter the destination router:")
        end_res = input()
        print("**************************************************************************")
        
        # Validating the Destination router
        
        if end_res.isdigit() and int(end_res) > 0 and int(end_res) <= len(nw_matrix):
            if int(root) == 0:
                print ("\nNo source router selected yet. Please select a source router using choice : 2")
                
            # Validating if the source router and destination router is equal or not
            
            elif int(root) == int(end_res):
                print ("\nSource and Destination routers are same. Please select a different destination router.")
            else:
                end_res = int(end_res)
                new_d = end_res
                print("\n")
                print("**************************************************************************")
                print("Minimum Cost from %s to %s is %s" % (root, end_res, visitedNode[end_res]))
                path = []
                while 1:
                    path.append(end_res)
                    if end_res == root:
                        break
                    end_res = lastNode[end_res]
                path.reverse()
                end_res = new_d
                
                # Printing the shortest path between source and destination
                
                print("\nShortest Path from %s to %s is %s"%(root,end_res,path))
                print("**************************************************************************")
                
        # If destination router is not valid then re-enter the valid destination router
        
        else:
            print ("\nPlease re-enter a valid destination router.")
            
    # If the user enter the choice 4 then user need to input the router to be modify
    
    elif enter_comm == 4:
        global unVisi
        print("\n")
        print("**************************************************************************")
        print("Enter the router to be deleted:")
        down_router = input()
        print("**************************************************************************")
        
        if int(root) == 0 or int(end_res) == 0:
                print ("\nNo router selected yet. Please select a missing router")
                
        
        # Validating the router to be modify if its same as source router 
        
        elif int(down_router) == int(root):
            print("Router same as source node. Please enter choice again.")
            
        # Validating the router to be modify if its same as destination router
        
        elif int(down_router) == int(end_res):
            print("Router same as destination node. Please enter the choice again.")
            
        # Validating the router to be modify
        
        elif down_router.isdigit() and int(down_router) > 0 and int(down_router) <= len(nw_matrix):
            down_router = int(down_router)
            z = down_router - 1
            for i in range(nOfN):
                link_cost[i + 1] = {j + 1 : nw_matrix[i][j] for j in range(nOfN) if i != j != z and i != j and nw_matrix[i][j] != -1}
            del link_cost[down_router]
            del nw_edge[z]
            dijkstra(root)
            print("\n")
            print("**************************************************************************")
            print("Router %s Connection Table:" % root)
            print("Destination Router\tInterface")
            for key in node_int:
                print("\t",key, "\t\t", node_int[key])
            path = []
            end_res2 = end_res
            while 1:
                path.append(end_res)
                if end_res == root:
                    break
                end_res = lastNode[end_res]
            path.reverse()
            end_res = end_res2
            print("**************************************************************************")
            print("\n")
            print("**************************************************************************")
            print("Updated shortest path:",path)
            print("\nUpdated shortest distance:",visitedNode[end_res])
            print("**************************************************************************")
            h = [k for k in link_cost]
        else:
            print ("\nPlease re-enter a valid router.")
            
    # If the user enter the choice 5 then print the best router with the lowest cost
    
    elif enter_comm == 5:
        
        if int(root) == 0 or int(end_res) == 0 or int(down_router) == 0:
            print ("\nNo router selected yet. Please select a missing router")
        else:
            nw_new_ar = []
            nw_arr = []
            print("\n")
            print("**************************************************************************")
            print("\tRouter\t\tTotal_Cost")
        
            # Find the best router for the updated matrix
        
            for f in h:
                dijkstra(f)
                l = 0
                for k,v in visitedNode.items():
                    l = l + v
                print("\t",f,"\t\t",l)
                nw_new_ar.append(f)
                nw_arr.append(l)
            u = min(nw_arr)
            v = nw_arr.index(u)
            t = nw_new_ar[v]
            print("**************************************************************************")
            print("\n")
            print("**************************************************************************")
            print("Best Router is %s with lowest cost %s"%(t,u))
            print("**************************************************************************")
        
    # If the user enter the choice 6 then exit
    
    else:
        print("\n")
        print("**************************************************************************")
        print ("Exit CS542 project. Good Bye!")
        print("**************************************************************************")
        print("\n")
        break
