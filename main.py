import requests,time,random,argparse,string,threading
from fake_useragent import UserAgent


password = "ffffffffffff"
url = "https://www.instagram.com/accounts/login/ajax/"

class Check_user:
    def __init__(self):
        self.command()
        self.run()
    def run(self):
        while True:
            try:
                ran_user = ''.join(random.choices(string.ascii_letters + string.digits + "_" + ".", k=self.r))
                headers = {
                    "accept-encoding": "gzip, deflate, br",
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
                data = {
                    "username": ran_user,
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1677354480:{password}",
                    "queryParams": "{}",
                    "optIntoOneTap": "false",
                    "trustedDeviceRecords": "{}",
                }

                req = requests.post(url, headers=headers, data=data, timeout=int(self.w))
                webpage = req.text
                if '"user":true' in webpage:
                    print(f"User '{ran_user}' is not found")
                    time.sleep(random.uniform(1, 3))
                elif '"message":"Sorry, your password was incorrect. Please double-check your password."' in webpage:
                    print(f"User '{ran_user}' is found")
                    time.sleep(random.uniform(1, 3))
                else:
                    print(f"Instagram website may have blocked you: {req.status_code, webpage}")
                    time.sleep(random.uniform(3.5, 4.5))
            except (requests.exceptions.Timeout, TimeoutError) as T:
                print(f"Timeout: {T}")
                time.sleep(random.uniform(3.5, 4.5))
            except ConnectionError as C:
                print(f"Connection Error: {C}")
                time.sleep(random.uniform(3.5 , 4.5))
            except Exception as e:
                print(f"Instagram website may have blocked you: {e}")
                time.sleep(random.uniform(3.5, 4.5))

    # commands
    def command(self):
        parser = argparse.ArgumentParser(description="Reads the commands and works accordingly")
        parser.add_argument("-r", metavar="range user", type=int, default="5")
        parser.add_argument("-w", metavar="wait time", type=float, default="2.5")
        parser.add_argument("-t", metavar="threading", type=int, default="1")
        args = parser.parse_args()
        self.r = args.r
        self.w = args.w
        self.t = args.t

if __name__ == "__main__":
    run = Check_user()



