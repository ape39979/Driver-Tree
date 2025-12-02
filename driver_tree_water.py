from graphviz import Digraph

def create_water_driver_tree():
    # Create Digraph
    dot = Digraph("WaterInfrastructureDriverTree", format="png")
    dot.attr(rankdir="TB", newrank="true")  # Top to Bottom direction

    # Default node attributes
    dot.attr("node", shape="box", style="filled, rounded", fontname="Arial", fontsize="12", margin="0.2")

    # Colors (approximate from Mermaid classes)
    # Main Goal: fill:#2C3E50, text:white
    # Driver: fill:#34495E, text:white
    # SubDriver: fill:#5D6D7E, text:white
    # Lever: fill:#EAEDED, text:#333 (dark gray/black)

    c_main = "#2C3E50"
    c_driver = "#34495E"
    c_subdriver = "#5D6D7E"
    c_lever = "#EAEDED"

    t_white = "#ffffff"
    t_dark = "#333333"

    # Root Goal
    dot.node("Goal", "GOAL: Resolve Water Loss &\nHarden Infrastructure",
             fillcolor=c_main, fontcolor=t_white)

    # Level 1: Strategic Drivers
    dot.node("D1", "Driver 1:\nRestore Physical\nWater Supply",
             fillcolor=c_driver, fontcolor=t_white)
    dot.node("D2", "Driver 2:\nMitigate Operational\nRisk",
             fillcolor=c_driver, fontcolor=t_white)
    dot.node("D3", "Driver 3:\nFuture-Proof\nResiliency",
             fillcolor=c_driver, fontcolor=t_white)

    dot.edge("Goal", "D1")
    dot.edge("Goal", "D2")
    dot.edge("Goal", "D3")

    # Level 2: Sub-Drivers (Tactical)
    dot.node("D1_A", "Utility Bypass &\nFlow Restoration",
             fillcolor=c_subdriver, fontcolor=t_white)
    dot.node("D1_B", "Potable Water\nStockpiling",
             fillcolor=c_subdriver, fontcolor=t_white)

    dot.node("D2_A", "Site Safety &\nContainment",
             fillcolor=c_subdriver, fontcolor=t_white)
    dot.node("D2_B", "Community\nContinuity",
             fillcolor=c_subdriver, fontcolor=t_white)

    dot.node("D3_A", "Asset Renewal",
             fillcolor=c_subdriver, fontcolor=t_white)
    dot.node("D3_B", "Organizational\nReadiness",
             fillcolor=c_subdriver, fontcolor=t_white)

    dot.edge("D1", "D1_A")
    dot.edge("D1", "D1_B")
    dot.edge("D2", "D2_A")
    dot.edge("D2", "D2_B")
    dot.edge("D3", "D3_A")
    dot.edge("D3", "D3_B")

    # Level 3: Actionable Levers (Inputs)
    # Using 'none' or 'plain' edge style to mimic --- might just be standard edge in hierarchical graph
    # Levers have lighter color and dark text

    # D1_A Levers
    dot.node("L1", "Coord w/ City\nof Yokosuka", fillcolor=c_lever, fontcolor=t_dark)
    dot.node("L2", "Install Insertion\nValves", fillcolor=c_lever, fontcolor=t_dark)
    dot.edge("D1_A", "L1")
    dot.edge("D1_A", "L2")

    # D1_B Levers
    dot.node("L3", "NEXCOM Inventory\n(27k+ Units)", fillcolor=c_lever, fontcolor=t_dark)
    dot.node("L4", "SVP Coordination\n(12k+ Units)", fillcolor=c_lever, fontcolor=t_dark)
    dot.edge("D1_B", "L3")
    dot.edge("D1_B", "L4")

    # D2_A Levers
    dot.node("L5", "Trenching &\nExcavation", fillcolor=c_lever, fontcolor=t_dark)
    dot.node("L6", "Pedestrian\nFencing", fillcolor=c_lever, fontcolor=t_dark)
    dot.edge("D2_A", "L5")
    dot.edge("D2_A", "L6")

    # D2_B Levers
    dot.node("L7", "Medical/School\nprioritization", fillcolor=c_lever, fontcolor=t_dark)
    dot.node("L8", "Housing Distribution\nPoints", fillcolor=c_lever, fontcolor=t_dark)
    dot.edge("D2_B", "L7")
    dot.edge("D2_B", "L8")

    # D3_A Levers
    dot.node("L9", "Separate System\nPipeline", fillcolor=c_lever, fontcolor=t_dark)
    dot.node("L10", "Pipe/Valve\nRenewal Plan", fillcolor=c_lever, fontcolor=t_dark)
    dot.node("L12", "Utility\nMapping", fillcolor=c_lever, fontcolor=t_dark)
    dot.edge("D3_A", "L9")
    dot.edge("D3_A", "L10")
    dot.edge("D3_A", "L12")

    # D3_B Levers
    dot.node("L11", "Contingency\nDrills", fillcolor=c_lever, fontcolor=t_dark)
    dot.edge("D3_B", "L11")

    # Render
    output_filename = "WaterInfrastructureDriverTree"
    dot.render(output_filename)
    print(f"Generated {output_filename}.png")

if __name__ == "__main__":
    create_water_driver_tree()
