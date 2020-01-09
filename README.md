# django-sdh-test

1) папка weather. файл csv я переименовал в weather. запускается python3 weather.py . использован pandas
2) проект Django в папке sdh_test
использовал virtualenv, установленные пакеты - в requrements.txt
БД - дефолтная sqlite


virtualenv -p python3 .env
source .env/bin/activate
pip install -r sdh_test/requirements.txt
make migrations
make run