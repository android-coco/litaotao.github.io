# -*- coding: utf-8 -*-

import os
import sys
import qrcode


prefix = 'http://litaotao.github.io/'


def gen_all_posts():
	'''
	'''
	all_posts = []
	qr = qrcode.QRCode(box_size=5)
	for i in os.listdir('.'):
		if not os.path.isdir(i):
			continue
		for post in os.listdir(i):
			# post = post[11:]
			post = post.split('.')[0]
			url = prefix+post
			f = open(post+'.jpg', 'wb')
			img = qrcode.make(url)
			img.save(f)
			f.close()
			# qr.add_data(url)
			# qr.make(fit=True)
			# img = qr.make_image()
			# img.save(post + '.jpg')
			print 'generate share code for: ' + post + ' success at: ' + url
			os.system('mv {} ../images/share/'.format(post+'.jpg'))


def insert_qrcode_into_blog():
	'''
	'''
	template = """\n\n**扫一扫从手机上打开**\n![{}](../../images/share/{}.jpg)"""

	for i in os.listdir('.'):
		if not os.path.isdir(i):
			continue
		# print i
		for post in os.listdir(i):
			name = post.split('.')[0]
			content = template.format(name, name)
			tmp = file('{}/{}'.format(i, post), 'a')
			tmp.write(content)
			tmp.close()		


def main():
	gen_all_posts()
	# insert_qrcode_into_blog()


if __name__ == '__main__':
	main()