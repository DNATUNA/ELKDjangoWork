# -*- coding: utf-8 -*-
# !/usr/bin/python
# ------------------------------------------------------------------------------------
# 1.Program Name
#   로그 관리
# 2. Input
#    configuration file : config.json
# 3. Target
#    /log/지정된로그.log
#  ------------------------------------------------------------------------------------
# 4. Program History
#     2018. 노홍균 개발
# ------------------------------------------------------------------------------------
import logging.handlers
from aims.aims_utils import global_config
import os

# DaRA Config 불러오기
config_common = global_config.config_common                                  #global config 의 COMMON 부분 가져오기

# 로그 레벨은 Debug > Info > Warning > Error > Critical
# logger 인스턴스 생성 및 로그 레벨 생성
logger = logging.getLogger("AIMS logger")

if config_common['DEBUG_LEVEL'].upper() == "DEBUG":
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] [%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
elif config_common['DEBUG_LEVEL'].upper() == "WARNING":
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('[%(levelname)s] [%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
elif config_common['DEBUG_LEVEL'].upper() == "ERROR":
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter('[%(levelname)s] [%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
elif config_common['DEBUG_LEVEL'].upper() == "CRITICAL":
    logger.setLevel(logging.CRITICAL)
else:
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s > %(message)s')

# fileHandler 와 StreamHandler 생성
logdir = config_common['HOME_DIR'].rstrip("/") + '/' + 'log'
logfile = config_common['HOME_DIR'].rstrip("/") + '/' + 'log'  + '/' +  'aims.log'

## 로그 디렉토리 확인 및 생성
if not os.path.exists(logdir):
    os.makedirs(logdir)

# fileHandler = logging.FileHandler(logfile)
file_max_bytes = 20 * 1024 * 1024 # 20MB
fileHandler = logging.handlers.RotatingFileHandler(filename=logfile, maxBytes=file_max_bytes, backupCount= 10, encoding='utf-8')
streamHandler = logging.StreamHandler()

# 각 핸들러에 포매터를 지정한다.
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

# Handler를 logging 에 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

# logging
# 다음과 같은형태로 사용
# logger.debug("DEBUG")
# logger.info("INFO")
# logger.warning("WARNING")
# logger.error("ERROR")
# logger.critical("CRITICAL")
#