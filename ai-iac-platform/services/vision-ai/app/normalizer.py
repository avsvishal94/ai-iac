def normalize_graph(graph):
    return {
        "cloud": "aws",
        "resources": [
            {"id": n, "type": graph.nodes[n]["type"]}
            for n in graph.nodes
        ],
        "edges": [
            {"from": u, "to": v}
            for u, v in graph.edges
        ]
    }
