import os

def create_project_structure():
    # Create a professional directory structure for data science work
    directories = [
        'data/raw',           # Original soccer match data goes here
        'data/processed',     # Cleaned and transformed data
        'notebooks',          # Your Jupyter analysis notebooks
        'src/data_preprocessing',  # Scripts for cleaning data
        'src/feature_engineering', # Code for creating prediction features
        'src/model',              # Your prediction models
        'reports/figures'         # Visualizations and results
    ]
    
    # Create each directory and track empty ones with .gitkeep
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, '.gitkeep'), 'a') as f:
            pass
            
    print("✓ Created directory structure")

    # Create starter files with initial documentation
    files = {
        'requirements.txt': '',  # Will list your project's dependencies
        'reports/final_report.md': '# Soccer Match Prediction Analysis\n\n[Report content will be added as the project progresses]',
        '.gitignore': '''venv/
__pycache__/
.DS_Store
.ipynb_checkpoints/
'''  # Tell Git which files to ignore
    }
    
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)
    
    print("✓ Created initial files")

if __name__ == "__main__":
    create_project_structure()