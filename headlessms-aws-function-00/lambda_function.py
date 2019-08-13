import json,sys,uuid,importlib
from base64 import b64decode
from selenium import webdriver

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

    moduleName = str(uuid.uuid4())

    with open('/tmp/%s.py' % moduleName, mode='w') as f:
        if event.get('viaRestApi','') == True:
            f.write(b64decode(event['body']).decode())
        else:
            f.write(event['body'])

    sys.path.insert(0, '/tmp/')
    module = importlib.import_module(moduleName)

    return(return200(module.scrape_process(driver)))