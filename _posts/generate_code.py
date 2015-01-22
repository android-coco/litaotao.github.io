# -*- coding: utf-8 -*-

import os
import sys
import qrcode


prefix = 'http://litaotao.github.io/'


def gen_all_posts():
	'''
	'''
	all_posts = []
	for i in os.listdir('.'):
		if not os.path.isdir(i):
			continue
		for post in os.listdir(i):
			post = post[11:]
			post = post.split('.')[0]
			url = prefix+post
			f = open(post+'.jpg', 'wb')
			img = qrcode.make(url)
			img.save(f)
			f.close()
			print 'generate share code for: ' + post + ' success at: ' + url
			os.system('mv {} ../images/share/'.format(post+'.jpg'))


def main():
	gen_all_posts()


if __name__ == '__main__':
	main()