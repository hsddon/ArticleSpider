from scrapy.cmdline import execute  #通过此函数介意执行scrapy脚本

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobble"])