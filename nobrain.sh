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
printf​ "​请输入以下指令: ​"
printf​ "​apt update -y && apt upgrade -y && apt install wget -y && wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/after.sh && bash after.sh​"

./start-ubuntu.sh
<<<<<<< HEAD

clear

printf "请输入以下指令: "
printf "apt update -y && apt upgrade -y && apt install wget -y && wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/after.sh && bash after.sh"
=======
>>>>>>> 1f7a3e6 (添加了after)
