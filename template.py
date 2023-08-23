import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "LemonClassifier"

fiels=[
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
    "research/trials.ipynb"

]

for path in fiels:
    path=Path(path)
    filedir, filename = os.path.split(path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(path) or os.path.getsize(path)==0):
        with open (path,"w") as f:
            pass
    else:
        logging.info(f"{filename} alerady existed")