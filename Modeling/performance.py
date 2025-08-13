class Performance:
    def __init__(self):
        print("[Performance] Evaluation activated")

        config_path = os.path.join(os.getcwd(), 'output', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {}

    def evaluate(self):
        print("[Performance] Running dummy performance evaluation")