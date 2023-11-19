import matplotlib.pyplot as plt
import networkx as nx

def create_esca_research_methodology_mind_map(filename):
    plt.figure(figsize=(15, 10))

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    central_node = "Esophageal Carcinoma (ESCA) Research Methodology"
    main_nodes = [
        "Data Procurement and Organization", "Epigenetic, Transcriptional Network",
        "Identification of Regulators", "Statistical Corroboration", "Clinical Outcome Correlation",
        "Unsupervised Machine Learning for Validation", "Interactive Data Visualization", 
        "Statistical, Predictive model", "Advanced Data Interpretation", 
        "Multi-Omics Framework", "Figure 1 Illustration", "Plots using (Python)"
    ]

    # Add edges
    for main_node in main_nodes:
        G.add_edge(central_node, main_node)

    # Position nodes using spring layout
    pos = nx.spring_layout(G, k=0.1)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color="lightblue", alpha=0.7)
    nx.draw_networkx_nodes(G, pos, nodelist=[central_node], node_size=3500, node_color="lightgreen", alpha=0.9)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="gray")

    # Draw node labels with custom font settings
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold', font_family='Times New Roman')

    # Title with professional formatting
    plt.title("Mind Map: ESCA Research Methodology", fontsize=14, fontweight='bold', fontname='Times New Roman')
    plt.axis('off')

    # Save the figure in 300 DPI TIFF format
    plt.savefig('research_methodology_mind_map', format='tif', dpi=300)

# Usage
create_esca_research_methodology_mind_map("esca_research_methodology_map.tif")



