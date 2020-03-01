import platform
from subprocess import *

libs = ( 
	'termcolor',
	'selenium', 
	'beautifulsoup4'
)

if platform.system() == 'Windows':
	for x in libs:
		Popen(('pip install %s' % x))
else:
	for x in libs:
		Popen(('pip3 install %s' % x))