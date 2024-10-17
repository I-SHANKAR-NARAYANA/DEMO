import pip

if 'requests' in [i.project_name for i in pip.get_installed_distributions()]:
    print("requests is installed")
else:
    print("requests is not installed")
# import pyperclip
# import requests

# tt = requests.get('https://i-shankar-narayana.github.io/DEMO/babbel/2.txt').text
# ct = ''
# for char in tt:
#     ct += chr((ord(char) - 24) % 256)

# pyperclip.copy(ct)