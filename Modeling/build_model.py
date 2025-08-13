class BuildModel:
    def __init__(self, os, ResourceManager):
        print("[Modeling] Model building activated")

        # Initialize ResourceManager
        self.resource_manager = ResourceManager()

        # Load config and model path
        self.config = self.resource_manager.get_config()
        self.model_path = self.resource_manager.get_model_path()
        print(f"[Modeling] Using model weights at: {self.model_path}")

        self.run_build()

    def run_build(self):
        print("[Modeling] Building dummy model with parameters:")
        print(self.config.get("model_params", {"layers": 0, "hidden_size": 0}))
        print("[Modeling] Dummy model build complete")
