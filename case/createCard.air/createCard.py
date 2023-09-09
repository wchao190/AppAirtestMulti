# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.report.report import LogToHtml,simple_report
import os

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
size = poco.get_screen_size()

## 启动应用
start_app("com.tencent.wework")
sleep(7)

try:
    touch(Template(r"tpl1691985081199.png", record_pos=(0.2, 0.8), resolution=(1080, 2160)))
    sleep(2)
    touch(Template(r"tpl1691985135675.png", record_pos=(0.351, 0.13), resolution=(1080, 2160)))
    sleep(5)

    ## 输入姓名
    click(Template(r"tpl1691125236322.png", record_pos=(0.011, -0.647), resolution=(1080, 2220)))
    text("李珂来")

    ## 输入手机号
    click(Template(r"tpl1691131991432.png", record_pos=(0.016, -0.517), resolution=(1080, 2220)))
    text("18808041455")

    ## 联系地址
    click(Template(r"tpl1691463006849.png", record_pos=(0.005, -0.381), resolution=(1080, 2220)))
    #size = poco.get_screen_size()  # [1080, 2220]

    # 滑动省
    #for i in range(9):
        #swipe((0.1675*size[0],0.7869*size[1]),(0.1675*size[0],0.7324*size[1]),duration=1)
    #滑动市
    #for x in range(4):
        #swipe((0.5009*size[0],0.7869*size[1]),(0.5009*size[0],0.7324*size[1]),duration=1)
    # 滑动县
    #for y in range(7):
        #swipe((0.8342*size[0],0.7869*size[1]),(0.8342*size[0],0.7342*size[1]),duration=1)

    #click((0.9305*size[0],0.6049*size[1]))
    touch(Template(r"tpl1691985315351.png", record_pos=(0.417, 0.082), resolution=(1080, 2160)))

    ## 选择客户来源
    click(Template(r"tpl1691133261822.png", record_pos=(-0.001, -0.246), resolution=(1080, 2220)))
    click(Template(r"tpl1691133295750.png", record_pos=(0.003, -0.057), resolution=(1080, 2220)))
    #click((0.9259*size[0],0.3909*size[1]))
    touch(Template(r"tpl1691985759225.png", record_pos=(0.42, -0.255), resolution=(1080, 2160)))

    ## 选择建卡方式
    click(Template(r"tpl1691133344141.png", record_pos=(0.005, -0.109), resolution=(1080, 2220)))

    ## 选择车系
    click(Template(r"tpl1691133366718.png", record_pos=(0.002, 0.311), resolution=(1080, 2220)))
    click(Template(r"tpl1691133382440.png", record_pos=(0.004, -0.056), resolution=(1080, 2220)))
    #click((0.9259*size[0],0.3909*size[1]))
    touch(Template(r"tpl1691985373100.png", record_pos=(0.424, -0.261), resolution=(1080, 2160)))

    ## 选择客户等级
    click(Template(r"tpl1691133472331.png", record_pos=(0.005, 0.426), resolution=(1080, 2220)))
    touch(Template(r"tpl1691985405402.png", record_pos=(0.414, 0.082), resolution=(1080, 2160)))

    #for l in range(2):
        #swipe((0.5018*size[0],0.7869*size[1]),(0.5018*size[0],0.7324*size[1]),duration=1 )
    #click((0.9305*size[0],0.6049*size[1]))

    ## 预计跟进时间
    pos=exists(Template(r"tpl1691991332886.png", record_pos=(-0.298, 0.691), resolution=(1080, 2220)))
    if not pos:
        swipe((0.5*size[0],0.8*size[1]),(0.5*size[0],0.2*size[1]),duration=1)
        sleep(2)
        click(Template(r"tpl1691991332886.png", record_pos=(-0.298, 0.691), resolution=(1080, 2220)))
        touch(Template(r"tpl1691481494357.png", record_pos=(-0.005, 0.806), resolution=(1080, 2220)))
    else:
        ## 滑动页面
        #poco.swipe((0.5,0.5797), (0.5,0.1180), duration=0.5)
        click(Template(r"tpl1691991332886.png", record_pos=(-0.298, 0.691), resolution=(1080, 2220)))
        touch(Template(r"tpl1691481494357.png", record_pos=(-0.005, 0.806), resolution=(1080, 2220)))
        sleep(2)
        swipe((0.5*size[0],0.8*size[1]),(0.5*size[0],0.2*size[1]),duration=1)
    sleep(2)
    ## 备注信息
    #touch((0.5*size[0],0.7292*size[1]))
    touch(Template(r"tpl1691985448514.png", record_pos=(-0.149, 0.208), resolution=(1080, 2160)))
    text("企业微信 airtest 自动化测试")

    ### 点击提交
    #touch((0.6592*size[0],0.8963*size[1]))

finally:
    sleep(3)
    ## 退出当前应用
    try:
       # simple_report(__file__,logpath=True,output=os.path.join(os.path.dirname(__file__),"report","card.html"))
        pass
    finally:
            stop_app("com.tencent.wework")
