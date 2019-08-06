import json,sys
from base64 import b64decode
from selenium import webdriver
from subprocess import call 

def lambda_handler(event, context):

    global driver
    options = webdriver.ChromeOptions()
    options.binary_location = "/opt/python/bin/headless-chromium"
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--single-process")
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome("/opt/python/bin/chromedriver",chrome_options=options)

    def return200(res_body):
        return{
            'statusCode': 200,
            'body': res_body
        }

    with open('/tmp/func.py', mode='w') as f:
        if event.get('viaRestApi','') == True:
            f.write(b64decode(event['body']).decode())
        else:
            f.write(event['body'])

    sys.path.insert(0, '/tmp/')
    import func
    call('rm -rf /tmp/*', shell=True)

    return(return200(func.scrape_process(driver)))