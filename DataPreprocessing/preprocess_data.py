class PreprocessData:
    def __init__(self, os, json, pd, ResourceManager):
        print("[DataPreprocessing] Data preprocessing activated")

        # Initialize ResourceManager
        self.resource_manager = ResourceManager()

        # Load config
        self.config = self.resource_manager.get_config()

        # Load sample dataset
        self.df = self.resource_manager.get_sample_data()
        print(f"[DataPreprocessing] Loaded dataset with {len(self.df)} rows")

        # Prepare folder for saving preprocessed data
        self.output_path = self.config.get("preprocessed_data_path", "output/preprocessed")
        os.makedirs(self.output_path, exist_ok=True)

        self.run_preprocessing()

    def run_preprocessing(self):
        print("[DataPreprocessing] Running dummy preprocessing")
        # Here you could add data cleaning, feature engineering, etc.
