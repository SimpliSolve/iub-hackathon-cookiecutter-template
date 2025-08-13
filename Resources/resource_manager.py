class ResourceManager:
    def __init__(self, os, json, pd, resources_dir="Resources"):
        self.os = os
        self.json = json
        self.pd = pd
        self.resources_dir = self.os.path.abspath(resources_dir)
        print(f"[Resources] Resource manager activated at {self.resources_dir}")

    def get_model_path(self, filename="dummy_model.pth"):
        path = self.os.path.join(self.resources_dir, filename)
        print(f"[Resources] Model path: {path}")
        return path

    def get_config(self, filename="default_config.json"):
        path = self.os.path.join(self.resources_dir, filename)
        print(f"[Resources] Loading config from: {path}")
        if self.os.path.exists(path):
            with open(path, "r") as f:
                return self.json.load(f)
        return {}

    def get_sample_data(self, filename="sample_data.csv"):
        path = self.os.path.join(self.resources_dir, filename)
        print(f"[Resources] Loading sample data from: {path}")
        if self.os.path.exists(path):
            return self.pd.read_csv(path)
        return self.pd.DataFrame([{"id": 1, "feature": 0}, {"id": 2, "feature": 1}])
