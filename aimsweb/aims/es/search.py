from elasticsearch_dsl import Search, MultiSearch
from elasticsearch import Elasticsearch

# 공통 환경 불러오기 - NHK
from aims.aims_utils.global_config import config
from aims.aims_utils.logger import logger
from aims.aims_utils.AimsData import AimsData


class Getdata():
    es = Elasticsearch(hosts='http://124.49.54.38:19200/')
    search = Search(using=es, index='test-2018.09.11').params(request_timeout=30)
    multi = MultiSearch(using=es, index='test-2018.09.11').params(request_timeout=30)
    res = search.execute()

    total = search.count()