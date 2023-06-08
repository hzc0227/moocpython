# -*- coding: utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/6/8 16:31
# @File:     vocal_top_stories.py
# @Software: PyCharm


import requests
from lxml import etree

headers = {
    "authority": "vocal.media",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
cookies = {
    "_gcl_au": "1.1.457186777.1686209690",
    "_scid": "eb49eddc-62cc-4f0b-8750-ba129b34262b",
    "ln_or": "eyI5NzE5MDYiOiJkIn0^%^3D",
    "gtm_p6_ip": "122.193.105.210",
    "gtm_p6_country_code": "cn",
    "gtm_p6_country": "ff2082aa78aea80a27cb4fb91f0350153702c16dce790a77f0bb0bfbf6899977",
    "gtm_p6_st": "f086f5030a840e3bd127f4497a7529a41a87ff7d89008524e495e981c0ec5a5d",
    "gtm_p6_ct": "8337d58da000fb60ed56ddcf2a0ad8e915f7a26e3846967b045a5016d7137ffa",
    "gtm_p6_s_id": "54318187",
    "_hp2_ses_props.2787354530": "^%^7B^%^22ts^%^22^%^3A1686209690139^%^2C^%^22d^%^22^%^3A^%^22vocal.media^%^22^%^2C^%^22h^%^22^%^3A^%^22^%^2F^%^22^%^7D",
    "authenticatedUser": "aRZ32pBUJIfBs4oY_7_JXaB1glZoWyek.Oij6OCKJTvg5732JSPN2NS19Vqvmz3Jn1l80eVCuTCQ",
    "keystone.sid": "s^%^3AaRZ32pBUJIfBs4oY_7_JXaB1glZoWyek.Oij6OCKJTvg5732JSPN2NS19Vqvmz3Jn1l80eVCuTCQ",
    "_gid": "GA1.2.1638244523.1686209746",
    "_gaexp": "GAX1.2.rtGmtYnbQLCpF9xz9xin8w.19578.1",
    "_screload": "1",
    "_rdt_uuid": "1686209746942.ccf23055-0afe-448e-9b14-e8e32a78499b",
    "_fbp": "fb.1.1686209747043.1880365170",
    "_tt_enable_cookie": "1",
    "_ttp": "YxBh7sLQn8e1IsOuklsPojYmOfb",
    "_pin_unauth": "dWlkPU5UVmxNak5tTm1VdE1UZGlZUzAwTURka0xXSmpNalV0TURJME56UmhZMkV6TXpFMg",
    "_sctr": "1^%^7C1686153600000",
    "AWSALB": "sfeBxr7jGClwazzihxxC90Sn4rM/WdG7s8Ag+PKLNlkacpXOo4rubqiVxo/MRx3N1CiJNGcExgTSxJ3tffKCBRoCQ7BxNUETZKLopkESEI0u1tU7D5++FDTdAG0A",
    "AWSALBCORS": "sfeBxr7jGClwazzihxxC90Sn4rM/WdG7s8Ag+PKLNlkacpXOo4rubqiVxo/MRx3N1CiJNGcExgTSxJ3tffKCBRoCQ7BxNUETZKLopkESEI0u1tU7D5++FDTdAG0A",
    "_uetsid": "f3ebf36005ce11eeb94d51dbcd16f37e",
    "_uetvid": "f3ec156005ce11ee95b8a9e1fc752da8",
    "_scid_r": "eb49eddc-62cc-4f0b-8750-ba129b34262b",
    "_ga": "GA1.2.1234848006.1686209691",
    "_dc_gtm_UA-45589719-1": "1",
    "_hp2_id.2787354530": "^%^7B^%^22userId^%^22^%^3A^%^228852892958024719^%^22^%^2C^%^22pageviewId^%^22^%^3A^%^223743973014770390^%^22^%^2C^%^22sessionId^%^22^%^3A^%^221719651432570080^%^22^%^2C^%^22identity^%^22^%^3A^%^22b1b0f0d8-71d9-4f75-976e-9783f7d272dc^%^22^%^2C^%^22trackerVersion^%^22^%^3A^%^224.0^%^22^%^2C^%^22identityField^%^22^%^3Anull^%^2C^%^22isIdentified^%^22^%^3A1^%^7D",
    "gtm_p6_eid": "null",
    "_ga_YP3PPMLHFE": "GS1.1.1686209690.1.1.1686212929.40.0.0"
}
url = "https://vocal.media/top-stories?page="
with open('.\stories.txt', 'a+') as f:
    for i in range(10):
        response = requests.get(url + str(i), headers=headers, cookies=cookies)
        if response and response.status_code == 200:
            html = etree.HTML(response.text)
            headlines = html.xpath('//h2[@class="post-name css-1alfqzo-Text"]')
            for headline in headlines:
                try:
                    headline.text.encode('utf-8')
                    print(headline.text)
                    f.write(headline.text + '\n')
                except Exception:
                    pass
