<<<<<<< HEAD
#!bin/bash
​clear
printf​ ​"​当前环境:​"
pwd
sleep 3s
printf​ ​"​正在更新容器的apt...​"
apt update -y ​&&​ apt upgrade -y
printf​ ​"​正在安装相应软件...​"
apt install git python3 python3-pip nano -y
printf​ ​"​正在获取仓库...​"
git clone https://gitlab.com/Xtao-Labs/pagermaid-modify.git pgm ​&&​ ​cd​ pgm
printf​ ​"​正在安装pgm的软件包...​"
apt install imagemagick -y
apt install libzbar-dev -y
apt install tesseract-ocr tesseract-ocr-all -y
apt install redis-server -y
printf​ ​"​正在安装pgm的依赖...​"
pip3 install -r requirements.txt
clear
printf​ ​"​三秒后将编辑配置文件，请填入相应的api_key和api_hash​"
cp config.gen.yml config.yml
sleep 3s
nano config.yml
printf​ ​"​正在启动pgm...​"
python3 -m pagermaid
=======
clear

printf "当前环境:"
pwd

sleep 3s

printf "正在更新容器的apt..."
apt update -y && apt upgrade -y

printf "正在安装相应软件..."
apt install git python3 python3-pip nano -y

printf "正在获取仓库..."
git clone https://gitlab.com/Xtao-Labs/pagermaid-modify.git pgm && cd pgm

printf "正在安装pgm的软件包..."
apt install imagemagick -y
apt install libzbar-dev -y
apt install tesseract-ocr tesseract-ocr-all -y
apt install redis-server -y

printf "正在安装pgm的依赖..."
pip3 install -r requirements.txt

clear

printf "三秒后将编辑配置文件，请填入相应的api_key和api_hash"
cp config.gen.yml config.yml

sleep 3s

nano config.yml

printf "正在启动pgm..."
python3 -m pagermaid
>>>>>>> 1f7a3e6 (添加了after)
