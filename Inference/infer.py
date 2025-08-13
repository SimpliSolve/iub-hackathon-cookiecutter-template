class Infer:
    def __init__(self, output_handler, os, datetime, ResourceManager):
        self.output_handler = output_handler
        self.os = os
        self.datetime = datetime

        # Initialize ResourceManager
        self.resource_manager = ResourceManager()
        print("[Inference] Inference activated")

    def run(self):
        print("[Inference] Running dummy inference")

        # Simulated predictions
        predictions = [
            {"id": 1, "label": "Class_A", "score": 0.92},
            {"id": 2, "label": "Class_B", "score": 0.81}
        ]

        # Save report via OutputHandler
        self.output_handler.save_report(predictions)
