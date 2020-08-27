import logging
import os.path
import time
from os.path import abspath, dirname


class LogDao:
    staticmethod

    def saveLog(file_name, msg):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        date = time.strftime("%Y%m%d", time.localtime())
        current_dir = abspath(dirname(__file__))
        print(current_dir)
        if not os.path.exists(current_dir + "/" + date):
            os.makedirs(current_dir + "/" + date)
        log_path = current_dir + "/" + date + "/" + file_name + ".log"
        if not os.path.exists(log_path):
            fd = open(log_path, mode="w", encoding="utf-8")
            fd.close()
        fh = logging.FileHandler(log_path, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logging.info(msg)

