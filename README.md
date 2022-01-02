# pgm-Termux脚本

**适用于[博客文章](https://wzk0.github.io/pm)的一键(其实是两键🌚)脚本**

## 使用方法:

* 首先在Termux安装`wget`和`python`:

```
apt update
apt upgrade
apt install wget
apt install python
```

* 然后获取该脚本:

```
wget https://raw.githubusercontent.com/wzk0/pgm-Termux/main/pgm.py
```

* 执行:

```
python3 pgm.py
```

## 关键点

* 进入容器前后是两个不同的环境，所以进入前后必须分别获取一遍脚本

