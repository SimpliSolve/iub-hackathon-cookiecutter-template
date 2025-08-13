##################### Initialization of pipeline starts #####################
#-----------------------------general imports-------------------------------#
import os
import json
import time
from datetime import datetime

#--------------------------custom library imports---------------------------#
from DataPreprocessing.preprocess_data import PreprocessData
from Modeling.build_model import BuildModel
from Modeling.performance import Performance
from Inference.infer import Infer
from Utilities.output_handler import OutputHandler
from Resources.resource_manager import ResourceManager

###################### Initialization of pipeline ends ######################

##################### Pipeline execution flow starts ########################
#############################################################################
#------------------------------time tracking--------------------------------#
def track_step(step_name, func):
    """Helper to time and track each step."""
    print(f"--- {step_name} START ---")
    start = time.time()
    func()
    elapsed = time.time() - start
    print(f"--- {step_name} END | Elapsed: {elapsed:.2f} sec ---\n")

#------------------------------time tracking--------------------------------#

if __name__ == "__main__":
    pipeline_start = time.time()
    print("===== Competition Pipeline Started =====\n")

    output_handler = OutputHandler()

    track_step("Data Preprocessing", lambda: PreprocessData())
    track_step("Model Building", lambda: BuildModel())
    track_step("Performance Evaluation", lambda: Performance().evaluate())
    track_step("Inference", lambda: Infer(output_handler).run())

    print("===== Pipeline Finished Successfully =====")
    print(f"Total Execution Time: {time.time() - pipeline_start:.2f} seconds")
###################### Pipeline execution flow ends #########################
