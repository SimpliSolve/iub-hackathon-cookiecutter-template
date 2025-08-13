class Performance:
    def __init__(self, os, json):
        self.os = os
        self.json = json
        print("[Performance] Evaluation activated")

        config_path = self.os.path.join(self.os.getcwd(), 'output', 'config.json')
        if self.os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = self.json.load(f)
        else:
            self.config = {}

    def evaluate(self):
        print("[Performance] Running dummy performance evaluation")
