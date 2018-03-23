# -*- coding: utf-8 -*-
import re
import scrapy



class JobbleSpider(scrapy.Spider):


    name = 'jobble'
    allowed_domains = ['blog.jobble.com']   #允许的域名是什么
    start_urls = ['http://blog.jobbole.com/112048/']    #起始的url

    def parse(self, response):

        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]  #标题
        crate_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·','') #创建时间
        parse_num = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]  #点赞数
        print(title,crate_time,parse_num)

        fav_num_data = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0] #未处理的收藏数据
        match_re_fav = re.match(".*(\d+).*",fav_num_data)    #匹配收藏数

        comment_num_data = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0] #未处理的评论数据
        match_re_comment = re.match(".*(\d+).*",comment_num_data)   #匹配评论数

        if match_re_fav: #判断收藏数是否为0
            fav_num = match_re_fav.group()[1]
        else:
            fav_num = 0

        if match_re_comment: #判断收藏数是否为0
            comment_num = match_re_comment.group()[1] # match_re_comment.group() = ' 2 评论'
        else:
            comment_num = 0

        print(fav_num,comment_num)

        #标签
        tag_list_data = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list_data if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)   #生成标签
        print(tags)

        #正文
        context = response.xpath('//div[@class="entry"]').extract()[0]
        print(context)

        pass
