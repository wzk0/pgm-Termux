import sys
import os

def p(str):
  print(str)

def n():
  print("\n")

def o(action):
  os.system(action)

pkg = "pkg update && pkg upgrade"
ubuntu = "pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh"
rq = "./start-ubuntu.sh"
apt = "apt-get update && apt-get upgrade"
install = "apt install git && apt install python3-pip && apt install nano"
clone = "git clone https://github.com/xtaodada/PagerMaid-Modify.git pagermaid && cp pgm.py pagermaid"
pic = "apt-get install imagemagick -y"
sys = "apt-get install software-properties-common && add-apt-repository ppa:dawidd0811/neofetch && apt-get update && apt-get install neofetch"
qr = "apt-get install libzbar-dev -y"
light = "apt-get install tesseract-ocr tesseract-ocr-all -y"
task = "apt-get install redis-server -y"
yl = "pip3 install -r requirements.txt"
copy = "cp config.gen.yml config.yml"
edit = "nano config.yml"
run = "python3 -m pagermaid"

p("\n欢迎使用pgm-Termux脚本\n\n0)-安装容器  \n1)-安装pgm及其一切所需(进入容器后执行！！)  \n2)-退出")
t = input("\n请输入序号:")
n()
if t == "0":
  sh = 'start-ubuntu.sh'
  if os.path.exists(sh):
    p("你好像已经安装过容器了...\n")
    enter = input("是否直接进入\n[进入后请输入 apt install python3 和 apt install wget ]\n以及 wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/pgm.py \n(y/n):")
    if enter == "y":
      o(rq)
  else:
    p("正在更新pkg源...")
    o(pkg)
    p("pkg源更新完成啦！")
    n()
    p("正在安装容器...")
    o(ubuntu)
    enter = input("容器安装完成啦！是否直接进入\n[进入后请输入 apt install python3 和 apt install wget ]\n以及 wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/pgm.py \n(y/n):")
    if enter == "y":
      o(rq)

if t == "1":
  p("正在更新apt源...")
  o(apt)
  p("apt源更新完成啦！")
  n()
  p("正在安装所有必须项...")
  o(install)
  p("安装完成啦！")
  n()
  p("正在clone仓库...")
  o(clone)
  p("clone完成啦！")
  os.chdir("./pagermaid")
  n()
  p("正在安装依赖...")
  o(yl)
  o(copy)
  p("依赖安装完成啦！")
  n()
  kexuan = input("是否安装所有可选软件包(y/n):")
  if kexuan == "y":
    o(pic)
    o(sys)
    o(qr)
    o(light)
    o(task)
  p("软件包安装完啦！")
  n()
  editor = input("是否编辑config[最上方ID填入数字，Hash填入字符串，不要删除冒号](y/n)")
  if editor =="y":
    o(edit)
  n()
  p("编辑完成，正在读取...")
  n()
  print("开始启动pgm...")
  o(run)
