# TA
appium+robotFramework环境搭建手册

【mac创建appium启动软链接】

ln -s /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js  /usr/local/bin/appium

【命令行启动Appium】
需要远程登录操作
appium -a 0.0.0.0 -p 4723 --session-override
-a 是指定监听的ip（也可写成 --address），后面“0.0.0.0”可以改为你需要的ip地址，0.0.0.0或本机ip，支持其他机器访问，127.0.0.1，不支持外网访问；
-p 是指定监听的端口（也可写成 --port），也可以修改为你需要的端口；
--session-override 是指覆盖之前的session

【远程执行测试脚本】

pybot -v ip:http://172.16.3.173 -v port:4723 path/flowTest.robot
-v 指定执行测试脚本的服务器ip和端口号，‘172.16.3.173:4723’替换为需要的ip和端口号即可
flowTest.robot 需要执行的测试文件，需要绝对路径


pybot -V path/config.py path/smokeTest.robot

config.py
# -*- coding: utf-8 -*-
# python
ip = 'http://172.16.3.173'  #Appium服务ip
port = '4723'  #Appium服务端口号
apkAdress = 'http://221.5.44.91:8666/data/wisegame/1cb74367b5c1881d/tongxunbeifen_35.apk?business_id=9034&task_id=7181019164690874375'    #apk下载链接  

【获取android软件的相关信息】
获取连接的手机devices
adb devices
获取当前启动的appPackage和appActivity
adb shell dumpsys window | grep mCurrentFocus

http://10.14.147.23:8081/repository/maven-snapshots/com/samsclub/oce/score-mobile-app/0.0.1-SNAPSHOT/score-mobile-app-0.0.1-20181210.070234-1.apk
http://10.14.147.21/apk/oce/score-mobile-app-0.0.1-SNAPSHOT.apk

https://dev-tirebattery-webapp.azurewebsites.net/swagger-ui.html#/vehicle-controller/findMakesByYearUsingGET
