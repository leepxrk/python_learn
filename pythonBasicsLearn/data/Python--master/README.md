# Python-
获取上交所和深交所所有股票的名称和交易信息  股票数据是进行量化交易的基础型数据，此爬虫也能为量化交易提供获得基础数据的方法
功能描述

目标：获取上交所和深交所所有股票的名称和交易信息

股票数据是进行量化交易的基础型数据，此爬虫也能为量化交易提供获得基础数据的方法

输出：保存到文件中

技术路线：requests‐bs4‐re

候选数据网站的选择

新浪股票：http://finance.sina.com.cn/stock/

百度股票：https://gupiao.baidu.com/stock/

选取原则：股票信息静态存在于HTML页面中，非js代码生成

没有Robots协议限制

选取方法：浏览器 F12，源代码查看等

选取心态：不要纠结于某个网站，多找信息源尝试

数据网站的确定

新浪股票在页面上看到的股票代码在源代码中并没有，说明很可能是由JavaScript脚本生成的；而百度股票的每一支个股的信息都写在HTML代码中

所以对于这两个网站来讲，百度股票更适合作为定向爬虫的数据来源

获取股票列表：

东方财富网：http://quote.eastmoney.com/stocklist.html

获取个股信息：

百度股票：https://gupiao.baidu.com/stock/

单个股票：https://gupiao.baidu.com/stock/sz002439.html

程序的结构设计

步骤1：从东方财富网获取股票列表

步骤2：根据股票列表逐个到百度股票获取个股信息

步骤3：将结果存储到文件

 

百度股票源代码中个股信息的组织形式

所以键值对，用字典类型
