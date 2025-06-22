from matplotlib import pyplot as plt
import networkx as nx
import heapq

def dijkstra(graph, start):
    # Initialize the priority queue (min-heap)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (distance, vertex)
    
    # Initialize distances with infinity
    distances = {vertex: float('inf') for vertex in graph.nodes()}
    distances[start] = 0
    
    # Initialize the shortest path tree
    shortest_path_tree = {}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If the distance is greater than the recorded distance, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors
        for neighbor, attr in graph[current_vertex].items():
            weight = attr['weight']
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, shortest_path_tree

def draw_graph(G):
  pos = nx.spring_layout(G)  # positions for all nodes

  # Draw nodes
  nx.draw_networkx_nodes(G, pos, node_size=700)

  # Draw edges
  nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='black')

  # Draw labels
  labels = nx.get_node_attributes(G, 'label')
  nx.draw_networkx_labels(G, pos, labels, font_size=12)

  # Show the graph
  plt.title("Directed Graph Example")
  plt.axis('off')  # Turn off the axis
  plt.show()

def create_graph():
  # Create a directed graph
  G = nx.DiGraph()

  # Add nodes with attributes
  G.add_node("A", label="Start")
  G.add_node("B", label="Process")
  G.add_node("C", label="Decision")
  G.add_node("D", label="End")
  G.add_node("E", label="Loop")
  G.add_node("F", label="Final")

  # Add edges with weights
  G.add_edge("A", "B", weight=1)
  G.add_edge("B", "C", weight=2)
  G.add_edge("C", "D", weight=3)
  G.add_edge("C", "B", weight=1)  # Loop back to process
  G.add_edge("D", "E", weight=1)  # Decision to loop
  G.add_edge("E", "F", weight=2)  # Loop to final
  G.add_edge("F", "D", weight=1)  # Loop back to decision
  G.add_edge("F", "A", weight=1)  # Final back to start
  G.add_edge("B", "F", weight=2)  # Direct path from process to final
  G.add_edge("A", "C", weight=1)  # Direct path from start to decision
  G.add_edge("C", "F", weight=2)  # Direct path from decision to final
  G.add_edge("D", "B", weight=1)  # Loop back to process from end

  return G

# Example usage
if __name__ == "__main__":
    # Create a weighted graph
    G = create_graph()  
    
    start_vertex = "A"
    distances, shortest_path_tree = dijkstra(G, start_vertex)
    
    print("Shortest distances from vertex", start_vertex)
    for vertex in G.nodes():
        print(f"Vertex {vertex}: {distances[vertex]}")
    
    print("\nShortest path tree:")
    for vertex in shortest_path_tree:
        print(f"Vertex {vertex} is reached from {shortest_path_tree[vertex]}")

    print("\nDrawing the graph:")
    draw_graph(G)
# This code implements Dijkstra's algorithm using a binary heap (min-heap) to find the shortest paths in a weighted graph.
# It uses the NetworkX library to create and manage the graph structure.



