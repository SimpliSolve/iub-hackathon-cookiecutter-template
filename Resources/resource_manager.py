import os
import json
import pandas as pd

class ResourceManager:
    def __init__(self, resources_dir="Resources"):
        self.resources_dir = os.path.abspath(resources_dir)
        print(f"[Resources] Resource manager activated at {self.resources_dir}")

    def get_model_path(self, filename="dummy_model.pth"):
        path = os.path.join(self.resources_dir, filename)
        print(f"[Resources] Model path: {path}")
        return path

    def get_config(self, filename="default_config.json"):
        path = os.path.join(self.resources_dir, filename)
        print(f"[Resources] Loading config from: {path}")
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def get_sample_data(self, filename="sample_data.csv"):
        path = os.path.join(self.resources_dir, filename)
        print(f"[Resources] Loading sample data from: {path}")
        if os.path.exists(path):
            return pd.read_csv(path)
        return pd.DataFrame()
