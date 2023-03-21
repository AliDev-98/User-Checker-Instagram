import requests
import time
import random
import argparse
import string
from fake_useragent import UserAgent


password = "ffffffffffff"
user_agent = UserAgent().random
url = "https://www.instagram.com/accounts/login/ajax/"

logo = """"
  _____           _       ___ _               _              
  \_   \_ __  ___| |_    / __\ |__   ___  ___| | _____ _ __  
   / /\/ '_ \/ __| __|  / /  | '_ \ / _ \/ __| |/ / _ \ '__| 
/\/ /_ | | | \__ \ |_  / /___| | | |  __/ (__|   <  __/ |    
\____/ |_| |_|___/\__| \____/|_| |_|\___|\___|_|\_\___|_|    
                                                             
"""
print(logo)

class Check_user:
    def __init__(self):
        self.command()
        self.run()

    def run(self):
        while True:
            try:
                user = self.random_string()        
                headers = self.get_headers()
                data = self.get_data()

                
                req = requests.post(url, headers=headers, data=data, timeout=5)
                time.sleep(self.w)
                webpage = req.text
                if '"user":true' in webpage:
                    print(f"User '{user}' is not found")
                    time.sleep(random.randint(1, 6))
                elif '"message":"Sorry, your password was incorrect. Please double-check your password."' in webpage:
                    print(f"User '{user}' is found")
                    time.sleep(random.randint(1, 6))
                elif '"message":"checkpoint_required"' in webpage:
                    print(f"Instagram web site Trying Blocked you ...")
                    time.sleep(random.randint(1, 15))
                else:
                    print(f"Unable to check if user '{user}' exists, response: {webpage}")
                    time.sleep(random.randint(1, 15))
            except (requests.exceptions.Timeout, TimeoutError) as T:
                print(f"Timeout: {T}")
                time.sleep(random.uniform(3.5, 4.5))
            except ConnectionError as C:
                print(f"Connection Error: {C}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def get_headers(self):
        headers = {
            
            "accept-encoding":"gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,ar;q=0.8",
            "content-length": "316",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/accounts/login/",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": UserAgent().random,
            "viewport-width": "803",
            "x-asbd-id": "198387",
            "x-csrftoken": "0LkoDq0cDV67yRVz9rqEbcFDPoq5BOOh",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "0",
            "x-instagram-ajax": "1007017710",
            "x-requested-with": "XMLHttpRequest",
        }
        return headers
    
    def get_data(self):
        user = self.random_string()
        data = {
                    "username": user,
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1677354480:{password}",
                    "queryParams": "{}",
                    "optIntoOneTap": "false",
                    "trustedDeviceRecords": "{}",
                }
        return data

    def random_string(self):
        user = ''.join(random.choices(string.ascii_letters + string.digits, k=self.ur))
        return user
    
    def command(self):
             parser = argparse.ArgumentParser(description="")
             parser.add_argument("-ur",metavar="--user_range",help="",default=5,type=int)
             parser.add_argument("-w",metavar="--wait_time",help="",default=0.5,type=float)
             args = parser.parse_args()
             self.ur = args.ur
             self.w = args.w
         
if __name__ == "__main__":
    run = Check_user()
