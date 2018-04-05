import requests
import os

file_url = 'https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war'

os.chdir('./dnld')

r = requests.get(file_url)

with open("sample.war", "wb") as code:

    code.write(r.content)
