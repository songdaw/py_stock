import time,gc,json
from libs import global_var
from data.Fonts import fonts

from libs.urllib import urequest
from ui.default import printChinese


d = global_var.LCD

#定义常用颜色
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

stock_url = r'http://qt.gtimg.cn/q='
sgm = r'sz300661'
sgm_name = r'圣邦股份'
sgm_img = "/data/picture/sgm.jpg"


def stock_display(stock_id, stock_name, stock_img):
    for i in range(5):#失败会重试，最多5次
        try:
            stockURL = urequest.urlopen(stock_url+stock_id)
            text = stockURL.read(1000).split(b'~')
            #print("Get stock ok")
            
            curr_price = text[3].decode('utf-8')
            today_open = text[5].decode('utf-8')
            up_down = text[31].decode('utf-8')
            up_down_per = text[32].decode('utf-8') + r'%'
            
            #d.fill(BLACK)
            if up_down[0] == '-':
                color = GREEN
            else:
                color = RED
            
            if stock_img is not None:
                d.Picture(0, 0, stock_img)
            else:
                d.printStr(stock_id, 0, 0, color, size=3)

            printChinese('当 前 ',10,50,color=color,backcolor=BLACK,size=2)
            d.printStr('          ', 110, 50, BLACK, size=3)
            d.printStr(curr_price, 110, 50, color, size=3)
            printChinese('今 开 ',10,100,color=color,backcolor=BLACK,size=2)
            d.printStr('          ', 110, 100, BLACK, size=3)
            d.printStr(today_open, 110, 100, color, size=3)
            printChinese('涨 跌 ',10,150,color=color,backcolor=BLACK,size=2)
            d.printStr('          ', 110, 150, BLACK, size=3)
            d.printStr(up_down, 110, 150, color, size=3)
            printChinese('涨跌幅 ',10,200,color=color,backcolor=BLACK,size=2)
            d.printStr('          ', 110, 200, BLACK, size=3)
            d.printStr(up_down_per, 110, 200, color, size=3)

            return None
            
        except:
            d.printStr("Can not get stock!", 0, 0, WHITE, size=2)
            print("Can not get stock!",i)
            gc.collect() #内存回收
        time.sleep_ms(1000)


global stock_tick
stock_tick = 61


def UI_Display(datetime):
    global stock_tick

    if global_var.UI_Change:
        global_var.UI_Change = 0        
        d.fill(BLACK)

    if stock_tick != datetime[5]:
        stock_tick = datetime[5]
        stock_display(sgm, sgm_name, sgm_img)
