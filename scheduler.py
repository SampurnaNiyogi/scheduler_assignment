from logger import logger_object
from datetime import datetime

#HeartBeat Job : Check if system is alive
def heartbeat_job():
    curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger_object.info(f"[HEARTBEAT] Task ran at: {curr_time}")

#Reminder Job : Periodic reminder
def reminder_job():
    curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger_object.info(f"[REMINDER] Reminder triggered at: {curr_time}")

#Startup Task(actual function for once executed) 
def startup_job():
    curr_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger_object.info(f"[STARTUP] One-time setup task completed at: {curr_time}")