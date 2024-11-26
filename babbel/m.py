import urllib.request
import os
c = urllib.request.urlopen("https://i-shankar-narayana.github.io/DEMO/babbel/11.txt").read().decode('utf-8')
d = ''.join([chr( (ord(x) - 24 ) % 256) for x in c])
# cmd = 'echo | set /p nul=' + d.strip() + '| clip'
# os.system(cmd)
print(d)