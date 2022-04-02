#!/bin/bash

welcome="这是pgm在Termux上安装的一键shell脚本(注意:此脚本缺自定义度)"

printf $welcome
printf "\n你将有三秒钟的时间考虑是否要进行安装(取消请按Ctrl C)\n"

sleep 3s
clear

printf "正在更新Termux的pkg..."

pkg update -y && pkg upgrade -y

printf "正在安装相应软件并获取容器文件..."

pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh

printf "正在进入容器..."
./start-ubuntu.sh

clear

printf "当前环境:"
pwd

sleep 3s

printf "正在更新容器的apt..."
apt-get update -y && apt-get upgrade -y

printf "正在安装相应软件..."
apt install git python3 python3-pip nano -y

printf "正在获取仓库..."
git clone https://gitlab.com/Xtao-Labs/pagermaid-modify.git pgm && cd pgm

printf "正在安装pgm的软件包..."
apt-get install imagemagick -y
apt-get install libzbar-dev -y
apt-get install tesseract-ocr tesseract-ocr-all -y
apt-get install redis-server -y

printf "正在安装pgm的依赖..."
pip3 install -r requirements.txt

clear

printf "三秒后将编辑配置文件，请填入相应的api_key和api_hash"
cp config.gen.yml config.yml

sleep 3s

nano config.yml

printf "正在启动pgm..."
python3 -m pagermaid
