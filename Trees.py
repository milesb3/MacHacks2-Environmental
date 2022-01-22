import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlencode
import shutil
import json
import time
import urllib.parse
import requests
import os
print("os imported")
print(os.getcwd())
os.chdir(r"C:\Users\pianb\Downloads\Trees\emerald ash boar")
print(os.getcwd())
class Tree(scrapy.Spider):
    name = "Tree"
    custom_settings = {
        "DOWNLOAD_DELAY":3
    }
    base_url = 'https://www.google.com/_/VisualFrontendUi/data/batchexecute?'
    #rpcids=HoAMBc&f.sid=4963449732369334386&bl=boq_visualfrontendserver_20220120.09_p1&hl=en&authuser=0&soc-app=162&soc-platform=1&soc-device=1&_reqid=236642&rt=c
    params={"rpcids":"HoAMBc","f.sid":"4963449732369334386","bl":"boq_visualfrontendserver_20220120.09_p1", "hl":"en","authuser":"0","soc-app":"162","soc-platform":"1","soc-device":"1","_reqid":"236642","rt":"c"}
    def start_requests(self):
        url = self.base_url+urlencode(self.params)
        yield scrapy.Request(
            url=url,
            callback=self.parse_page
        )
    def parse_page(self, response):
        json_data = json.load(response)
        print("This is my json data",json_data)
#            filename = ("Dog"+str(time.time())+".jpg")
#            print("fileName: ", filename)
#            r = requests.get(x, stream=True)
#            r.raw.decode_content = True
#            with open(filename, 'w+b') as f:
#                print(os.getcwd())
#                shutil.copyfileobj(r.raw, f)
#        self.params["after"] = json_data["token"]
#        self.params["dist"] = json_data["dist"]
#        url = self.base_url+urlencode(self.params)
#        print("\n\n\n\n\n\n\n\n\n next page")
#        print(url)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(Tree)
    process.start()