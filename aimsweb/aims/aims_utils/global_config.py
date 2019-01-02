# -*- coding: utf-8 -*-
# !/usr/bin/python
# ------------------------------------------------------------------------------------
# 1.Program Name
# config

import os
import inspect
import json

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
print(current_dir)
# config 설정 불러오기
config_path = "D:/dev/aimsweb/aims/config"
config_file = "aims_config.json"
aims_config_file_full = config_path + '/' + config_file
# print(current_dir)
# 환경설정은 smart_dara_config.json 설정파일에 미리 설정된 타입으로 지정함. 운영으로 넘어갈때에도 이 셋팅을 이용

if os.path.isfile(aims_config_file_full) and os.access(aims_config_file_full, os.R_OK):
    with open(aims_config_file_full) as json_data_file:
        try:
            config = json.load(json_data_file)
            config_common = config['COMMON']
            config_aims_runtype = config['RUN_TYPE']
            config = config[config_aims_runtype]
            if config_common['DEBUG_LEVEL'].upper() == "DEBUG":
                print("[DEBUG] aims configuration file is loading : " + aims_config_file_full)
                print("[DEBUG] RUN TYPE: " + config_aims_runtype)
        except json.JSONDecodeError:
            print('[Error] Decoding JSON has failed :' + repr(json_data_file))
            # print(sys.exc_info())
            # sys.exit(1)
else:
    print("[Error] AIMS configuration file is missing or is not readable : " + aims_config_file_full)
    # sys.exit(1)
