# -*- coding: utf-8 -*-

import os
import sys
import qrcode
from PIL import Image


prefix = 'http://litaotao.github.io/'


def gen_all_posts_with_icon():
    '''
    '''
    qr = qrcode.QRCode(version = 2, box_size = 5, 
                       error_correction=qrcode.constants.ERROR_CORRECT_Q)
    for i in os.listdir('.'):
        if not os.path.isdir(i):
            continue
        for post in os.listdir(i):
            post = post.split('.')[0]
            qr.add_data(prefix + post)
            # try:
            #     qr.make(fit = True)
            # except:
            #     print 'qr.make(fit = True) failed ...'
            try:
                qr.make()
            except:
                print 'qr.make() also failed , continue to next one '
                print 'failed for {} '.format(post)
                continue
            
            img = qr.make_image()
            
            img = img.convert("RGBA")
            img_w, img_h = img.size
            factor = 3
            size_w, size_h = int(img_w / factor), int(img_h / factor)
            
            icon = Image.open("../images/2.png")
            icon_w, icon_h = icon.size
            icon_w = size_w if icon_w > size_w else icon_w
            icon_h = size_h if icon_h > size_h else icon_h
            icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

            w = int((img_w - icon_w) / 2)
            h = int((img_h - icon_h) / 2)
            # img.paste(icon, (w, h), mask=icon)
            img.paste(icon, (w, h))
            img.save("../images/share/{}.jpg".format(post))
            print 'generate share code for: ' + post + ' success'


def gen_all_posts():
    '''
    '''
    all_posts = []
    # qr = qrcode.QRCode(version = 3, box_size=5)
    for i in os.listdir('.'):
        if not os.path.isdir(i):
            continue
        for post in os.listdir(i):
            url = prefix + post[11:].split('.')[0]
            img = qrcode.make(url, version = 1, box_size = 5)
            # img.resize(200, 200)
            img.save("../images/share/{}.jpg".format(post))
            print 'generate share code for: ' + post + ' success at: ' + url
            

def insert_qrcode_into_blog():
    '''
    '''
    template = """\n\n## 扫一扫     \n\n![{}](../../images/share/{}.jpg)"""

    for i in os.listdir('.'):
        if not os.path.isdir(i):
            continue
        for post in os.listdir(i):
            content = template.format(post, post)
            tmp = file('{}/{}'.format(i, post), 'a')
            tmp.write(content)
            tmp.close()     
            
            print 'insert_qrcode_into_blog {}/{} done ...'.format(i, post)
            # return 

def remove_qrcode_from_blog():
    pass


def main():
    gen_all_posts()
    # insert_qrcode_into_blog()


if __name__ == '__main__':
    main()
