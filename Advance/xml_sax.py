"""
2019.11.27 15:45
XML 解析
1. SAX (simple API for XML )
Python 标准库包含 SAX 解析器，SAX 用事件驱动模型，
通过在解析 XML 的过程中触发一个个的事件并调用用户定义的回调函数来处理 XML 文件。

# 创建一个新的解析器对象并返回
xml.sax.make_parser( [parser_list] )
    parser_list - 可选参数，解析器列表

# 创建一个 SAX 解析器并解析xml文档
xml.sax.parse( xmlfile, contenthandler[, errorhandler])
    xmlfile - xml文件名
    contenthandler - 必须是一个 ContentHandler 的对象
    errorhandler - 如果指定该参数，errorhandler 必须是一个 SAX ErrorHandler 对象

# 创建一个 XML 解析器并解析 xml 字符串
xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
    xmlstring - xml字符串
    contenthandler - 必须是一个 ContentHandler 的对象
    errorhandler - 如果指定该参数，errorhandler 必须是一个 SAX ErrorHandler对象

2. DOM(Document Object Model)
将 XML 数据在内存中解析成一个树，通过对树的操作来操作 XML

3. ElementTree

*****Movie*****
Title: Enemy Behind
Type: War, Thriller
Format: DVD
Year: 2003
Rating: PG
Stars: 10
Description: Talk about a US-Japan war
*****Movie*****
Title: Transformers
Type: Anime, Science Fiction
Format: DVD
Year: 1989
Rating: R
Stars: 8
Description: A schientific fiction
*****Movie*****
Title: Trigun
Type: Anime, Action
Format: DVD
Rating: PG
Stars: 10
Description: Vash the Stampede!
*****Movie*****
Title: Ishtar
Type: Comedy
Format: VHS
Rating: PG
Stars: 2
Description: Viewable boredom
"""

# #!/usr/bin/python3

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")
