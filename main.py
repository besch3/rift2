import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
class Zone:
    def __init__(self, z_id):
        self.z_id = z_id
        self.owner_id = -1
        self.pods = [0, 0]
        self.visible = 0
        self.platinum = 0
    
    def update(self, owner_id, pods_p0, pods_p1, visible, platinum):
        self.owner_id = owner_id
        self.pods = [pods_p0, pods_p1]
        self.visible = visible
        if platinum > 0:
            self.platinum = platinum
        
class Map:
    def __init__(self, my_id, zone_count):
        self.my_id = my_id
        self.map_graph = {key: [] for key in range(zone_count)}
        self.zones = [Zone(z_id) for z_id in range(zone_count)]
        self.pods = list()
        self.own_teritorry = list()
        self.enemy_teritorry =list()
        self.unexplored = list()
        #not visited tile list
    
    def add_zones_to_map(self, z_id_1, z_id_2):
        self.map_graph[z_id_1].append(z_id_2)
        self.map_graph[z_id_2].append(z_id_1)
        
    def update(self, z_id, owner_id, pods_p0, pods_p1, visible, platinum):
        self.zones[z_id].update(owner_id, pods_p0, pods_p1, visible, platinum)
        my_pods = self.zones[z_id].pods[self.my_id]
        op_pods = self.zones[z_id].pods[1-self.my_id] #opponent_id =  1 - my_id
        if my_pods > 0:
            self.pods.append(Pod(z_id, my_pods, my_pods-op_pods))
            
    def move(self):
        moves = ""
        for p in self.pods:
            moves += p.move(self.map_graph)
        return moves

        
class Pod:
    def __init__(self, z_id, count, strength_delta):
        self.z_id = z_id
        self.count = count
        self.strength_delta = strength_delta
        
    def move_explore(self, graph): #simple random moves
        z = random.choice(graph[self.z_id])
        return str(self.count) + " " + str(self.z_id) + " " + str(z) + " "
    
    def move_target(self, zone):
        pass #move towards, target zone
    
    def move(self, graph):
        if 1: #decision logic needs improvement
           return self.move_explore(graph)
        else:
           return self.move_target(graph, 1)
    
    def need_help(self):
        #return platinum, number_of_pods needed to hold zone
        pass
    
    def evaluate(self):
        #calculate score, memorize move for pods on the same zone for this turn of
        pass
    
    def surrounding_tiles(self):
        pass
    
    
# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]

map_z = Map(my_id, zone_count)

for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    map_z.add_zones_to_map(zone_1, zone_2)

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    map_z.pods = list() #recalculate pods in the next step
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        map_z.update(z_id, owner_id, pods_p0, pods_p1, visible, platinum)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(map_z.pods, file=sys.stderr)

    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    print(map_z.move())
    print("WAIT")
