# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:20:28 2019

@author: wjlee
"""
import argparse

# Diffusion parameter selection
parser = argparse.ArgumentParser()
parser.add_argument('--saveGraph', type = bool, default = False,
                    help="To make graph type as gpickle")
parser.add_argument('--GraphName', type = str, default = "KarateClub",
                    help="There must be files whoes names are (DatasetName).community.txt & (DatasetName).ungraph.txt and this Datasetname is also used as Directory")
parser.add_argument('--case', default = "DFOA",
                    choices=["DFOA","CDIOA","CDFOA"], help="What's the case do you want to look?(default: DFOA)")
parser.add_argument('--q', type = float, default = 0,
                    help="Set q value(threshold), if you don't choose q value, then the program will chooose q value randomly.")
parser.add_argument('--c', type = float, default = 0,
                    help="Set c value(cost), if you don't choose c value, then the program will chooose c value randomly.")
args = parser.parse_args()


if __name__ == '__main__':
    saveGraph = args.saveGraph
    GraphName = args.GraphName
    print("........ GRAPH: {}".format(GraphName))
    # Make graph type as gpickle
    if saveGraph:
        import SaveGraph
        community, overlap, NODE = SaveGraph.PreprocessCommunity(GraphName)
        SaveGraph.LoadAndSaveGraph(GraphName, community, overlap, NODE)
    
    case = args.case
    q = args.q
    c = args.c
    
    import Diffusion as diffusion
    # Read graph & Set the nodes' behavior as B
    # Save the nodes in overlapped region
    # and the nodes which are 1-hop neighbor of nodes in overlapped region
    G, InOverlap, _1hop = diffusion.initialize(GraphName)
    # Do diffusion process & save the results
    if case == "DFOA":
        diffusion.DFOA(GraphName, G.copy(), InOverlap, _1hop, q)
    elif case == "CDIOA":
        diffusion.CDIOA(GraphName, G.copy(), InOverlap, _1hop, q, c)
    elif case == "CDFOA":
        diffusion.CDFOA(GraphName, G.copy(), InOverlap, _1hop, q, c)