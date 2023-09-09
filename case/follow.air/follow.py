# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.report.report import simple_report
from airtest.core.android.android import Android
import requests
import sys
from airtest.cli.parser import runner_parser,get_parser
from airtest.cli.runner import run_script

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


ap = get_parser()
args = ap.parse_args()
phone = args.mobile

size = poco.get_screen_size()

start_app("com.tencent.wework")
sleep(7)

try:
    touch(Template(r"tpl1691982964059.png", record_pos=(0.201, 0.806), resolution=(1080, 2160)))
    sleep(2)
    touch(Template(r"tpl1691982985871.png", record_pos=(-0.357, 0.424), resolution=(1080, 2160)))
    sleep(5)
    
    # 输入手机号
    click(Template(r"tpl1691982632785.png", record_pos=(0.004, -0.694), resolution=(1080, 2160)))

    if phone:
        text(phone)
    sleep(3)
    
    # 点击客户来源
    touch(Template(r"tpl1691983099521.png", record_pos=(-0.001, -0.565), resolution=(1080, 2160)))
    sleep(2)

    # 客户等级
    #swipe(Template(r"tpl1691982695327.png", record_pos=(0.001, 0.759), resolution=(1080, 2160)), Template(r"tpl1691982719805.png", record_pos=(-0.009, 0.514), resolution=(1080, 2160)))
    #touch(Template(r"tpl1691982759827.png", record_pos=(0.417, 0.087), resolution=(1080, 2160)))

    sleep(1)
    
    # 跟进方式 电话
    touch(Template(r"tpl1691982784833.png", record_pos=(-0.068, -0.157), resolution=(1080, 2160)))
    sleep(1)
    
    # 接通情况 接通
    touch(Template(r"tpl1691982816356.png", record_pos=(-0.057, -0.001), resolution=(1080, 2160)))
    sleep(1)
    
    # 跟进结果
    touch(Template(r"tpl1691982832207.png", record_pos=(-0.05, 0.152), resolution=(1080, 2160)))

    # 预计跟进时间
    touch(Template(r"tpl1691982848011.png", record_pos=(-0.009, 0.422), resolution=(1080, 2160)))
    sleep(1)
    touch(Template(r"tpl1691982868229.png", record_pos=(-0.006, 0.767), resolution=(1080, 2160)))
    sleep(1)
    
    # 滑屏
    swipe((0.5*size[0],0.8*size[1]),(0.5*size[0],0.2*size[1]),duration=1)
    sleep(2)
    
    # 跟进内容
    touch(Template(r"tpl1691982898690.png", record_pos=(-0.249, 0.207), resolution=(1080, 2160)))
    text("airtest 自动化跟进测试")
    
    # 提交
    #click((0.6592*size[0],0.8964*size[1]))

finally:
    sleep(3)
    try:
        #simple_report(__file__,logpath=True,output=os.path.join(os.path.dirname(__file__),"report","follow.html"))
        pass
    finally:
        stop_app("com.tencent.wework")
