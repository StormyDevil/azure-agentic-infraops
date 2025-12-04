"""
Agentic InfraOps Workflow Diagram - PowerPoint Theme
Matches the dark purple gradient theme with orange/coral accents
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
import os

# Create icons directory if needed
icons_dir = os.path.join(os.path.dirname(__file__), "icons")
os.makedirs(icons_dir, exist_ok=True)

# Graph attributes for dark theme
graph_attr = {
    "bgcolor": "#1a1a2e",  # Dark purple background
    "fontcolor": "#ffffff",
    "fontname": "Segoe UI",
    "fontsize": "14",
    "pad": "0.5",
    "splines": "curved",
    "nodesep": "0.8",
    "ranksep": "1.0",
}

# Cluster styling
cluster_attr = {
    "bgcolor": "#16213e",  # Slightly lighter purple
    "fontcolor": "#ffffff",
    "fontname": "Segoe UI Bold",
    "fontsize": "13",
    "style": "rounded",
    "pencolor": "#0f3460",
    "penwidth": "2",
}

# Node styling - using box nodes with custom colors
node_attr = {
    "fontname": "Segoe UI",
    "fontsize": "11",
    "fontcolor": "#ffffff",
    "style": "filled,rounded",
    "shape": "box",
    "penwidth": "0",
    "margin": "0.3,0.2",
}

# Edge styling
edge_attr = {
    "color": "#94a3b8",
    "fontcolor": "#94a3b8",
    "fontname": "Segoe UI",
    "fontsize": "10",
    "penwidth": "1.5",
}

# Color palette matching PowerPoint theme
COLORS = {
    "orange": "#FF6B35",      # Primary accent (title color)
    "coral": "#f4722b",       # Secondary accent
    "blue": "#0078D4",        # Azure blue
    "green": "#10b981",       # Success green
    "yellow": "#fbbf24",      # Warning/optional yellow
    "purple": "#8b5cf6",      # Purple accent
    "pink": "#ec4899",        # Pink accent
    "teal": "#14b8a6",        # Teal
    "gray": "#64748b",        # Muted gray
    "dark_bg": "#1a1a2e",     # Dark background
    "card_bg": "#16213e",     # Card background
}

# Create the diagram using graphviz directly for more control


def create_workflow_diagram():
    """Generate the workflow diagram with PowerPoint theme."""

    dot_content = f'''
digraph AgenticInfraOps {{
    // Graph settings
    graph [
        bgcolor="{COLORS['dark_bg']}"
        fontcolor="white"
        fontname="Segoe UI"
        fontsize="16"
        pad="0.5"
        splines="ortho"
        nodesep="0.6"
        ranksep="0.8"
        rankdir="TB"
        dpi="150"
    ]
    
    node [
        fontname="Segoe UI"
        fontsize="11"
        fontcolor="white"
        style="filled,rounded"
        shape="box"
        penwidth="0"
        margin="0.25,0.15"
    ]
    
    edge [
        color="#64748b"
        fontcolor="#94a3b8"
        fontname="Segoe UI"
        fontsize="9"
        penwidth="2"
        arrowsize="0.8"
    ]
    
    // Title (invisible node for spacing)
    title [label="" shape="none" height="0.1"]
    
    // Step 1: Requirements
    subgraph cluster_step1 {{
        label="Step 1: Requirements"
        fontcolor="white"
        fontname="Segoe UI Semibold"
        fontsize="12"
        bgcolor="{COLORS['card_bg']}"
        style="rounded"
        pencolor="#0f3460"
        penwidth="2"
        
        plan [
            label="@plan\\n(built-in)"
            fillcolor="{COLORS['blue']}"
        ]
    }}
    
    // Step 2: Architecture
    subgraph cluster_step2 {{
        label="Step 2: Architecture"
        fontcolor="white"
        fontname="Segoe UI Semibold"
        fontsize="12"
        bgcolor="{COLORS['card_bg']}"
        style="rounded"
        pencolor="#0f3460"
        penwidth="2"
        
        architect [
            label="azure-principal-architect\\n(NO CODE)"
            fillcolor="{COLORS['orange']}"
        ]
        
        // Optional tools cluster
        subgraph cluster_optional2 {{
            label="Optional"
            fontcolor="#94a3b8"
            fontsize="10"
            bgcolor="#0f3460"
            style="rounded,dashed"
            pencolor="#334155"
            
            mcp [
                label="💰 Azure Pricing MCP\\n(real-time costs)"
                fillcolor="{COLORS['yellow']}"
                fontcolor="#1a1a2e"
            ]
            
            diagrams [
                label="📊 diagram-generator\\n(visualization)"
                fillcolor="{COLORS['purple']}"
            ]
            
            adr1 [
                label="📝 adr-generator\\n(decisions)"
                fillcolor="{COLORS['teal']}"
            ]
        }}
    }}
    
    // Step 3: Planning
    subgraph cluster_step3 {{
        label="Step 3: Planning"
        fontcolor="white"
        fontname="Segoe UI Semibold"
        fontsize="12"
        bgcolor="{COLORS['card_bg']}"
        style="rounded"
        pencolor="#0f3460"
        penwidth="2"
        
        bicep_plan [
            label="bicep-plan\\n(plan only)"
            fillcolor="{COLORS['green']}"
        ]
    }}
    
    // Step 4: Implementation
    subgraph cluster_step4 {{
        label="Step 4: Implementation"
        fontcolor="white"
        fontname="Segoe UI Semibold"
        fontsize="12"
        bgcolor="{COLORS['card_bg']}"
        style="rounded"
        pencolor="#0f3460"
        penwidth="2"
        
        bicep_implement [
            label="bicep-implement\\n(code generation)"
            fillcolor="{COLORS['pink']}"
        ]
        
        // Optional ADR
        subgraph cluster_optional4 {{
            label="Optional"
            fontcolor="#94a3b8"
            fontsize="10"
            bgcolor="#0f3460"
            style="rounded,dashed"
            pencolor="#334155"
            
            adr2 [
                label="📝 adr-generator"
                fillcolor="{COLORS['teal']}"
            ]
        }}
    }}
    
    // Main workflow edges
    plan -> architect [xlabel="requirements" color="{COLORS['blue']}" fontcolor="{COLORS['blue']}"]
    architect -> bicep_plan [xlabel="architecture" color="{COLORS['orange']}" fontcolor="{COLORS['orange']}"]
    bicep_plan -> bicep_implement [xlabel="plan" color="{COLORS['green']}" fontcolor="{COLORS['green']}"]
    
    // Optional edges (dashed)
    mcp -> architect [style="dashed" xlabel="pricing" color="{COLORS['yellow']}" fontcolor="{COLORS['yellow']}"]
    diagrams -> architect [style="dashed" color="{COLORS['purple']}"]
    adr1 -> architect [style="dashed" color="{COLORS['teal']}"]
    mcp -> bicep_plan [style="dashed" xlabel="costs" color="{COLORS['yellow']}" fontcolor="{COLORS['yellow']}"]
    adr2 -> bicep_implement [style="dashed" color="{COLORS['teal']}"]
    
    // Invisible edges for layout
    {{rank=same; plan}}
    {{rank=same; architect; mcp; diagrams; adr1}}
    {{rank=same; bicep_plan}}
    {{rank=same; bicep_implement; adr2}}
}}
'''

    return dot_content


def create_simple_workflow():
    """Create a simpler horizontal workflow for README."""

    dot_content = f'''
digraph SimpleWorkflow {{
    graph [
        bgcolor="{COLORS['dark_bg']}"
        fontcolor="white"
        fontname="Segoe UI"
        pad="0.4"
        splines="curved"
        nodesep="0.5"
        ranksep="0.6"
        rankdir="LR"
        dpi="150"
    ]
    
    node [
        fontname="Segoe UI"
        fontsize="11"
        fontcolor="white"
        style="filled,rounded"
        shape="box"
        penwidth="0"
        margin="0.2,0.15"
    ]
    
    edge [
        color="#64748b"
        fontcolor="#94a3b8"
        fontname="Segoe UI"
        fontsize="9"
        penwidth="2"
        arrowsize="0.7"
    ]
    
    // Main workflow nodes
    plan [label="@plan" fillcolor="{COLORS['blue']}"]
    architect [label="azure-principal-\\narchitect" fillcolor="{COLORS['orange']}"]
    bicep_plan [label="bicep-plan" fillcolor="{COLORS['green']}"]
    bicep_implement [label="bicep-implement" fillcolor="{COLORS['pink']}"]
    
    // Optional nodes
    mcp [label="💰 Pricing MCP" fillcolor="{COLORS['yellow']}" fontcolor="#1a1a2e"]
    diagrams_node [label="📊 Diagrams" fillcolor="{COLORS['purple']}"]
    
    // Main flow
    plan -> architect -> bicep_plan -> bicep_implement
    
    // Optional connections
    mcp -> architect [style="dashed" constraint="false"]
    mcp -> bicep_plan [style="dashed" constraint="false"]
    diagrams_node -> architect [style="dashed" constraint="false"]
    
    // Layout hints
    {{rank=same; mcp; diagrams_node}}
}}
'''

    return dot_content


if __name__ == "__main__":
    import subprocess

    output_dir = os.path.dirname(__file__)

    # Generate full workflow diagram
    print("🎨 Generating themed workflow diagram...")
    full_dot = create_workflow_diagram()
    full_dot_path = os.path.join(output_dir, "workflow_themed.dot")
    full_png_path = os.path.join(output_dir, "workflow_themed.png")
    full_svg_path = os.path.join(output_dir, "workflow_themed.svg")

    with open(full_dot_path, "w") as f:
        f.write(full_dot)

    # Generate PNG and SVG
    subprocess.run(["dot", "-Tpng", "-Gdpi=150", full_dot_path,
                   "-o", full_png_path], check=True)
    subprocess.run(["dot", "-Tsvg", full_dot_path,
                   "-o", full_svg_path], check=True)
    print(f"✅ Generated: {full_png_path}")
    print(f"✅ Generated: {full_svg_path}")

    # Generate simple workflow diagram
    print("\n🎨 Generating simple workflow diagram...")
    simple_dot = create_simple_workflow()
    simple_dot_path = os.path.join(output_dir, "workflow_simple.dot")
    simple_png_path = os.path.join(output_dir, "workflow_simple.png")
    simple_svg_path = os.path.join(output_dir, "workflow_simple.svg")

    with open(simple_dot_path, "w") as f:
        f.write(simple_dot)

    subprocess.run(["dot", "-Tpng", "-Gdpi=150", simple_dot_path,
                   "-o", simple_png_path], check=True)
    subprocess.run(["dot", "-Tsvg", simple_dot_path,
                   "-o", simple_svg_path], check=True)
    print(f"✅ Generated: {simple_png_path}")
    print(f"✅ Generated: {simple_svg_path}")

    print("\n🎉 All diagrams generated successfully!")
    print(f"\nFiles created in: {output_dir}")
