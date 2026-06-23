#!/bin/sh
# ============================================================
#   命令查询脚本(综合)(适配系统)  v2.1
#   适用: MT管理器终端 / Termux / Linux / Android
# ============================================================
#   特点:
#   - 235+ 条常用命令内嵌在脚本中，零临时文件！
#   - 3 级菜单导航：主菜单 → 结果列表 → 命令详情
#   - 兼容 POSIX sh，MT终端和Termux都能跑
# ============================================================
#   📖 如何加命令？
#   找到下方 load_dict() 函数内的 CMDEOF 区域，
#   按格式 命令名|分类|用法|说明|示例 添加一行即可。
# ============================================================

# ============================================================
#   ⚙️【配置区】—— 你只改这里！
# ============================================================

# 显示模式: "progress"=进度条  "stream"=流式蹦出
DISPLAY_MODE="progress"

# 流式输出速度（秒），越小越快
STREAM_SPEED="0.08"

# 查完是否继续: "yes"=继续  "no"=查完就退
LOOP_MODE="yes"

# ============================================================
#   📚 字典数据区  ============================================
#   ↓↓↓ 要加命令在这里加一行！格式: 命令名|分类|用法|说明|示例
# ============================================================
#   注意: CMDEOF 是分隔标记，不能删！
# ============================================================
load_dict() {
    cat << 'CMDEOF'
cd|文件管理|cd [目录路径]|切换当前工作目录|cd /sdcard
ls|文件管理|ls [选项] [路径]|列出目录内容|ls -la /sdcard
cp|文件管理|cp [选项] <源> <目标>|复制文件或目录|cp -r dir1 dir2
mv|文件管理|mv [选项] <源> <目标>|移动或重命名文件|mv old.txt new.txt
rm|文件管理|rm [选项] <文件>|删除文件或目录|rm -rf unwanted_dir/
mkdir|文件管理|mkdir [选项] <目录名>|创建目录|mkdir -p a/b/c
rmdir|文件管理|rmdir [选项] <目录名>|删除空目录|rmdir empty_dir
touch|文件管理|touch [选项] <文件>|创建空文件或更新时间戳|touch newfile.txt
cat|文件管理|cat [选项] <文件>|查看文件全部内容|cat /etc/hosts
less|文件管理|less [选项] <文件>|分页查看（支持上下翻页）|less largefile.log
more|文件管理|more [选项] <文件>|分页查看（只能向下）|more long_text.txt
head|文件管理|head [选项] <文件>|查看文件开头N行|head -n 20 file.txt
tail|文件管理|tail [选项] <文件>|查看文件末尾或实时追踪|tail -f log.txt
find|文件管理|find <路径> [选项]|搜索文件|find /sdcard -name "*.mp3"
locate|文件管理|locate <关键词>|快速定位文件|locate passwd
chmod|文件管理|chmod [选项] <权限> <文件>|修改文件权限|chmod 755 script.sh
chown|文件管理|chown [选项] <用户>[:组] <文件>|修改文件所有者|chown user:group file.txt
ln|文件管理|ln [选项] <源> <链接名>|创建链接（硬/软）|ln -s /sdcard/download link
stat|文件管理|stat [选项] <文件>|显示文件详细状态|stat file.txt
du|文件管理|du [选项] [路径]|统计磁盘使用量|du -sh /sdcard
df|文件管理|df [选项] [挂载点]|显示磁盘剩余空间|df -h
mount|文件管理|mount [选项] <设备> <挂载点>|挂载文件系统|mount -o loop image.iso /mnt
umount|文件管理|umount [选项] <挂载点>|卸载文件系统|umount /mnt
sync|文件管理|sync|将缓存写入磁盘|sync
rsync|文件管理|rsync [选项] <源> <目标>|高效同步文件|rsync -avz dir/ user@host:/path/
scp|文件管理|scp [选项] <源> <目标>|通过SSH安全复制文件|scp file.txt user@host:~/
rename|文件管理|rename [选项] <表达式> <文件>|批量重命名|rename 's/\.JPG$/.jpg/' *.JPG
tree|文件管理|tree [选项] [路径]|树形显示目录结构|tree -L 2 /sdcard
file|文件管理|file [选项] <文件>|检测文件实际类型|file /bin/ls
basename|文件管理|basename <路径> [后缀]|提取文件名|basename /a/b/c.txt .txt
dirname|文件管理|dirname <路径>|提取目录部分|dirname /a/b/c.txt
realpath|文件管理|realpath [选项] <路径>|获取绝对路径|realpath ~/link
mktemp|文件管理|mktemp [选项]|创建临时文件或目录|mktemp -d
readlink|文件管理|readlink [选项] <链接>|显示链接指向的目标|readlink /usr/bin/python
grep|文本处理|grep [选项] <模式> [文件]|搜索文本（支持正则）|grep -rn "TODO" *.sh
sed|文本处理|sed [选项] <脚本> [文件]|流式文本编辑器|sed -i 's/old/new/g' file.txt
awk|文本处理|awk [选项] <程序> [文件]|强大的文本分析工具|awk '{print $1,$NF}' file.txt
cut|文本处理|cut [选项] [文件]|按列截取文本|cut -d: -f1 /etc/passwd
sort|文本处理|sort [选项] [文件]|文本排序|sort -k2 -n grades.txt
uniq|文本处理|uniq [选项] [文件]|去除或统计重复行|sort file.txt | uniq -c
wc|文本处理|wc [选项] [文件]|统计行数/单词数/字符数|wc -l file.txt
tr|文本处理|tr [选项] <set1> [set2]|替换或删除字符|tr 'a-z' 'A-Z' < input.txt
diff|文本处理|diff [选项] <文件1> <文件2>|比较两个文件差异|diff -u old.txt new.txt
patch|文本处理|patch [选项] <原文件> <补丁>|应用补丁|patch < fix.patch
echo|文本处理|echo [字符串]|输出文本|echo "Hello World"
printf|文本处理|printf <格式> [参数]|格式化输出|printf "%03d\n" 5
fmt|文本处理|fmt [选项] [文件]|格式化文本段落|fmt -w 80 file.txt
fold|文本处理|fold [选项] [文件]|按宽度折叠长行|fold -w 72 file.txt
join|文本处理|join [选项] <文件1> <文件2>|基于公共字段合并文件|join -t: a.txt b.txt
paste|文本处理|paste [选项] [文件...]|按列合并多个文件|paste f1.txt f2.txt
split|文本处理|split [选项] <文件> [前缀]|分割大文件|split -l 1000 bigfile chunk_
tee|文本处理|tee [选项] <文件>|同时输出到终端和文件|echo "data" | tee log.txt
expand|文本处理|expand [选项] [文件]|制表符转空格|expand -t 4 file.txt
unexpand|文本处理|unexpand [选项] [文件]|空格转制表符|unexpand -t 4 file.txt
rev|文本处理|rev [选项] [文件]|反转每行字符顺序|echo "hello" | rev
strings|文本处理|strings [选项] <文件>|提取二进制中的可读字符串|strings /bin/ls | head
iconv|文本处理|iconv [选项] <文件>|转换文件编码|iconv -f GBK -t UTF-8 file.txt
xargs|文本处理|xargs [选项] <命令>|将输入转为命令参数|find . -name "*.txt" | xargs rm
comm|文本处理|comm [选项] <文件1> <文件2>|比较两个已排序文件|comm -12 sorted1.txt sorted2.txt
ping|网络相关|ping [选项] <目标>|测试网络连通性和延迟|ping -c 4 google.com
curl|网络相关|curl [选项] <URL>|发送网络请求或下载文件|curl -O https://example.com/file.zip
wget|网络相关|wget [选项] <URL>|下载文件（支持断点续传）|wget -c https://example.com/bigfile.iso
ssh|网络相关|ssh [选项] <用户@主机>|SSH远程连接|ssh user@192.168.1.100
ifconfig|网络相关|ifconfig [接口] [参数]|查看或配置网络接口|ifconfig wlan0
ip|网络相关|ip [选项] <对象> <命令>|网络配置管理工具|ip addr show
netstat|网络相关|netstat [选项]|显示网络连接和路由表|netstat -tuln
nslookup|网络相关|nslookup <域名>|查询DNS解析记录|nslookup baidu.com
dig|网络相关|dig [选项] <域名> [类型]|更强大的DNS查询|dig A baidu.com
traceroute|网络相关|traceroute [选项] <目标>|追踪数据包路由路径|traceroute google.com
nmap|网络相关|nmap [选项] <目标>|网络端口扫描|nmap -sS 192.168.1.1
nc|网络相关|nc [选项] <主机> <端口>|网络调试工具（netcat）|nc -zv 127.0.0.1 22
route|网络相关|route [选项]|查看或修改路由表|route -n
ss|网络相关|ss [选项]|查看套接字统计（替代netstat）|ss -tuln
host|网络相关|host [选项] <域名> [服务器]|简洁版DNS查询|host baidu.com
telnet|网络相关|telnet <主机> <端口>|Telnet远程连接|telnet 192.168.1.1 23
ftp|网络相关|ftp <主机>|FTP文件传输|ftp ftp.example.com
hostnamectl|网络相关|hostnamectl [选项]|查看或设置主机名|hostnamectl set-hostname mydevice
ps|进程管理|ps [选项]|显示当前进程快照|ps aux
top|进程管理|top [选项]|实时显示进程状态和负载|top -u root
htop|进程管理|htop [选项]|增强版top（彩色/鼠标）|htop
kill|进程管理|kill [选项] <PID>|终止指定进程|kill -9 1234
pkill|进程管理|pkill [选项] <名称>|按名称批量杀进程|pkill -f python
killall|进程管理|killall [选项] <名称>|杀死所有同名进程|killall -9 java
nice|进程管理|nice [选项] <命令>|以指定优先级运行程序|nice -n 5 ./script.sh
renice|进程管理|renice <优先级> <PID>|调整运行中进程优先级|renice -5 1234
nohup|进程管理|nohup <命令> [参数]|退出终端后继续运行|nohup python server.py &
bg|进程管理|bg [作业号]|将暂停作业放到后台|bg %1
fg|进程管理|fg [作业号]|将后台作业调到前台|fg %1
jobs|进程管理|jobs [选项]|显示后台作业列表|jobs -l
wait|进程管理|wait [PID]|等待后台进程结束|wait $!
timeout|进程管理|timeout [选项] <秒数> <命令>|超时后自动终止|timeout 5 ping google.com
pstree|进程管理|pstree [选项] [PID]|树形显示进程关系|pstree -p
lsof|进程管理|lsof [选项]|列出系统打开的文件|lsof -i :8080
watch|进程管理|watch [选项] <命令>|周期性执行并刷新|watch -n 1 'ps aux | head'
uname|系统信息|uname [选项]|显示系统内核信息|uname -a
hostname|系统信息|hostname|显示或设置系统主机名|hostname
uptime|系统信息|uptime|显示系统运行时间和负载|uptime
dmesg|系统信息|dmesg [选项]|显示内核日志（硬件和驱动）|dmesg | grep error
free|系统信息|free [选项]|显示内存使用情况|free -h
lscpu|系统信息|lscpu [选项]|显示CPU架构信息|lscpu
lspci|系统信息|lspci [选项]|列出PCI设备|lspci -vnn
lsusb|系统信息|lsusb [选项]|列出USB设备|lsusb -v
lsblk|系统信息|lsblk [选项]|列出块设备（磁盘和分区）|lsblk -f
blkid|系统信息|blkid [选项] [设备]|显示UUID和文件系统类型|blkid /dev/block/mmcblk0
env|系统信息|env [选项]|显示环境变量|env | grep PATH
printenv|系统信息|printenv [变量名]|打印指定环境变量|printenv HOME
whoami|系统信息|whoami|显示当前登录用户名|whoami
id|系统信息|id [选项] [用户]|显示用户UID、GID和所属组|id
who|系统信息|who [选项]|显示当前登录用户|who -a
w|系统信息|w [选项] [用户]|显示登录用户及其执行的命令|w
last|系统信息|last [选项] [用户]|显示最近登录记录|last -10
date|系统信息|date [选项] [+格式]|显示或设置日期时间|date +%Y-%m-%d
cal|系统信息|cal [选项] [月] [年]|显示日历|cal -y 2026
arch|系统信息|arch|显示系统架构（如aarch64）|arch
nproc|系统信息|nproc [选项]|显示CPU核心数|nproc --all
pkg|包管理|pkg <子命令> [包名]|Termux包管理器|pkg install python
apt|包管理|apt [子命令] [选项] [包名]|Debian系包管理器|apt update && apt upgrade
dpkg|包管理|dpkg [选项] <包名>|Debian底层包管理器|dpkg -i package.deb
pip|包管理|pip <子命令> [选项] [包名]|Python包管理器|pip install requests
npm|包管理|npm <子命令> [选项] [包名]|Node.js包管理器|npm install express
gem|包管理|gem <子命令> [选项] [包名]|Ruby包管理器|gem install rails
cargo|包管理|cargo <子命令> [选项]|Rust包管理器|cargo build --release
tar|压缩归档|tar [选项] <归档> [文件...]|创建或解压tar包|tar -czf archive.tar.gz dir/
gzip|压缩归档|gzip [选项] <文件>|压缩为.gz格式|gzip -k file.txt
gunzip|压缩归档|gunzip [选项] <文件>|解压.gz文件|gunzip file.txt.gz
bzip2|压缩归档|bzip2 [选项] <文件>|压缩为.bz2格式|bzip2 -k file.txt
bunzip2|压缩归档|bunzip2 [选项] <文件>|解压.bz2文件|bunzip2 file.txt.bz2
xz|压缩归档|xz [选项] <文件>|压缩为.xz格式|xz -k file.txt
unxz|压缩归档|unxz [选项] <文件>|解压.xz文件|unxz file.txt.xz
zcat|压缩归档|zcat [选项] <文件.gz>|查看压缩文件内容|zcat log.gz | grep error
zip|压缩归档|zip [选项] <压缩包> <文件...>|压缩为.zip格式|zip -r archive.zip dir/
unzip|压缩归档|unzip [选项] <文件.zip>|解压.zip文件|unzip archive.zip -d target_dir
7z|压缩归档|7z <子命令> [选项] <归档>|7-Zip压缩或解压（需p7zip）|7z x archive.7z
fdisk|磁盘存储|fdisk [选项] <设备>|磁盘分区管理工具|fdisk -l
parted|磁盘存储|parted [选项] <设备> [命令]|分区工具（支持GPT）|parted /dev/block/mmcblk0 print
mkfs|磁盘存储|mkfs [选项] <设备>|创建文件系统|mkfs.ext4 /dev/sdb1
fsck|磁盘存储|fsck [选项] <设备>|检查并修复文件系统错误|fsck /dev/sda1
dd|磁盘存储|dd [选项]|低级复制工具（可备份整个磁盘）|dd if=/dev/sda of=backup.img bs=4M
smartctl|磁盘存储|smartctl [选项] <设备>|查看硬盘S.M.A.R.T.健康状态|smartctl -a /dev/sda
losetup|磁盘存储|losetup [选项] <设备> <文件>|设置循环设备|losetup /dev/loop0 image.img
useradd|用户权限|useradd [选项] <用户名>|创建新用户|useradd -m newuser
usermod|用户权限|usermod [选项] <用户名>|修改用户属性|usermod -aG sudo newuser
userdel|用户权限|userdel [选项] <用户名>|删除用户|userdel -r olduser
groupadd|用户权限|groupadd [选项] <组名>|创建新用户组|groupadd developers
groupdel|用户权限|groupdel <组名>|删除用户组|groupdel oldgroup
passwd|用户权限|passwd [选项] [用户名]|修改密码|passwd
su|用户权限|su [选项] [用户]|切换用户身份|su - root
sudo|用户权限|sudo [选项] <命令>|以超级用户执行命令|sudo apt update
umask|用户权限|umask [选项] <掩码>|设置新建文件默认权限掩码|umask 022
chage|用户权限|chage [选项] <用户名>|修改密码过期信息|chage -M 90 username
termux-open|Android专属|termux-open <文件或URL>|用应用打开文件或链接|termux-open https://google.com
termux-clipboard-get|Android专属|termux-clipboard-get|读取Android剪贴板|termux-clipboard-get
termux-clipboard-set|Android专属|termux-clipboard-set <文本>|设置Android剪贴板|termux-clipboard-set "hello"
termux-battery-status|Android专属|termux-battery-status|获取电池状态（JSON格式）|termux-battery-status
termux-wifi-scaninfo|Android专属|termux-wifi-scaninfo|扫描附近WiFi信息|termux-wifi-scaninfo
termux-sensor|Android专属|termux-sensor [选项] [传感器]|读取传感器数据|termux-sensor -s "Accelerometer" -n 5
termux-toast|Android专属|termux-toast [选项] <文本>|显示系统提示（Toast）|termux-toast "Hello!"
termux-notification|Android专属|termux-notification [选项]|发送系统通知|termux-notification --title "提醒" --content "完成啦"
termux-camera-photo|Android专属|termux-camera-photo [选项] <文件>|拍照并保存为图片|termux-camera-photo photo.jpg
termux-media-scan|Android专属|termux-media-scan [文件或目录]|通知系统扫描媒体文件|termux-media-scan ~/downloads
termux-wake-lock|Android专属|termux-wake-lock <子命令>|防止设备进入休眠|termux-wake-lock lock
termux-torch|Android专属|termux-torch <on或off>|控制相机闪光灯（手电筒）|termux-torch on
am|Android专属|am <子命令> [选项]|活动管理器（启动应用或广播）|am start -a android.intent.action.VIEW -d https://google.com
input|Android专属|input <子命令> [参数]|模拟输入事件（触摸或按键）|input tap 500 1000
pm|Android专属|pm <子命令> [选项]|包管理器（列出或管理应用）|pm list packages | grep wechat
settings|Android专属|settings <子命令> [参数]|修改系统设置|settings put global airplane_mode_on 1
dumpsys|Android专属|dumpsys [选项] [服务]|转储系统服务状态|dumpsys battery
logcat|Android专属|logcat [选项] [过滤器]|查看系统日志|logcat -c && logcat
screencap|Android专属|screencap [选项] <文件>|截取屏幕截图|screencap /sdcard/screen.png
screenrecord|Android专属|screenrecord [选项] <文件>|录制屏幕视频|screenrecord --time-limit 10 /sdcard/demo.mp4
alias|Shell内置|alias [别名=命令]|创建或查看命令别名|alias ll='ls -la'
unalias|Shell内置|unalias <别名>|删除命令别名|unalias ll
type|Shell内置|type [选项] <命令名>|显示命令的类型|type cd
which|Shell内置|which [选项] <命令名>|定位可执行文件路径|which python
command|Shell内置|command [选项] <命令> [参数]|以内置方式执行命令|command -v ls
exec|Shell内置|exec <命令> [参数]|替换当前Shell进程|exec zsh
eval|Shell内置|eval <参数>|将字符串作为命令执行|eval "echo $HOME"
source|Shell内置|source <文件名>|在当前Shell执行脚本（同.）|source ~/.bashrc
export|Shell内置|export [变量名[=值]]|设置或导出环境变量|export PATH=$PATH:/my/bin
readonly|Shell内置|readonly [变量名=值]|将变量设为只读|readonly PI=3.14159
return|Shell内置|return [N]|从函数返回并指定退出码|return 1
exit|Shell内置|exit [N]|退出Shell或脚本|exit 0
break|Shell内置|break [N]|跳出循环|break 2
continue|Shell内置|continue [N]|跳过本次循环剩余部分|continue
test|Shell内置|test <条件>|条件测试表达式|test -f file.txt && echo "存在"
trap|Shell内置|trap <命令> <信号>|捕获信号并执行命令|trap "rm -f /tmp/tmpfile" EXIT
read|Shell内置|read [选项] [变量名]|从标准输入读取一行|read -p "输入名字: " name
ulimit|Shell内置|ulimit [选项] [限制值]|设置用户资源限制|ulimit -n 4096
sleep|日期时间|sleep <秒数>|延迟指定时间（支持小数）|sleep 0.5
hwclock|日期时间|hwclock [选项]|查看或同步硬件时钟|hwclock --show
at|日期时间|at [选项] <时间>|在指定时间执行一次任务|at now + 1 minute
crontab|日期时间|crontab [选项]|管理定时任务（cron）|crontab -e
timedatectl|日期时间|timedatectl [选项] [命令]|查看或设置时间和时区|timedatectl list-timezones
time|日期时间|time <命令> [参数]|测量命令执行时间|time sleep 1
clear|终端控制|clear|清空终端屏幕|clear
reset|终端控制|reset|重置终端显示（乱码时救命）|reset
stty|终端控制|stty [选项]|查看或修改终端行设置|stty -a
tty|终端控制|tty|显示当前终端的设备文件名|tty
seq|终端控制|seq [选项] <首数> [增量] <末数>|生成数字序列|seq -w 1 100
yes|终端控制|yes [字符串]|持续输出字符串（自动确认）|yes "" | apt install
script|终端控制|script [选项] [文件]|记录终端会话到文件|script session.log
git|开发工具|git <子命令> [选项]|分布式版本控制系统|git clone https://github.com/user/repo
python|开发工具|python [选项] [文件]|Python解释器|python -c "print('hello')"
node|开发工具|node [选项] [文件]|Node.js运行时|node app.js
gcc|开发工具|gcc [选项] <源文件>|GNU C编译器|gcc -o hello hello.c
g++|开发工具|g++ [选项] <源文件>|GNU C++编译器|g++ -o hello hello.cpp
make|开发工具|make [选项] [目标]|自动化构建（Makefile）|make && make install
cmake|开发工具|cmake [选项] <源目录>|构建系统生成器|cmake -B build
perl|开发工具|perl [选项] <文件>|Perl解释器|perl -e 'print "Hello\n"'
lua|开发工具|lua [选项] [文件]|Lua解释器|lua -e 'print("hello")'
gdb|开发工具|gdb [选项] <程序>|GNU调试器|gdb ./a.out core
strace|开发工具|strace [选项] <命令>|跟踪系统调用和信号|strace -f -e open ls
nm|开发工具|nm [选项] <文件>|列出目标文件中的符号|nm -C a.out | grep main
ldd|开发工具|ldd [选项] <文件>|查看程序依赖的共享库|ldd /bin/ls
strip|开发工具|strip [选项] <文件>|去除符号表（减小体积）|strip myprogram
bc|其他工具|bc [选项] [文件]|高精度计算器|echo "scale=2; 10/3" | bc
expr|其他工具|expr <表达式>|整数运算和字符串操作|expr 5 + 3
shuf|其他工具|shuf [选项] [文件]|随机排列或生成随机数|shuf -i 1-10 -n 3
screen|其他工具|screen [选项]|终端多路复用器|screen -S mysession
tmux|其他工具|tmux [命令] [选项]|终端复用器（增强版screen）|tmux new -s mysession
column|其他工具|column [选项] [文件]|将文本按列对齐显示|column -t -s: /etc/passwd
figlet|其他工具|figlet [选项] <文本>|用ASCII艺术字显示文本|figlet "Linux"
openssl|网络调试|openssl <子命令> [选项]|SSL/TLS加密工具|openssl s_client -connect google.com:443
sftp|网络调试|sftp [选项] <用户@主机>|SSH文件传输工具|sftp user@server:/path/
ssh-keygen|网络调试|ssh-keygen [选项]|生成SSH密钥对|ssh-keygen -t ed25519
ssh-copy-id|网络调试|ssh-copy-id <用户@主机>|复制公钥到远程服务器|ssh-copy-id user@server
whois|网络调试|whois <域名>|查询域名注册信息|whois example.com
tcpdump|网络调试|tcpdump [选项] [表达式]|抓取网络数据包|tcpdump -i wlan0 port 80
docker|容器管理|docker <子命令> [选项]|容器管理平台|docker run -it ubuntu bash
docker ps|容器管理|docker ps [选项]|列出运行中的容器|docker ps -a
docker images|容器管理|docker images [选项]|列出本地Docker镜像|docker images
docker build|容器管理|docker build [选项] <路径>|构建镜像|docker build -t myapp .
docker exec|容器管理|docker exec [选项] <容器> <命令>|在容器中执行命令|docker exec -it container1 bash
docker logs|容器管理|docker logs [选项] <容器>|查看容器日志|docker logs -f container1
docker pull|容器管理|docker pull <镜像名>|拉取镜像|docker pull alpine:latest
CMDEOF
}
# ============================================================
#   📚 字典数据区结束  ========================================
#   以上 load_dict() 内的CMDEOF之间就是所有字典数据。
#   要加命令，在 CMDEOF 之间按格式加一行即可！
# ============================================================

# ============================================================
#   ⚙️ 以下为主程序 —— 不用改！
# ============================================================

# ---------- 颜色 ----------
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[0;33m'
BLUE='\033[0;34m'; MAGENTA='\033[0;35m'; CYAN='\033[0;36m'
WHITE='\033[0;37m'; BOLD='\033[1m'; DIM='\033[2m'; NC='\033[0m'
CLS='\033[2J\033[H'

# ---------- 全局变量 ----------
TOTAL_LINES=0

# ---------- 显示标题 ----------
show_banner() {
    printf "%b" "$CLS"
    printf "${BOLD}${CYAN}"
    echo "  ╔══════════════════════════════════════╗"
    echo "  ║    🚀 命令查询脚本 v2.1             ║"
    echo "  ║    综合适配 MT/ Termux / Linux      ║"
    echo "  ╚══════════════════════════════════════╝"
    printf "${NC}\n"
}

print_line()  { printf "${DIM}${BLUE}──────────────────────────────────────${NC}\n"; }
print_thick() { printf "${BOLD}${CYAN}══════════════════════════════════════${NC}\n"; }

# ---------- 获取字典数据 ----------
get_dict_data() { load_dict; }

# ---------- 初始化 ----------
init_dict() {
    TOTAL_LINES=$(get_dict_data | wc -l)
    [ "$TOTAL_LINES" -eq 0 ] && TOTAL_LINES=1
}

# ---------- 显示命令详情 ----------
show_detail() {
    print_thick
    printf "${BOLD}${MAGENTA}  📖 命令详情${NC}\n"
    print_line
    printf "  ${BOLD}命令名:${NC}    ${GREEN}${BOLD}%s${NC}\n" "$1"
    [ -n "$2" ] && [ "$2" != " " ] && printf "  ${BOLD}分　　类:${NC}    ${YELLOW}%s${NC}\n" "$2"
    [ -n "$3" ] && [ "$3" != " " ] && printf "  ${BOLD}用　　法:${NC}    ${CYAN}%s${NC}\n" "$3"
    [ -n "$4" ] && [ "$4" != " " ] && printf "  ${BOLD}说　　明:${NC}    ${WHITE}%s${NC}\n" "$4"
    [ -n "$5" ] && [ "$5" != " " ] && printf "  ${BOLD}示　　例:${NC}    ${YELLOW}%s${NC}\n" "$5"
    print_thick
}

trim() { echo "$1" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'; }

# ---------- 菜单选择 ----------
menu_select() {
    prompt="$1"; shift
    item_count=$#
    echo ""
    printf "${BOLD}${prompt}${NC}\n"
    printf "${DIM}请输入数字选择:${NC}\n\n"
    i=1
    for item in "$@"; do
        printf "  ${GREEN}${BOLD}%d${NC}. ${WHITE}%s${NC}\n" "$i" "$item"
        i=$((i + 1))
    done
    printf "\n  ${CYAN}→${NC} "
    read -r choice
    case "$choice" in
        ''|*[!0-9]*) return 0 ;;
        *) [ "$choice" -ge 1 ] 2>/dev/null && [ "$choice" -le "$item_count" ] 2>/dev/null && return "$choice"; return 0 ;;
    esac
}

# ---------- 精确查询 ----------
exact_query() {
    show_banner
    printf "${BOLD}${GREEN}✔🔥${NC} ${BOLD}------- 精准模式${NC}\n"
    printf "${YELLOW}输入你想要查询的命令!${NC}\n"
    print_line
    printf "  ${CYAN}→${NC} "
    read -r search_cmd
    search_cmd=$(trim "$search_cmd")
    [ -z "$search_cmd" ] && { printf "\n${YELLOW}⚠️  没有输入内容${NC}\n"; sleep 1; return; }

    found=false
    while IFS='|' read -r name category usage desc example; do
        if [ "$(trim "$name")" = "$search_cmd" ]; then
            show_detail "$(trim "$name")" "$(trim "$category")" "$(trim "$usage")" "$(trim "$desc")" "$(trim "$example")"
            found=true; break
        fi
    done << DICTEOF
$(get_dict_data)
DICTEOF

    if [ "$found" = false ]; then
        print_thick
        printf "${RED}${BOLD}  😢 Not found  TvT${NC}\n"
        printf "${YELLOW}  字典中未收录 '%s'${NC}\n" "$search_cmd"
        print_thick
    fi
}

# ---------- 指令集查询（3级菜单）----------
prefix_query() {
    show_banner
    printf "${BOLD}${MAGENTA}✔┄┄┄┄ 指令集查询:${NC}\n"
    printf "${YELLOW}输入你印象中的指令部分${NC}\n"
    print_line
    printf "  ${CYAN}→${NC} "
    read -r search_prefix
    search_prefix=$(trim "$search_prefix")
    [ -z "$search_prefix" ] && { printf "\n${YELLOW}⚠️  没有输入内容${NC}\n"; sleep 1; return; }

    printf "\n${BOLD}🔍 正在搜索以 '%s' 开头的命令...${NC}\n\n" "$search_prefix"

    # ---- 扫描阶段 ----
    current=0; match_count=0; match_list=""; total=$TOTAL_LINES

    while IFS='|' read -r name category usage desc example; do
        current=$((current + 1))

        # 短进度条（20格）
        if [ "$DISPLAY_MODE" = "progress" ]; then
            percent=$((current * 100 / total))
            blen=$((percent * 20 / 100))
            [ "$blen" -gt 20 ] && blen=20
            bar=""; i=0
            while [ "$i" -lt "$blen" ]; do bar="${bar}="; i=$((i+1)); done
            i=0; while [ "$i" -lt $((20 - blen)) ]; do bar="${bar} "; i=$((i+1)); done
            printf "\r  ${CYAN}[${bar}]${NC} ${BOLD}%3d%%${NC}" "$percent"
        fi

        name_trim=$(trim "$name")
        case "$name_trim" in
            "${search_prefix}"*)
                match_count=$((match_count + 1))
                # 构建条目（用真实换行，避免 $(...) 吃掉末尾 \n）
                mentry="$name_trim|$(trim "$category")|$(trim "$usage")|$(trim "$desc")|$(trim "$example")
"               # ← 上面引号里有一个真实换行，不能删！
                match_list="${match_list}${mentry}"
                if [ "$DISPLAY_MODE" = "stream" ]; then
                    printf "\n  ${GREEN}%s${NC}  ${DIM}- %s${NC}\n" "$name_trim" "$(trim "$desc")"
                    sleep "$STREAM_SPEED"
                fi
                ;;
        esac
    done << DICTEOF
$(get_dict_data)
DICTEOF

    printf "\n"   # 换行，避免进度条残留

    if [ "$match_count" -eq 0 ]; then
        print_thick
        printf "${RED}${BOLD}  😢 无此类别，字典可能未收录 TvT${NC}\n"
        printf "${YELLOW}  没有以 '%s' 开头的命令${NC}\n" "$search_prefix"
        print_thick
        return
    fi

    # ---- 3 级菜单循环 ----
    while true; do
        # 2级：显示结果列表
        printf "\n${BOLD}${GREEN}  ✅ 匹配到 %d 条命令 (前缀: %s)${NC}\n\n" "$match_count" "$search_prefix"

        if [ "$DISPLAY_MODE" = "progress" ]; then
            idx=0
            printf '%s' "$match_list" | while IFS='|' read -r mn mc mu md me; do
                [ -z "$mn" ] && continue
                idx=$((idx + 1))
                printf "  ${GREEN}%3d.${NC} %-20s ${DIM}%s${NC}\n" "$idx" "$mn" "$md"
            done
        fi

        printf "\n"; print_line
        printf "${YELLOW}💡 输入序号(1-%d)查看详情，回车返回主菜单，q退出${NC}\n" "$match_count"
        printf "  ${CYAN}→${NC} "
        read -r choice

        case "$choice" in
            q|Q) exit 0 ;;
            '')  return ;;   # 回车 → 1级（主菜单）

            *)
                if echo "$choice" | grep -q '^[1-9][0-9]*$' 2>/dev/null && \
                   [ "$choice" -le "$match_count" ] 2>/dev/null; then
                    # 3级：显示命令详情
                    cur=0
                    printf '%s' "$match_list" | while IFS='|' read -r mn mc mu md me; do
                        [ -z "$mn" ] && continue
                        cur=$((cur + 1))
                        if [ "$cur" -eq "$choice" ]; then
                            show_detail "$mn" "$mc" "$mu" "$md" "$me"
                            break
                        fi
                    done
                    # 按回车返回 2级（结果列表）
                    printf "\n${BOLD}${YELLOW}↩️  按回车返回结果列表${NC}"
                    read -r dummy
                    continue
                else
                    printf "${RED}❌ 无效输入${NC}\n"
                    sleep 0.5
                    continue
                fi
                ;;
        esac
    done
}

# ---------- 结束 ----------
exit_script() {
    show_banner
    printf "\n${BOLD}${GREEN}  ✨ 感谢使用！祝你玩得开心 💪${NC}\n"
    printf "${DIM}  内置字典: %d 条命令${NC}\n\n" "$TOTAL_LINES"
    exit 0
}

# ============================================================
#   🚀 主程序入口
# ============================================================
show_banner
printf "${BOLD}📚 正在加载内置字典...${NC}"
init_dict
printf " ${GREEN}${BOLD}完成！${NC} ${DIM}(%d 条命令)${NC}\n" "$TOTAL_LINES"
sleep 0.3

while true; do
    show_banner
    printf "${BOLD}${GREEN}✅ 字典已就绪 (%d 条记录)${NC}\n\n" "$TOTAL_LINES"
    menu_select "?---------------- 请选择查询模式" \
        "🔍  精确查询" \
        "📋  指令集查询" \
        "🚪  退出工具"
    sel=$?
    case "$sel" in
        1) exact_query ;;
        2) prefix_query ;;
        3|0) exit_script ;;
    esac
    if [ "$LOOP_MODE" = "yes" ]; then
        printf "\n"; print_line
        printf "${YELLOW}按 回车 继续查询，输入 q 退出${NC}\n"
        printf "  ${CYAN}→${NC} "
        read -r cont
        case "$cont" in q|Q|exit) exit_script ;; esac
    else
        exit_script
    fi
done
