
import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s'
)

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    # Create parent directories only if they don't exist
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Create file only if it doesn't already exist
    if not filepath.exists():

        filepath.touch()
        logging.info(f"Created new file: {filepath}")

    else:
        logging.info(f"Already exists, skipping: {filepath}")

logging.info("Project structure creation completed successfully!")
