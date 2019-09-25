# -*- coding:utf-8 -*-
import os
import re
import requests
from lxml import etree
from queue import Queue
from threading import Thread
from fontTools.ttLib import TTFont
import fontTools.ttLib


class Dianping_Spider(object):
    def __init__(self):
        self.proxies = {
            'http': 'http:/180.126.201.139:21449',
            'https': 'https://180.126.201.139:21449'
        }
        self.url = 'http://www.dianping.com/guangzhou/ch10/r30509p{}'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'navCtgScroll=200; showNav=#nav-tab|0|0; showNav=#nav-tab|0|0; navCtgScroll=100; _lxsdk_cuid=16cc829e244bc-0127189c8ba4d2-c343162-144000-16cc829e245c8; _lxsdk=16cc829e244bc-0127189c8ba4d2-c343162-144000-16cc829e245c8; _hc.v=cb43b207-95b2-19e1-1f2f-32ff66fe3ed1.1566726284; s_ViewType=10; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; thirdtoken=7b20f866-cfcb-460f-9978-5b7c5efe1a60; ua=dpuser_0388174498; ctu=ab489bae698ec8f8941b6e1f06135f9772ab4d226e82a0f9d51191081b5bbc65; cy=7; cye=shenzhen; _lxsdk_s=16cdcbae397-1c1-a32-8e0%7C%7C21',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}  # 请求头
        self.headers02 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}  # 字体请求头
        self.woff_name = []  # 字体名称
        self.woffs_link = []  # 字体链接
        self.q = Queue()  # url线程池
        self.get_num = {}  # 实际的 数字对照表 unicode：汉字
        self.get_tag = {}  # 实际的 招牌菜等 unicode：汉字
        self.get_address = {}  # 实际的 地址的 unicode：汉字
        self.var01 = 1
        self.var02 = 1
        self.var03 = 1
        self.i = 1

    def start_url(self):
        for index in range(1, 10):
            url = self.url.format(index)
            self.q.put(url)

    def get_page(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                res = requests.get(url, headers=self.headers)

                print("请求%s次" % self.i)
                res.encoding = 'utf-8'
                html = res.text
                self.parse_html(html)
                self.replace_str(html)
            else:
                break

    def parse_html(self, html):
        # 获取字体链接
        svgtextcss = re.search(r'href="([^"]+svgtextcss[^"]+)"', html, re.S)
        svgtext = requests.get(url=('http:' + svgtextcss.group(1)), headers=self.headers02)

        # 正则取字体链接
        woff_urls = re.findall(r'url\("//(.*?)"\)', svgtext.text)
        woff_url_list = []
        for woff_url in woff_urls:
            # 将不存在列表的字体链接添加到列表 self.woffs_link
            if woff_url not in self.woffs_link and '.woff' in woff_url:
                woff_url = 'http://' + woff_url
                self.woffs_link.append(woff_url)
                woff_url_list.append(woff_url)
            else:
                pass

        print(self.woffs_link)
        print(woff_url_list)

        self.download_num_woff(woff_url_list)
        self.download_tag_woff(woff_url_list)
        self.download_address_woff(woff_url_list)
        self.i += 1

    def base_font(self):

        base_font = TTFont('base.woff')  # 打开本地字体文件01.ttf
        base_obj_list = base_font.getGlyphNames()[1:-1]  # 获取所有字符的对象，去除第一和最后
        base_uni_list = base_font.getGlyphOrder()[2:]  # 获取所有编码，去除前2个

        font_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '店', '中', '美', '家', '馆', '小', '车', '大', '市', '公',
                     '酒',
                     '行', '国', '品', '发', '电', '金', '心', '业', '商', '司', '超', '生', '装', '园', '场', '食', '有', '新', '限', '天',
                     '面',
                     '工', '服', '海', '华', '水', '房', '饰', '城', '乐', '汽', '香', '部', '利', '子', '老', '艺', '花', '专', '东', '肉',
                     '菜',
                     '学', '福', '饭', '人', '百', '餐', '茶', '务', '通', '味', '所', '山', '区', '门', '药', '银', '农', '龙', '停', '尚',
                     '安',
                     '广', '鑫', '一', '容', '动', '南', '具', '源', '兴', '鲜', '记', '时', '机', '烤', '文', '康', '信', '果', '阳', '理',
                     '锅',
                     '宝', '达', '地', '儿', '衣', '特', '产', '西', '批', '坊', '州', '牛', '佳', '化', '五', '米', '修', '爱', '北', '养',
                     '卖',
                     '建', '材', '三', '会', '鸡', '室', '红', '站', '德', '王', '光', '名', '丽', '油', '院', '堂', '烧', '江', '社', '合',
                     '星',
                     '货', '型', '村', '自', '科', '快', '便', '日', '民', '营', '和', '活', '童', '明', '器', '烟', '育', '宾', '精', '屋',
                     '经',
                     '居', '庄', '石', '顺', '林', '尔', '县', '手', '厅', '销', '用', '好', '客', '火', '雅', '盛', '体', '旅', '之', '鞋',
                     '辣',
                     '作', '粉', '包', '楼', '校', '鱼', '平', '彩', '上', '吧', '保', '永', '万', '物', '教', '吃', '设', '医', '正', '造',
                     '丰',
                     '健', '点', '汤', '网', '庆', '技', '斯', '洗', '料', '配', '汇', '木', '缘', '加', '麻', '联', '卫', '川', '泰', '色',
                     '世',
                     '方', '寓', '风', '幼', '羊', '烫', '来', '高', '厂', '兰', '阿', '贝', '皮', '全', '女', '拉', '成', '云', '维', '贸',
                     '道',
                     '术', '运', '都', '口', '博', '河', '瑞', '宏', '京', '际', '路', '祥', '青', '镇', '厨', '培', '力', '惠', '连', '马',
                     '鸿',
                     '钢', '训', '影', '甲', '助', '窗', '布', '富', '牌', '头', '四', '多', '妆', '吉', '苑', '沙', '恒', '隆', '春', '干',
                     '饼',
                     '氏', '里', '二', '管', '诚', '制', '售', '嘉', '长', '轩', '杂', '副', '清', '计', '黄', '讯', '太', '鸭', '号', '街',
                     '交',
                     '与', '叉', '附', '近', '层', '旁', '对', '巷', '栋', '环', '省', '桥', '湖', '段', '乡', '厦', '府', '铺', '内', '侧',
                     '元',
                     '购', '前', '幢', '滨', '处', '向', '座', '下', '県', '凤', '港', '开', '关', '景', '泉', '塘', '放', '昌', '线', '湾',
                     '政',
                     '步', '宁', '解', '白', '田', '町', '溪', '十', '八', '古', '双', '胜', '本', '单', '同', '九', '迎', '第', '台', '玉',
                     '锦',
                     '底', '后', '七', '斜', '期', '武', '岭', '松', '角', '纪', '朝', '峰', '六', '振', '珠', '局', '岗', '洲', '横', '边',
                     '济',
                     '井', '办', '汉', '代', '临', '弄', '团', '外', '塔', '杨', '铁', '浦', '字', '年', '岛', '陵', '原', '梅', '进', '荣',
                     '友',
                     '虹', '央', '桂', '沿', '事', '津', '凯', '莲', '丁', '秀', '柳', '集', '紫', '旗', '张', '谷', '的', '是', '不', '了',
                     '很',
                     '还', '个', '也', '这', '我', '就', '在', '以', '可', '到', '错', '没', '去', '过', '感', '次', '要', '比', '觉', '看',
                     '得',
                     '说', '常', '真', '们', '但', '最', '喜', '哈', '么', '别', '位', '能', '较', '境', '非', '为', '欢', '然', '他', '挺',
                     '着',
                     '价', '那', '意', '种', '想', '出', '员', '两', '推', '做', '排', '实', '分', '间', '甜', '度', '起', '满', '给', '热',
                     '完',
                     '格', '荐', '喝', '等', '其', '再', '几', '只', '现', '朋', '候', '样', '直', '而', '买', '于', '般', '豆', '量', '选',
                     '奶',
                     '打', '每', '评', '少', '算', '又', '因', '情', '找', '些', '份', '置', '适', '什', '蛋', '师', '气', '你', '姐', '棒',
                     '试',
                     '总', '定', '啊', '足', '级', '整', '带', '虾', '如', '态', '且', '尝', '主', '话', '强', '当', '更', '板', '知', '己',
                     '无',
                     '酸', '让', '入', '啦', '式', '笑', '赞', '片', '酱', '差', '像', '提', '队', '走', '嫩', '才', '刚', '午', '接', '重',
                     '串',
                     '回', '晚', '微', '周', '值', '费', '性', '桌', '拍', '跟', '块', '调', '糕']
        base_dict = {}
        for k, v in zip(base_uni_list, font_char):
            base_dict[k] = v

        return base_dict, base_font, base_uni_list

    def download_num_woff(self, woff_url_list):
        base_dict, base_font, base_uni_list = self.base_font()
        for index in range(3, 0, -1):
            woff_url = woff_url_list[index]
            woff_name = woff_url.split('/')[-1]

            if not os.path.exists(woff_name):
                # 如果字体文件不存在，则下载 并执行下面的操作
                woff_content = requests.get(woff_url, headers=self.headers02).content
                with open(woff_name, 'wb') as f:
                    f.write(woff_content)
                    print(woff_name + '下载成功')

                    new_font = TTFont(woff_name)  # 打开访问网页新获得的字体文件02.ttf

                    obj_list2 = new_font.getGlyphNames()[1:-1]
                    uni_list2 = new_font.getGlyphOrder()[2:]
                    for uni1 in base_uni_list:
                        obj1 = base_font['glyf'][uni1]

                        for uni2 in uni_list2:
                            obj2 = new_font['glyf'][uni2]

                            if obj1 == obj2:
                                self.get_num[uni2] = base_dict[uni1]
            else:
                pass

        print('我是获取数字的哦', self.get_num)

    def download_tag_woff(self, woff_url_list):
        if self.var01 == 1:
            base_dict, base_font, base_uni_list = self.base_font()
            for index in range(3, -1, -1):
                if index != 2:
                    woff_url = woff_url_list[index]
                    woff_name = woff_url.split('/')[-1]

                    new_font = TTFont(woff_name)  # 打开访问网页新获得的字体文件02.ttf
                    obj_list2 = new_font.getGlyphNames()[1:-1]
                    uni_list2 = new_font.getGlyphOrder()[2:]
                    for uni1 in base_uni_list:
                        obj1 = base_font['glyf'][uni1]

                        for uni2 in uni_list2:
                            obj2 = new_font['glyf'][uni2]

                            if obj1 == obj2:
                                self.get_tag[uni2] = base_dict[uni1]
                else:
                    pass

            self.var01 += 1
        else:
            pass

        print('我是获取菜馆格式的哦', self.get_tag)

    def download_address_woff(self, woff_url_list):
        if self.var02 == 1:
            base_dict, base_font, base_uni_list = self.base_font()
            for index in range(1, 4):
                woff_url = woff_url_list[index]
                woff_name = woff_url.split('/')[-1]

                new_font = TTFont(woff_name)  # 打开访问网页新获得的字体文件02.ttf
                obj_list2 = new_font.getGlyphNames()[1:-1]
                uni_list2 = new_font.getGlyphOrder()[2:]
                for uni1 in base_uni_list:
                    obj1 = base_font['glyf'][uni1]

                    for uni2 in uni_list2:
                        obj2 = new_font['glyf'][uni2]

                        if obj1 == obj2:
                            self.get_address[uni2] = base_dict[uni1]
            self.var02 += 1
        else:
            pass

        print('我是获取店铺地址的哦', self.get_address)

    def replace_str(self, html):
        # 获取所有需要修改的字体 unicode

        tag_html = html
        html_unicode = re.findall('&#x(.*?);</svgmtsi>', tag_html, re.S)

        for string in html_unicode:
            char_string = 'uni' + string
            html_string = '&#x' + string
            tag_html = tag_html.replace(html_string, self.get_tag[char_string])

        num_html = html
        html_unicode = re.findall('&#x(.*?);</svgmtsi>', num_html, re.S)
        for string in html_unicode:
            char_string = 'uni' + string
            html_string = '&#x' + string
            num_html = num_html.replace(html_string, self.get_tag[char_string])

        address_html = html
        html_unicode = re.findall('&#x(.*?);</svgmtsi>', address_html, re.S)
        for string in html_unicode:
            char_string = 'uni' + string
            html_string = '&#x' + string
            address_html = address_html.replace(html_string, self.get_tag[char_string])

        title = re.findall('data-name="(.*?)">.*?', tag_html, re.S)

        parse_html = etree.HTML(address_html)
        # 获取价格
        price_list = parse_html.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[2]/a[2]//b//text()')

        x = ''
        for price in price_list:
            if ";" in price:
                x += price[0]
            else:
                x += price
        # print(x.split('￥')[1:])

        address = re.findall('data-address="(.*?)" data-sname.*?', tag_html, re.S)

        sign = re.findall('target="_blank">(.*?)</a>.*?', tag_html, re.S)

        index = 0
        signs = []
        for i in range(15):
            signs.append(sign[:45][index:index + 3])
            index += 3

        types = re.findall('shop_tag_cate_click"(.*?)</span></a>', tag_html, re.S)

        type = []
        for i in types:
            t = re.sub('[1234567890 \<\>;qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.\/\--="_]', '', i)
            type.append(t)

        comment = re.findall('list-readreview.*?<b>(.*?)</b>.*?条点评</a>.*?', address_html, re.S)
        comments = []
        for i in comment:
            comments.append(re.sub('[\<\>\/svgmtsi ;class="shopNum"]', '', i))

        for t, n, p, d, s, c in zip(type, title, x.split('￥')[1:], address, (signs), comments):
            print('type:%s  title:%s  price:%s  address:%s  sign:%s  comment:%s  ' % (t, n, p, d, s, c))

    def main(self):

        self.start_url()
        self.get_page()

        t_list = []
        for i in range(10):
            t = Thread(target=self.get_page)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()


if __name__ == '__main__':
    spider = Dianping_Spider()
    spider.main()
