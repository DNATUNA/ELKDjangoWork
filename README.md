# ELKDjangoWork

## 소개

AIMS에서 외주하면서 만든 결과물들입니다. 개발 기간은 총 5개월 반이었고, Django와 ELK에 대한 지식이 전혀 없던 상태여서 많이 미숙합니다. 실제 서비스를 올린 것은 아니며 제가 기능 개발하면서 정리한 내용들과 간단한 검색 기능이 있는 Django Back-end입니다.

## 개발 환경

- 서버 2대 : Beats와 ELK 서버 1대, Django 서버 1대
- Ubuntu 16.04(LTS)
- ELK : docker
- File Beat : local에 설치
- Django : local에 설치

## File beat와 ELK 세팅 및 이슈 해결 방법

- 세팅과 이슈 해결법의 자세한 내용들은 ELKDjangoWork/aimsweb/FELK 경로에 따로따로 분류하여 정리했습니다.
- 각각 이슈의 번호까지 작성해두진 않았습니다.
- File Beat는 우분투에 직접 설치했고, ELK는 docker로 실행했습니다.
- File Beat는 로컬에 있는 .log 파일을 logstash로 보냅니다. logstash는 파이프 라인을 통해 데이터를 분류하고 분류한 데이터를 Elastic으로 보냅니다.
- 키바나는 그래프를 따로 설정하진 않았고 데이터가 들어와서 분류가 잘 되었는지 확인하는 용으로 밖에 사용해보지 못했습니다.

## Django 세팅

- elasticsearch, django-elasticsearch-dsl 패키지를 사용합니다.