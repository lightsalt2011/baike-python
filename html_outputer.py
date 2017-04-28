# -*- coding: utf-8 -*-
"""
Html输出器
"""
import codecs

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        """
        收集数据
        :param data:
        :return:
        """
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        """
        将收集结果输出成Html页面
        :return:
        """
        #file_out = open('./output/output.html', 'w')
        file_out = codecs.open('./output/output.html', 'a', 'utf-8')
        file_out.write('<html>\n<head>\n')
        file_out.write('<link rel="stylesheet" type="text/css" href="./style.css" />\n')
        file_out.write('</head>\n<body class="g-wrap">\n')
        for data in self.datas:
            file_out.write('<div class="g-info">\n')
           # file_out.writelines('<p class="m-tt"><a target="_blank" href="%s">%s</a></p>\n' %(("").join(data['url']), ("").join(data['title'])))
           # file_out.writelines('<p class="m-tt"><a target="_blank" href="%s">%s</a></p>\n'  %((str(line) for line in data['url']), (str(line) for line in data['title'])))
            #file_out.writelines(['<p class="summary">%s</p>\n' %(str(line) for line in data['summary']), '</div>\n'])
            file_out.write('<p class="m-tt"><a target="_blank" href="%s">%s</a></p>\n' %(data['url'], data['title']))
            file_out.write('<p class="summary">%s</p>\n</div>\n' % data['summary'])
            print type(data['summary'])
        file_out.write('</body>\n</html>')
        file_out.close()
