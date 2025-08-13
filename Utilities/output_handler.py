class OutputHandler:
    def __init__(self, os, datetime, output_dir="output", docs_dir="documentation"):
        self.os = os
        self.datetime = datetime
        self.output_dir = self.os.path.abspath(output_dir)
        self.docs_dir = self.os.path.abspath(docs_dir)
        self.os.makedirs(self.output_dir, exist_ok=True)
        self.os.makedirs(self.docs_dir, exist_ok=True)
        print("[OutputHandler] Ready to save outputs.")

    def save_report(self, predictions, filename_prefix="competition_report"):
        """Saves a simple text report to documentation/"""
        timestamp = self.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_path = self.os.path.join(self.docs_dir, f"{filename_prefix}_{timestamp}.txt")

        with open(report_path, "w") as f:
            f.write("=== Competition Inference Report ===\n")
            f.write(f"Generated on: {self.datetime.now()}\n\n")
            for pred in predictions:
                f.write(f"ID: {pred['id']}, Label: {pred['label']}, Score: {pred['score']:.2f}\n")
            f.write("\n--- End of Report ---\n")

        print(f"[OutputHandler] Report saved at: {report_path}")
        return report_path

    def save_metrics(self, metrics_dict, filename_prefix="metrics"):
        """Saves model performance metrics as a text file in output/"""
        timestamp = self.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        metrics_path = self.os.path.join(self.output_dir, f"{filename_prefix}_{timestamp}.txt")

        with open(metrics_path, "w") as f:
            f.write("=== Model Performance Metrics ===\n")
            f.write(f"Generated on: {self.datetime.now()}\n\n")
            for key, value in metrics_dict.items():
                f.write(f"{key}: {value}\n")
            f.write("\n--- End of Metrics ---\n")

        print(f"[OutputHandler] Metrics saved at: {metrics_path}")
        return metrics_path
