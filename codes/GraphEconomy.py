class GraphEconomy: 
    #Doing a DFS on the Economy graph
    from collections import defaultdict 

    def __init__(self, importers = []): 
        # default dictionary to store graph 
        # initialize graph, edgeweights and importers list
        self.graph = self.defaultdict(list)
        self.edgeweights = self.defaultdict(list) 
        self.importers = importers

    def addEdges(self,edge_lst):

        """
        input raw edges with format of (source,sink,edgeweights)
        build graph dictionary from edge tuple pairs. 
        build dictionary with keys as edges and values as edge weights
        e.g. turn [(1,2,0.5),(1,3,0.2)] into {1:[2,3]} and {"1 2":0.5, "1 3":0.2} 
        """
        edges = []
        for i in edge_lst:
            edges.append((i[0],i[1])) 
            ew_key = str(i[0]) + " " + str(i[1])
            self.edgeweights[ew_key] = i[2]
        for k, v in edges:
            self.graph[k].append(v)

    def printEconomy(self):
        """
        print the current economy structure
        """
        print(self.graph)

    def findPaths(self, start, end, path=[]):
        """
        input the starting node and the ending node
        find all possible connecting paths recursively
        """
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.findPaths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def sumWeights(self,paths):
        """
        with the found paths, calculate the summed weights of all the edges
        """
        summed = 0
        for path in paths:
            if len(path) == 1:
                summed = summed + self.importers[path[0]]
            else:
                for i in range(len(path) - 1):
                    key = str(path[i]) + " " + str(path[i + 1])
                    if path[i] in self.importers:
                        summed = summed + self.importers[path[i]] * self.edgeweights[key]
                    else:
                        summed = summed + self.edgeweights[key]
        return summed

if __name__ == '__main__':

    # testing cases
    raw edges = [(1,2,0.7),\
            (1,5,0.3),\
            (3,1,.03),\
            (3,4,.8),(4,6,.01),(6,5,.2),(5,2,.03)] # raw edges
    importers = {1:.45,4:.72} # importers
    test = [2,1,3] # testing target nodes

    # initialize economy with the 
    economy = GraphEconomy(importers)

    # build the graph through raw edges
    economy.addEdges(raw edges)

    # find all paths between an importer and a target 
    
    for i in list(importers.keys()):
        for j in test:
            print("from " + str(i) + " to " + str(j) + " " + str(economy.sumWeights(economy.findPaths(i,j))))


