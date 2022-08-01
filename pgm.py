import sys
import os

def p(str):
  print(str)

def n():
  print("\n")

def o(action):
  os.system(action)

def check():
  print("警告:检测到容器已存在或不在容器内！将尝试自动进入容器，请进入后再次使用脚本启动")

pkg = "pkg update && pkg upgrade"
ubuntu = "pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh"
rq = "./start-ubuntu.sh"
apt = "apt-get update && apt-get upgrade"
install = "apt install git -y && apt install python3-pip -y && apt install nano -y"
clone = "git clone https://gitlab.com/Xtao-Labs/pagermaid-modify.git pagermaid && cp pgm.py pagermaid"
pic = "apt-get install imagemagick -y"
qr = "apt-get install libzbar-dev -y"
light = "apt-get install tesseract-ocr tesseract-ocr-all -y"
task = "apt-get install redis-server -y"
yl = "pip3 install -r requirements.txt"
copy = "cp config.gen.yml config.yml"
edit = "nano config.yml"
run = "python3 -m pagermaid"
sh = './start-ubuntu.sh'

p("\n欢迎使用pgm-Termux脚本\n\n0)-安装容器  \n1)-安装pgm及其一切所需(进入容器后执行！！)  \n2)-启动pgm(需要先完成登陆) \n3)-退出 \n4)-一键部署(无自定义度)")
t = input("\n请输入序号:")
n()
if t == "0":
  if os.path.exists(sh):
    check()
    o(rq)
  else:
    p("正在更新pkg源...")
    o(pkg)
    p("pkg源更新完成啦！")
    n()
    p("正在安装容器...")
    o(ubuntu)
    enter = input("容器安装完成啦！是否直接进入\n[进入后请输入\napt update && apt upgrade\napt install python3 wget -y ]\n以及 wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/pgm.py \n(y/n):")
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
    o(qr)
    o(light)
    o(task)
    p("软件包安装完啦！")
    n()
  else:
    pass
  editor = input("是否编辑(编辑器使用nano,Ctrl O保存,随后回车,之后Ctrl X退出)config[最上方ID填入数字，Hash填入字符串，不要删除冒号](y/n)")
  if editor =="y":
    o(edit)
  n()
  p("编辑完成，正在读取...")
  n()
  p('请选择启动模式:\n1.死循环(会一直尝试启动,第一次不建议)\n2. 启动一次')
  cs=input('请输入序号:')
  p("开始启动pgm...")
  if cs=='1':
    while True:
      o(run)
  if cs=='2':
    o(run)

if t == "2":
  p('请选择启动模式:\n1.死循环(会一直尝试启动,第一次不建议)\n2. 启动一次')
  cs=input('请输入序号:')
  print("正在启动pgm...")
  os.chdir("./pagermaid")
  if cs=='1':
    while True:
      o(run)
  if cs=='2':
    o(run)

if t == "4":
  os.system("wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/nobrain.sh && bash nobrain.sh")
