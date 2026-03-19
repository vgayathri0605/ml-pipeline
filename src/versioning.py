import os
import joblib
from datetime import datetime

def save_model(model, path):
    # create models folder if not exists
    os.makedirs(path, exist_ok=True)

    # create version using timestamp
    version = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"model_{version}.pkl"
    full_path = os.path.join(path, filename)

    # save model
    joblib.dump(model, full_path)

    return full_path