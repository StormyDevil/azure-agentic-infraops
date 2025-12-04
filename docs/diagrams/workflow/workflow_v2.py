"""
Agentic InfraOps Workflow Diagram v2 - PowerPoint Theme
Numbered steps with cleaner layout
"""

import os
import subprocess

# Color palette matching PowerPoint theme
COLORS = {
    "orange": "#FF6B35",      # Primary accent (title color)
    "blue": "#0078D4",        # Azure blue
    "green": "#10b981",       # Success green
    "yellow": "#fbbf24",      # Warning/optional yellow
    "purple": "#8b5cf6",      # Purple accent
    "pink": "#ec4899",        # Pink accent
    "teal": "#14b8a6",        # Teal/cyan
    "gray": "#64748b",        # Muted gray
    "dark_bg": "#1a1a2e",     # Dark background
    "light_gray": "#94a3b8",  # Light gray for labels
}


def create_workflow_diagram():
    """Generate the numbered workflow diagram - widescreen horizontal."""

    dot_content = f'''
digraph AgenticInfraOps {{
    // Graph settings - WIDESCREEN HORIZONTAL
    graph [
        bgcolor="{COLORS['dark_bg']}"
        fontcolor="white"
        fontname="Segoe UI, Arial, sans-serif"
        pad="0.8"
        splines="ortho"
        nodesep="0.6"
        ranksep="1.0"
        rankdir="LR"
        dpi="150"
    ]
    
    node [
        fontname="Segoe UI, Arial, sans-serif"
        fontsize="11"
        fontcolor="white"
        style="filled,rounded"
        shape="box"
        penwidth="0"
        margin="0.2,0.12"
    ]
    
    edge [
        color="{COLORS['gray']}"
        fontcolor="{COLORS['light_gray']}"
        fontname="Segoe UI, Arial, sans-serif"
        fontsize="9"
        penwidth="2"
        arrowsize="0.7"
    ]

    // ============================================
    // STEP 1: PLAN
    // ============================================
    step1 [
        label="1. Plan\\n@plan (built-in)"
        fillcolor="{COLORS['blue']}"
        width="2"
    ]

    // ============================================
    // STEP 2: ARCHITECTURE  
    // ============================================
    step2 [
        label="2. Architecture\\nazure-principal-architect"
        fillcolor="{COLORS['orange']}"
        width="2.5"
    ]
    
    // Step 2 optional tools (horizontal row)
    step2a [
        label="2a. Visualize\\ndiagram-generator"
        fillcolor="{COLORS['purple']}"
    ]
    
    step2b [
        label="2b. Estimate\\nAzure Pricing MCP"
        fillcolor="{COLORS['yellow']}"
        fontcolor="#1a1a2e"
    ]
    
    step2c [
        label="2c. Document\\nadr-generator"
        fillcolor="{COLORS['teal']}"
    ]

    // ============================================
    // STEP 3: BICEP PLANNING
    // ============================================
    step3 [
        label="3. Plan Infrastructure\\nbicep-plan"
        fillcolor="{COLORS['green']}"
        width="2.2"
    ]

    // ============================================
    // STEP 4: CODE GENERATION
    // ============================================
    step4 [
        label="4. Generate Code\\nbicep-implement"
        fillcolor="{COLORS['pink']}"
        width="2.2"
    ]
    
    step4a [
        label="4a. Document\\nadr-generator"
        fillcolor="{COLORS['teal']}"
    ]

    // ============================================
    // STEP 5: DEPLOY
    // ============================================
    step5 [
        label="5. Deploy"
        fillcolor="{COLORS['blue']}"
        width="1.8"
    ]

    // ============================================
    // MAIN FLOW (solid arrows)
    // ============================================
    step1 -> step2 [color="{COLORS['blue']}"]
    step2 -> step3 [color="{COLORS['orange']}"]
    step3 -> step4 [color="{COLORS['green']}"]
    step4 -> step5 [color="{COLORS['pink']}"]

    // ============================================
    // OPTIONAL CONNECTIONS (dashed arrows)
    // ============================================
    // Step 2 optional tools
    step2a -> step2 [style="dashed" color="{COLORS['purple']}" dir="back"]
    step2b -> step2 [style="dashed" color="{COLORS['yellow']}" dir="back"]
    step2c -> step2 [style="dashed" color="{COLORS['teal']}" dir="back"]
    
    // Step 4 optional
    step4a -> step4 [style="dashed" color="{COLORS['teal']}" dir="back"]

    // ============================================
    // LAYOUT HINTS - Horizontal layout
    // ============================================
    // Optional tools above their parent steps
    {{ rank=same; step2a; step2b; step2c }}
    {{ rank=same; step4a }}
    
    // Invisible edges for vertical alignment of optionals
    step2a -> step2b -> step2c [style="invis"]
}}
'''
    return dot_content


def create_simple_workflow():
    """Create a compact horizontal workflow for README."""

    dot_content = f'''
digraph SimpleWorkflow {{
    graph [
        bgcolor="{COLORS['dark_bg']}"
        fontcolor="white"
        fontname="Segoe UI, Arial, sans-serif"
        pad="0.4"
        splines="ortho"
        nodesep="0.4"
        ranksep="0.5"
        rankdir="LR"
        dpi="150"
    ]
    
    node [
        fontname="Segoe UI, Arial, sans-serif"
        fontsize="10"
        fontcolor="white"
        style="filled,rounded"
        shape="box"
        penwidth="0"
        margin="0.15,0.1"
    ]
    
    edge [
        color="{COLORS['gray']}"
        penwidth="2"
        arrowsize="0.6"
    ]
    
    // Main workflow
    s1 [label="1. Plan" fillcolor="{COLORS['blue']}"]
    s2 [label="2. Architect" fillcolor="{COLORS['orange']}"]
    s3 [label="3. Plan Infra" fillcolor="{COLORS['green']}"]
    s4 [label="4. Generate" fillcolor="{COLORS['pink']}"]
    s5 [label="5. Deploy" fillcolor="{COLORS['blue']}"]
    
    // Optional
    opt [label="2a-c: Diagrams | Pricing | ADRs" fillcolor="{COLORS['purple']}" fontsize="9"]
    
    // Flow
    s1 -> s2 -> s3 -> s4 -> s5
    
    // Optional connection
    opt -> s2 [style="dashed" color="{COLORS['purple']}" constraint="false"]
}}
'''
    return dot_content


def create_detailed_workflow():
    """Create a detailed widescreen horizontal workflow."""

    dot_content = f'''
digraph DetailedWorkflow {{
    graph [
        bgcolor="{COLORS['dark_bg']}"
        fontcolor="white"
        fontname="Segoe UI, Arial, sans-serif"
        pad="1.0"
        splines="ortho"
        nodesep="0.5"
        ranksep="1.2"
        rankdir="LR"
        dpi="150"
        newrank="true"
    ]
    
    node [
        fontname="Segoe UI, Arial, sans-serif"
        fontsize="11"
        fontcolor="white"
        style="filled,rounded"
        shape="box"
        penwidth="0"
        margin="0.25,0.15"
    ]
    
    edge [
        color="{COLORS['gray']}"
        fontcolor="{COLORS['light_gray']}"
        fontname="Segoe UI, Arial, sans-serif"
        fontsize="9"
        penwidth="2.5"
        arrowsize="0.8"
    ]

    // Step 1
    step1 [
        label="① Plan\\n@plan"
        fillcolor="{COLORS['blue']}"
        width="1.8"
        height="0.6"
    ]

    // Step 2 main
    step2 [
        label="② Architect\\nazure-principal-architect"
        fillcolor="{COLORS['orange']}"
        width="2.5"
        height="0.6"
    ]
    
    // Step 2 optionals in a row
    opt2a [label="Visualize\\ndiagram-generator" fillcolor="{COLORS['purple']}" fontsize="10"]
    opt2b [label="Estimate\\nPricing MCP" fillcolor="{COLORS['yellow']}" fontcolor="#1a1a2e" fontsize="10"]
    opt2c [label="Document\\nadr-generator" fillcolor="{COLORS['teal']}" fontsize="10"]

    // Step 3
    step3 [
        label="③ Plan Infrastructure\\nbicep-plan"
        fillcolor="{COLORS['green']}"
        width="2.2"
        height="0.6"
    ]

    // Step 4
    step4 [
        label="④ Generate Code\\nbicep-implement"
        fillcolor="{COLORS['pink']}"
        width="2.2"
        height="0.6"
    ]
    
    opt4a [label="Document\\nadr-generator" fillcolor="{COLORS['teal']}" fontsize="10"]

    // Step 5
    step5 [
        label="⑤ Deploy"
        fillcolor="{COLORS['blue']}"
        width="1.6"
        height="0.6"
    ]

    // Main flow - thick colored arrows
    step1 -> step2 [color="{COLORS['blue']}" penwidth="3"]
    step2 -> step3 [color="{COLORS['orange']}" penwidth="3"]
    step3 -> step4 [color="{COLORS['green']}" penwidth="3"]
    step4 -> step5 [color="{COLORS['pink']}" penwidth="3"]

    // Optional tools connections - above main flow
    opt2a -> step2 [style="dashed" color="{COLORS['purple']}" arrowhead="none" arrowtail="normal" dir="back"]
    opt2b -> step2 [style="dashed" color="{COLORS['yellow']}" arrowhead="none" arrowtail="normal" dir="back"]
    opt2c -> step2 [style="dashed" color="{COLORS['teal']}" arrowhead="none" arrowtail="normal" dir="back"]
    
    // ADR for step 4
    opt4a -> step4 [style="dashed" color="{COLORS['teal']}" arrowhead="none" arrowtail="normal" dir="back"]

    // Layout for horizontal - optionals stacked vertically
    {{ rank=same; opt2a; opt2b; opt2c }}
    opt2a -> opt2b -> opt2c [style="invis" weight="10"]
}}
'''
    return dot_content


if __name__ == "__main__":
    output_dir = os.path.dirname(__file__)

    # Generate numbered workflow
    print("🎨 Generating numbered workflow diagram...")
    dot = create_workflow_diagram()
    dot_path = os.path.join(output_dir, "workflow_numbered.dot")
    png_path = os.path.join(output_dir, "workflow_numbered.png")
    svg_path = os.path.join(output_dir, "workflow_numbered.svg")

    with open(dot_path, "w") as f:
        f.write(dot)

    subprocess.run(["dot", "-Tpng", "-Gdpi=150",
                   dot_path, "-o", png_path], check=True)
    subprocess.run(["dot", "-Tsvg", dot_path, "-o", svg_path], check=True)
    print(f"✅ {png_path}")
    print(f"✅ {svg_path}")

    # Generate simple horizontal
    print("\n🎨 Generating simple workflow...")
    dot = create_simple_workflow()
    dot_path = os.path.join(output_dir, "workflow_simple_v2.dot")
    png_path = os.path.join(output_dir, "workflow_simple_v2.png")
    svg_path = os.path.join(output_dir, "workflow_simple_v2.svg")

    with open(dot_path, "w") as f:
        f.write(dot)

    subprocess.run(["dot", "-Tpng", "-Gdpi=150",
                   dot_path, "-o", png_path], check=True)
    subprocess.run(["dot", "-Tsvg", dot_path, "-o", svg_path], check=True)
    print(f"✅ {png_path}")
    print(f"✅ {svg_path}")

    # Generate detailed workflow
    print("\n🎨 Generating detailed workflow...")
    dot = create_detailed_workflow()
    dot_path = os.path.join(output_dir, "workflow_detailed.dot")
    png_path = os.path.join(output_dir, "workflow_detailed.png")
    svg_path = os.path.join(output_dir, "workflow_detailed.svg")

    with open(dot_path, "w") as f:
        f.write(dot)

    subprocess.run(["dot", "-Tpng", "-Gdpi=150",
                   dot_path, "-o", png_path], check=True)
    subprocess.run(["dot", "-Tsvg", dot_path, "-o", svg_path], check=True)
    print(f"✅ {png_path}")
    print(f"✅ {svg_path}")

    print("\n🎉 All diagrams generated!")
    print(f"\nFiles in: {output_dir}")
