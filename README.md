## 代码结构
boot.py ：启动参数配置，可以不用。

main.py：主函数代码

data: 素材

    |---Fonts : 字库文件
	
    |---picture：主题图片素材
	
    |---CityCode.txt：全国城市编码

libs: 项目Micropython库

    |---urllib: urequest库
	
    |---ap.py: AP热点配网
	
    |---global_var.py：全局变量定义

ui：UI主题库 

    |---default.py: 默认主题（图片素材位于“/data/picture/default”目录下）
	
    |---dial.py：极简表盘）
	
    |---photo_album.py：默认主题（图片素材位于“/data/picture/photo_album”目录下）

  （用户可以自定义UI主题并在这里添加，通过主函数按键切换，添加过多主题可能导致内存不足。）



## 版本说明

2022-12-12 v1.9
1、增加'扬沙'天气图片和汉字。

2022-11-1 v1.8
1、修复实时温度显示重影问题；
2、增加'雨夹雪'、'小雪'、'中雪'、'大雪'天气图片和汉字。

2022-9-22 v1.7
1、WiFi密码支持空格和特殊字符；

2022-7-28 v1.6
1、WiFi账号支持空格和特殊字符；

2022-7-27 v1.5
1、增加'雾'，'雪'汉字；
2、增加雾的天气图片。

2022-6-24 v1.4
1、增加看门狗功能，超时时间为30秒。
   说明：有需要通过REPL中断代码调试可以将main.py代码中的 wdt = WDT(timeout=30000) 看门狗启动代码注释。

2022-6-22 v1.3
1、WiFi配网网页名称更改，SSID改为WiFi账号，PASSWORD改为WiFi密码。便于用户理解。

2022-6-21 v1.2
1、部分城市无空气质量，不显示。
2、字库文件重大升级，已支持全国所有城市。中文数量1073个，组合城市2444个。

2022-6-15 v1.1
1、支持对纯中文或中文、英文、数字混合的WiFi SSID连接。

2022-6-9：v1.0 
1、正式发布。