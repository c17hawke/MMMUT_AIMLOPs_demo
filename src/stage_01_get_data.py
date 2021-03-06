import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import random
from urllib import request


STAGE = "Get data" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def download_data(config):
    URL = config["source_url"]
    RAW_DATA_DIR = config['artifacts']["RAW_DATA_DIR"]
    create_directories([RAW_DATA_DIR])
    RAW_DATA_FILPATH = config['artifacts']["RAW_DATA_FILEPATH"]
    request.urlretrieve(URL, RAW_DATA_FILPATH)

def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    download_data(config)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e