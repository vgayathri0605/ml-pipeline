import yaml
from src.s3_utils import download_latest_file
from src.ingest import load_latest_file
from src.preprocess import preprocess_data
from src.train import train_model
from src.versioning import save_model
from src.logger import setup_logger

def run_pipeline():
    print("Pipeline started")   

def run_pipeline():
    # load config
    config = yaml.safe_load(open("config/config.yaml"))

    # setup logger
    logger = setup_logger(config["logging"]["log_file"])

    try:
        logger.info("Pipeline started")

        # ingestion
        df, filename = load_latest_file(config["data"]["input_path"])
        logger.info(f"Loaded file: {filename}")

        # preprocessing
        X, y = preprocess_data(df)
        logger.info("Data preprocessed")

        # training
        model = train_model(X, y)
        logger.info("Model trained")

        # versioning
        model_path = save_model(model, config["model"]["save_path"])
        logger.info(f"Model saved at {model_path}")

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")