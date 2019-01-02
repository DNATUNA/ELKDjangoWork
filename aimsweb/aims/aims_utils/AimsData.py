# -*- coding: utf-8 -*-
# !/usr/bin/python
# ------------------------------------------------------------------------------------
# 1.Program Name
#   IN/OUT, 파일 핸들링을 하는 클래스
# ------------------------------------------------------------------------------------
#     2018.11. 노홍균
# ------------------------------------------------------------------------------------
import time
import sys, os
import pandas as pd
import numpy as np
from sys import platform
import re
import csv
from aims.aims_utils.global_config import config
from aims.aims_utils.logger import logger
import moment
from unipath import Path
import glob
import json
import ast


class AimsData:

    def __init__(self, aimsId, hostId, app_id):
        self.dataPath = config['AIMS_SETTING']['DATA_ROOT']  # 데이터 저장 Root
        self.aimsId = aimsId
        self.app_id = app_id
        self.hostId = hostId
        self.encoding = "utf-8"
        self.date_format = '%Y%m%d'
        self.float_format = '%.3f'
        self.date_today = moment.now().format("YYYY-M-D")
        self.platform = platform
        return

    def set_data_dir(self):
        # 201811 초기셋팅
        # DATA ROOT (Level 1)
        data_root = Path(self.dataPath)
        data_root.mkdir()

        # DATA IN/OUT/TMP (Level 2)
        data_input_path = Path(data_root.rstrip("/") + "/" + "INPUT")
        data_input_path.mkdir()
        data_output_path = Path(data_root.rstrip("/") + "/" + "OUTPUT")
        data_output_path.mkdir()
        data_tmp_path = Path(data_root.rstrip("/") + "/" + "TMP")
        data_tmp_path.mkdir()

        # DATA (INPUT) Equv ID
        data_input_eid_path = Path(data_input_path.rstrip("/") + "/" + self.app_id.upper())
        data_input_eid_path.mkdir()
        data_input_rid_path = Path(data_input_eid_path.rstrip("/") + "/" + self.aimsId.upper())
        data_input_rid_path.mkdir()
        data_input_lid_path = Path(data_input_rid_path.rstrip("/") + "/" + self.hostId.upper())
        data_input_lid_path.mkdir()

        # DATA (INPUT) CSV, JSON, IMAGE, VIDEO (Level 3)
        data_input_csv_path = Path(data_input_lid_path.rstrip("/") + "/" + "CSV")
        data_input_csv_path.mkdir()
        data_input_json_path = Path(data_input_lid_path.rstrip("/") + "/" + "JSON")
        data_input_json_path.mkdir()
        data_input_image_path = Path(data_input_lid_path.rstrip("/") + "/" + "IMAGE")
        data_input_image_path.mkdir()
        data_input_video_path = Path(data_input_lid_path.rstrip("/") + "/" + "VIDEO")
        data_input_video_path.mkdir()

        # DATA (tmp) Equv ID
        data_tmp_eid_path = Path(data_tmp_path.rstrip("/") + "/" + self.app_id.upper())
        data_tmp_eid_path.mkdir()
        data_tmp_rid_path = Path(data_tmp_eid_path.rstrip("/") + "/" + self.aimsId.upper())
        data_tmp_rid_path.mkdir()
        data_tmp_lid_path = Path(data_tmp_rid_path.rstrip("/") + "/" + self.hostId.upper())
        data_tmp_lid_path.mkdir()

        # DATA (tmp) CSV, JSON, IMAGE, VIDEO (Level 3)
        data_tmp_csv_path = Path(data_tmp_lid_path.rstrip("/") + "/" + "CSV")
        data_tmp_csv_path.mkdir()
        data_tmp_json_path = Path(data_tmp_lid_path.rstrip("/") + "/" + "JSON")
        data_tmp_json_path.mkdir()
        data_tmp_image_path = Path(data_tmp_lid_path.rstrip("/") + "/" + "IMAGE")
        data_tmp_image_path.mkdir()

        data_tmp_imagecrp_path = Path(data_tmp_image_path.rstrip("/") + "/" + "CROP")
        data_tmp_imagecrp_path.mkdir()
        # logger.debug("CROP dir :{}".format(data_tmp_imagecrp_path))

        data_tmp_imageinten_path = Path(data_tmp_image_path.rstrip("/") + "/" + "ITENSITY")
        data_tmp_imageinten_path.mkdir()
        # logger.debug("Intensity dir :{}".format(data_tmp_imageinten_path))

        data_tmp_video_path = Path(data_tmp_lid_path.rstrip("/") + "/" + "VIDEO")
        data_tmp_video_path.mkdir()

        # DATA (output) Equv ID
        data_output_eid_path = Path(data_output_path.rstrip("/") + "/" + self.app_id.upper())
        data_output_eid_path.mkdir()
        data_output_rid_path = Path(data_output_eid_path.rstrip("/") + "/" + self.aimsId.upper())
        data_output_rid_path.mkdir()
        data_output_lid_path = Path(data_output_rid_path.rstrip("/") + "/" + self.hostId.upper())
        data_output_lid_path.mkdir()

        # DATA (output) CSV, JSON, IMAGE, VIDEO (Level 3)
        data_output_csv_path = Path(data_output_lid_path.rstrip("/") + "/" + "CSV")
        data_output_csv_path.mkdir()
        data_output_json_path = Path(data_output_lid_path.rstrip("/") + "/" + "JSON")
        data_output_json_path.mkdir()
        data_output_image_path = Path(data_output_lid_path.rstrip("/") + "/" + "IMAGE")
        data_output_image_path.mkdir()

        data_output_video_path = Path(data_output_lid_path.rstrip("/") + "/" + "VIDEO")
        data_output_video_path.mkdir()

        data_out_videointen_path = Path(data_output_video_path.rstrip("/") + "/" + "ITENSITY")
        data_out_videointen_path.mkdir()

        data = {
            "DATA_NAME": ["INPUT_CSV_PATH", "INPUT_JSON_PATH", "INPUT_IMAGE_PATH", "INPUT_VIDEO_PATH",
                          "OUTPUT_CSV_PATH", "OUTPUT_JSON_PATH", "OUTPUT_IMAGE_PATH",
                          "OUTPUT_VIDEO_PATH",
                          "TMP_CSV_PATH", "TMP_JSON_PATH", "TMP_IMAGE_PATH", "TMP_VIDEO_PATH", "TMP_IMAGE_CROP_PATH",
                          "TMP_IMAGE_INTEN_PATH", "OUTPUT_VIDEO_INTEN_PATH"
                          ],
            "DATA_PATH": [data_input_csv_path, data_input_json_path, data_input_image_path,
                          data_input_video_path,
                          data_output_csv_path, data_output_json_path,
                          data_output_image_path, data_output_video_path,
                          data_tmp_csv_path, data_tmp_json_path, data_tmp_image_path,
                          data_tmp_video_path, data_tmp_imagecrp_path, data_tmp_imageinten_path,
                          data_out_videointen_path
                          ],
            "USE_YN": ["Y", "Y", "Y", "Y",
                       "Y", "Y", "Y", "Y",
                       "Y", "Y", "Y", "Y", "Y", "Y", "Y"
                       ]}
        self.df_datafile = pd.DataFrame(data, columns=["DATA_NAME", "DATA_PATH", "USE_YN"])

        #
        return self.df_datafile

    def get_data_path(self, data_name):
        df1 = self.df_datafile[(self.df_datafile["DATA_NAME"] == data_name) & (self.df_datafile["USE_YN"] == "Y")]
        v1 = df1.loc(axis=1)['DATA_PATH'].astype(str).values
        v2 = "".join(v1)
        return v2

    def get_runid(self):
        return self.aimsId.upper()

    def get_layerid(self):
        return self.hostId.upper()

    def get_jpg_file_list(self, path):
        image_jpg_list = Path(path).listdir(pattern="*.jpg")
        image_jpg_list.sort()
        return image_jpg_list

    def write_pd_csv(self, df):
        # 수정예정
        write_result = df.to_csv(self.output_imgfile_full, encoding=self.encoding, date_format=self.date_format,
                                 float_format=self.float_format)
        return write_result

    def export_inferenced_video(self):
        # 셋팅 예정
        return

    def export_inferenced_ptn_csv(self):
        # 셋팅 예정
        return

    def cleanup_dir(self, clearn_dir):
        path = clearn_dir.rstrip("/") + "/"
        logger.warning("Cleaning up : {}".format(path))
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError:
                logger.error("can not make directory : {}".format(path))
                pass
        filelist = glob.glob(path + '*')
        for file in filelist:
            os.remove(file)


class AimsCsv:
    count = 0

    def __init__(self, filepath, filename, file_ext):
        self.filepath = filepath.rstrip("/")
        self.filename = filename
        self.file_ext = file_ext
        self.file_name_full = self.filepath + "/" + self.filename + "." + self.file_ext
        self.date_today = moment.now().format("YYYYMD")
        p = Path(self.filepath, self.file_name_full)

    def write_cvs_file(self, df, output_filename_full):
        write_result = df.to_csv(output_filename_full, encoding=self.encoding, date_format=self.date_format,
                                 float_format=self.float_format)
        return write_result

    def load_csv_file(self, input_csv_filename_full):
        df_input_file = pd.read_csv(input_csv_filename_full, encoding=self.encoding)
        return df_input_file


    def write_json_d3_from_df(self, target_bright_json_full, slice_step=10):
        df_brgt = self.df_hist[['FRAME_NUM','BRIGHT_FRAME']]
        values_data = df_brgt.values[1:len(df_brgt):slice_step].tolist()

        def obj_dict(obj):
            return obj.__dict__

        fig = [
            {
                "key": "brightness",
                "values": values_data
            }
        ]

        json_string = json.dumps(fig, default=obj_dict)
        json_string = json_string.replace('"', '\'').replace('"[', '[').replace(']"', ']')
        json_string = json_string.replace("'", '"')
        json_string = ast.literal_eval(json_string)


#
# print(config)
# p = AimsData("D:/DATA_HOME_TEST", "rid001", "layer01", "mbe003")
# # 설정 PATH 들이 DF 형태로 리턴됨
# df_dataset_path = p.set_data_dir()
# # 다음과 같이  get_data_path 도 가능
# p.get_data_path("INPUT_CSV_PATH")


class Filename:
    count = 0

    def __init__(self, filepath, filename, file_ext):
        self.filepath = filepath.rstrip("/")
        self.filename = filename
        self.file_ext = file_ext
        self.file_name_full = self.filepath + "/" + self.filename + "." + self.file_ext
        self.date_today = moment.now().format("YYYYMD")
        p = Path(self.filepath, self.file_name_full)

    def set_output_format(self, prefix1, prefix2, postfix1, postfix2, timestamp_yn=False, separator="_"):
        if (prefix1 != ""):
            part1 = prefix1 + separator
        else:
            part1 = ""

        if (prefix2 != ""):
            part2 = prefix2 + separator
        else:
            part2 = ""

        if (postfix1 != ""):
            part3 = postfix1 + separator
        else:
            part3 = ""

        if (postfix2 != ""):
            part4 = postfix2 + separator
        else:
            part4 = ""

        if (timestamp_yn):
            self.formatted_filename = part1 + part2 + self.filename + part3 + part4 + self.date_today + "." + self.file_ext
        else:
            self.formatted_filename = part1 + part2 + self.filename + part3 + part4 + "." + self.file_ext

        self.formatted_filename_full = self.filepath + "/" + self.formatted_filename
        return self.formatted_filename_full

    def rename_filename_format(self, prefix1, prefix2, filename, postfix1, postfix2, file_ext, timestamp_yn=False,
                               separator="_"):

        if (prefix1 != ""):
            part1 = prefix1 + separator
        else:
            part1 = ""

        if (prefix2 != ""):
            part2 = prefix2 + separator
            logger.debug(part2)
        else:
            part2 = ""

        if (filename != ""):
            p = Path(filename)
            filename_only = p.stem + separator
            filepath = p.parent
        else:
            filename_only = ""

        if (postfix1 != ""):
            part3 = + separator + postfix1
            logger.debug(part3)
        else:
            part3 = ""

        if (postfix2 != ""):
            part4 = separator + postfix2
        else:
            part4 = ""

        if (timestamp_yn):
            formatted_filename = part1 + part2 + filename_only + part3 + part4 + separator + self.date_today + "." + file_ext
        else:
            formatted_filename = part1 + part2 + filename_only + part3 + part4 + "." + file_ext

        rename_formatted_filename = formatted_filename
        return rename_formatted_filename.replace(separator + separator, separator)
