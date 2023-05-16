import scrapy

class DiemThiSpider(scrapy.Spider):
    name = 'diemthi'
    start_number = 51000001
    end_number = 51018632
    start_urls = [
        'https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/{}.html'.format(idx)
        for idx in range(start_number, end_number + 1)
    ]

    def parse(self, response):
        if response.status == 404:
            print("[INFO] {}: no data".format(response.url))
            return

        subjects = {'Toán': '',
                    'Văn': '',
                    'Sử': '',
                    'Địa': '',
                    'Lí': '',
                    'Hóa': '',
                    'Sinh': '',
                    'Ngoại ngữ': '',
                    'GDCD': ''}
        
        candidate_number = response.url.split('/')[-1].split('.')[0]
        subjects['sbd'] = candidate_number

        for row in response.xpath('//div[@class="resultSearch__right"]//tbody/tr'):
            subject = row.xpath('td[1]//text()').get()
            score = row.xpath('td[2]//text()').get()
            if subject in subjects:
                subjects[subject] = score.strip()

        yield subjects
