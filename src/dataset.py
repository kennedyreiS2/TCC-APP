from roboflow import Roboflow
from dotenv import load_dotenv
import os

load_dotenv()

def download_dataset() -> None:
    api_key = os.environ.get('ROBOFLOW_API_KEY')
    workspace = os.environ.get('ROBOFLOW_WORKSPACE')
    project = os.environ.get('ROBOFLOW_PROJECT')

    rf = Roboflow(api_key=api_key)
    project = rf.workspace(workspace).project(project)
    dataset = project.version(1).download("folder")

if __name__ == "__main__":
    download_dataset()
