# -*- coding: utf-8 -*-

# 循环周期 秒
CYCLE = 10

# 数据库配置
DB_PARAMS = {
    'host': '',
    'port': 3306,
    'user': '',
    'passwd': '',
    'db': '',
    'charset': 'utf8',
}

# 订单签收历史数据周期 天数
TRACKING_CYCLE = 90

# 追踪状态 已完成
TRACKING_STATUS = 2

# 图片存储路径
STORAGE_DIR = 'F:\\screen_shot\\'

# 截图处理类
SCREENSHOTS_DICT = {
    # 'aupost': 'AuPostShots',
    # 'depost': 'DePostShots',
    # 'dhl': 'DHLShots',
    # 'dhl(de)': 'DHLDEShots',
    # 'dpd': 'DPDShots',
    # 'dpd(uk)': 'DPDUKShots',
    # 'ems': 'EMSShots',  # 验证码
    # 'fedex': 'FedexShots',
    # 'p2p': 'P2PShots',
    # 'parcelforce': 'ParcelForceShots',
    # 'royalmail': 'RoyalMailShots',  # 无法搜索
    # 'tnt': 'TNTShots',
    # 'toll': 'TollShots',
    # 'ups': 'UPSShots',
    # 'usps': 'USPSShots',
    # 'yodel': 'YodelShots',  # 无法访问
}

# 承运商
CARRIER_SITE_DICT = {
    # 'aupost': 'https://auspost.com.au/mypost/track/#/details/%s',
    # 'depost': 'https://www.deutschepost.de/sendung/simpleQuery.html?locale=en_GB',
    # 'dhl': 'http://www.cn.dhl.com/zh/express/tracking.html?AWB=%s&brand=DHL',
    # 'dhl(de)': 'https://nolp.dhl.de/nextt-online-public/en/search?piececode=%s&cid=dhlde',
    # 'dpd': 'https://tracking.dpd.de/status/en_US/parcel/%s',
    # 'dpd(uk)': 'https://www.dpd.co.uk/apps/tracking/?reference=%s&postcode=#results',
    # 'ems': 'http://www.ems.com.cn/mailtracking/you_jian_cha_xun.html',  # 验证码
    # 'fedex': 'https://www.fedex.com/en-cn/home.html',
    # 'p2p': 'http://www.trackmytrakpak.com/?MyTrakPakNumber=%s',
    # 'parcelforce': 'https://tracking.parcelforce.net/Pfw/SNP_login.php?CLIENT=Pfw&CAR=068&COUNTRYCODE=GB&MMITYPE=2&HOME_DISPLAY=complete&NEOPOD_URL=tracking.parcelforce.net&NEOPOD_PROTOCOL=https:&NEOPOD_WEBSITE=https://tracking.parcelforce.net/',
    # 'royalmail': 'https://www.royalmail.com/track-your-item#/',  # 无法搜索
    # 'tnt': 'https://www.tnt.com/express/en_us/site/tracking.html?searchType=con&cons=%s',
    # 'toll': 'https://www.mytoll.com/?externalSearchQuery=%s&op=Search',
    # 'ups': 'https://wwwapps.ups.com/WebTracking/track',
    # 'usps': 'https://tools.usps.com/go/TrackConfirmAction_input',
    # 'yodel': 'http://yodel.co.uk/track/',  # 无法访问
}
