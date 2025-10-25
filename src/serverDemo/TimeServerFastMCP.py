from mcp.server.fastmcp import FastMCP
import logging
import time
from datetime import datetime,timedelta
import cnlunar #中国农历

#@author BiHongCue876
#功能：测试时间获取的MCP工具

#日志记录器
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s") #日志格式
logger=logging.getLogger(__name__)

#创建FastMCP实例，命名为CurrentTime
mcp=FastMCP("CurrentTime")

#时间戳
@mcp.tool()
def time_stamp():
    """current time(ms)"""
    t = time.time()
    logger.info("current time stamp: %f",t)
    return t

#格式化日期
@mcp.tool()
def current_date_time():
    """getting current date time"""
    current=datetime.now()
    #格式化
    fmttm=current.strftime("%Y-%m-%dT%H:%M:%S")
    logger.info("formatted current time: %s",fmttm)
    return fmttm

#农历日期
@mcp.tool()
def cnlunar_date() -> str:
    date=[datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute]
    logger.info("cnlunar農曆日期：公曆%d年%d月%d日%d時%d分",date[0],date[1],date[2],date[3],date[4])
    a = cnlunar.Lunar(datetime(date[0], date[1], date[2], date[3], date[4]), godType='8char')  # 常规算法
    # a = cnlunar.Lunar(datetime.datetime(2022, 2, 3, 10, 30), godType='8char', year8Char='beginningOfSpring')  # 八字立春切换算法
    #钦定算法农历库用法全图
    dic = {
        '日期': a.date,
        '农历数字': (a.lunarYear, a.lunarMonth, a.lunarDay, '闰' if a.isLunarLeapMonth else ''),
        '农历': '%s %s[%s]年 %s%s' % (a.lunarYearCn, a.year8Char, a.chineseYearZodiac, a.lunarMonthCn, a.lunarDayCn),
        '星期': a.weekDayCn,
        # 未增加除夕
        '今日节日': (a.get_legalHolidays(), a.get_otherHolidays(), a.get_otherLunarHolidays()),
        '八字': ' '.join([a.year8Char, a.month8Char, a.day8Char, a.twohour8Char]),
        '今日节气': a.todaySolarTerms,
        '下一节气': (a.nextSolarTerm, a.nextSolarTermDate, a.nextSolarTermYear),
        '今年节气表': a.thisYearSolarTermsDic,
        '季节': a.lunarSeason,

        '今日时辰': a.twohour8CharList,
        '时辰凶吉': a.get_twohourLuckyList(),
        '生肖冲煞': a.chineseZodiacClash,
        '星座': a.starZodiac,
        '星次': a.todayEastZodiac,

        '彭祖百忌': a.get_pengTaboo(),
        '彭祖百忌精简': a.get_pengTaboo(long=4, delimit='<br>'),
        '十二神': a.get_today12DayOfficer(),
        '廿八宿': a.get_the28Stars(),

        '今日三合': a.zodiacMark3List,
        '今日六合': a.zodiacMark6,
        '今日五行': a.get_today5Elements(),

        '纳音': a.get_nayin(),
        '九宫飞星': a.get_the9FlyStar(),
        '吉神方位': a.get_luckyGodsDirection(),
        '今日胎神': a.get_fetalGod(),
        '神煞宜忌': a.angelDemon,
        '今日吉神': a.goodGodName,
        '今日凶煞': a.badGodName,
        '宜忌等第': a.todayLevelName,
        '宜': a.goodThing,
        '忌': a.badThing,
        '时辰经络': a.meridians
    }
    return str(dic)

if __name__ == "__main__":
    #host
    mcp.settings.host="localhost"
    mcp.run(transport="sse")
    logger.info("启动时间测试项 Start time serverDemo through MCP") # 记录服务启动日志
    #mcp.run(transport="stdio") #运行状态