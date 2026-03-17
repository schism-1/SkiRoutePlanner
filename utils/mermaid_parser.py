import re

def parse_mermaid(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    graph = {}
    node_data = {}

    # Matches definitions like: LiftA [[...]] or Piste1 ([...])
    def_pattern = re.compile(r'(\w+)\s*(?:\[\[|\(\[|\[)([^\]\)]+)(?:\]\]|\]\)|\])')
    # Matches edges like: LiftA --> Piste1
    edge_pattern = re.compile(r'(\w+)\s*-->\s*(\w+)')

    for match in def_pattern.finditer(content):
        node_id, raw_props = match.groups()
        props = raw_props.split('<br/>')[-1].split(';')
        node_data[node_id] = [p.strip() for p in props]
        if node_id not in graph:
            graph[node_id] = []

    for match in edge_pattern.finditer(content):
        start_node, end_node = match.groups()
        if start_node in graph:
            graph[start_node].append(end_node)
        else:
            graph[start_node] = [end_node]
    
    return graph, node_data

ski_graph, details = parse_mermaid("example_graph.txt")
print("Graph", ski_graph)
print("data", details)

