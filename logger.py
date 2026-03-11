import logging
import datetime
import time



logging.basicConfig(level = logging.INFO, 
                    format = "%(asctime)s - [%(levelname)s] - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    handlers=[
                        logging.FileHandler("scheduler.log"),
                        logging.StreamHandler()
                    ])


logger_object = logging.getLogger("TaskScheduler") 