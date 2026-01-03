import networkx as nx

def build_graph(detections):
    g = nx.DiGraph()

    for d in detections:
        g.add_node(d["id"], type=d["type"])

    # Simple heuristic
    g.add_edge("alb-1", "eks-1")
    g.add_edge("eks-1", "vpc-1")

    return g
