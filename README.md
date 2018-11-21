# TA
appium+robotFramework环境搭建手册

【mac创建appium启动软链接】

ln -s /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js  /usr/local/bin/appium

【命令行启动Appium】

appium -a 0.0.0.0 -p 4723 --session-override
-a 是指定监听的ip（也可写成 --address），后面“0.0.0.0”可以改为你需要的ip地址，0.0.0.0或本机ip，支持其他机器访问，127.0.0.1，不支持外网访问；
-p 是指定监听的端口（也可写成 --port），也可以修改为你需要的端口；
--session-override 是指覆盖之前的session

【远程执行测试脚本】

pybot -v url:http://172.16.3.173:4723/wd/hub flowTest.robot
-v 指定执行测试脚本的服务器ip和端口号，‘172.16.3.173:4723’替换为需要的ip和端口号即可
flowTest.robot 需要执行的测试文件，需要绝对路径


