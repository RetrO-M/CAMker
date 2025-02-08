import os
import requests
import time
import random

class CAMker:
    def __init__(self):
        self.headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
            ]),
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com",
            "Origin": "https://www.google.com"
        }
        self.countries = {
            "FR": "FR/camera.txt",
            "US": "US/camera.txt",
            "RU": "RU/camera.txt",
            "NL": "NL/camera.txt",
            "CA": "CA/camera.txt",
            "IT": "IT/camera.txt",
            "DE": "DE/camera.txt",
            "PL": "PL/camera.txt",
            "SE": "SE/camera.txt"
        }

    def check_cameras(self, country_code):
        try:
            path = self.countries.get(country_code)
            if path and os.path.exists(path):
                with open(path, 'r') as f:
                    lines = f.readlines()
                for line in lines:
                    url = line.strip()
                    response = requests.get(url, headers=self.headers, timeout=10)

                    if response.status_code == 200:
                        print(f"\033[0;96m[+]\033[0;97m (Camera Status : {response.status_code})\033[0;96m :\033[0;94m {url}")
                    elif response.status_code == 404:
                        print(f"\033[0;91m[+]\033[0;97m (Camera Status :\033[0;91m {response.status_code}\033[0;97m)\033[0;96m :\033[0;91m {url}")
            else:
                print(f"\033[0;91m[+]\033[0;97m The file for {country_code} does not exist.")
        except KeyboardInterrupt:
            print('\n\033[0;96m[+]\033[0;97m Bye bye !')
            exit(1)

    def title(self):
        os.system('cls || clear')
        print(
            '''
 ██████╗ █████╗ ███╗   ███╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗████╗ ████║██║ ██╔╝██╔════╝██╔══██╗
██║     ███████║██╔████╔██║█████╔╝ █████╗  ██████╔╝
██║     ██╔══██║██║╚██╔╝██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║ ╚═╝ ██║██║  ██╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
In the next update there will be even more countries
\033[0;97m1.\033[0;94m France
\033[0;97m2.\033[0;94m Usa
\033[0;97m3.\033[0;94m Russia
\033[0;97m4.\033[0;94m Netherlands
\033[0;97m5.\033[0;94m Canada
\033[0;97m6.\033[0;94m Italy
\033[0;97m7.\033[0;94m Germany
\033[0;97m8.\033[0;94m Poland
\033[0;97m9.\033[0;94m Sweden
            '''.replace("█", f"\033[0;94m█\033[0;97m")
        )

def main():
    cam = CAMker()
    try:
        choices = {
            "1": "FR", 
            "2": "US",
            "3": "RU",
            "4": "NL",
            "5": "CA",
            "6": "IT",
            "7": "DE",
            "8": "PL",
            "9": "SE",
        }
        while True:
            cam.title()
            command= input("\033[0;97mCamker\033[0;94m>\033[0;97m ")
            if command in choices:
                cam.check_cameras(choices[command])
                input("\033[0;96m[>]\033[0;97m Type 'enter' to continue. . .")
            elif command == "exit" or command == "EXIT":
                print('\n\033[0;96m[+]\033[0;97m Bye bye !')
                exit(1)
            else:
                print("\033[0;91m[+]\033[0;97m Error, try again")
    except KeyboardInterrupt:
        print('\n\033[0;96m[+]\033[0;97m Bye bye !')
        exit(1)

if __name__ == "__main__":
    main()

