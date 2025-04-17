import os

# Define the project structure
project_structure = {
    "Power_BI_Library": {
        "README.md": "# Power BI Library\n\nInitial placeholder for the README.",
        "LICENSE": "",  # Add your license text here
        "CONTRIBUTING.md": "# Contribution Guidelines\n\nInitial placeholder for contributing guidelines.",
        "docs": {},
        "techniques": {
            "README.md": "# Techniques\n\nOverview of techniques.",
            "technique_1": {
                "overview.md": "# Technique 1\n\nDescription of this technique.",
                "examples": {},
                "assets": {}
            }
        },
        "artifacts": {
            "README.md": "# Artifacts\n\nOverview of artifacts.",
            "dax_formulas": {
                "formula_1.dax": "// Example DAX formula."
            },
            "data_models": {
                "model_1.pbix": ""  # Placeholder for a Power BI Desktop file
            }
        },
        "components": {
            "README.md": "# Components\n\nOverview of components.",
            "widget_1": {
                "widget.pbiviz": "",  # Placeholder for a Power BI custom visual file
                "documentation.md": "# Documentation\n\nInstructions for using this widget.",
                "assets": {}
            }
        },
        "widgets": {
            "README.md": "# Widgets\n\nOverview of widgets.",
            "widget_1": {
                "overview.md": "# Widget 1\n\nDescription of this widget.",
                "examples": {},
                "assets": {}
            }
        },
        ".gitignore": """# Ignore unnecessary files
*.tmp
*.cache
*.pbix.lock

# Python virtual environment
.venv/
__pycache__/
*.py[cod]
*$py.class
"""
    }
}

# Function to create files and folders
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Create file
            with open(path, "w") as f:
                f.write(content)

# Create the project structure
base_path = os.getcwd()  # Current directory
create_structure(base_path, project_structure)

print(f"Project structure created in {base_path}")