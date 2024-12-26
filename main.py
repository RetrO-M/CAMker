from requests                       import get, RequestException
from bs4                            import BeautifulSoup
from re                             import search, IGNORECASE
from random                         import choice
from os                             import system

class NoTrack:
    def __init__(self):
        self.proxies = {
            "http": "socks5h://127.0.0.1:9050",
            "https": "socks5h://127.0.0.1:9050"
        }
        self.headers = {
            "User-Agent": choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/119.0.2151.65 Version/17.0 Mobile/15E148 Safari/604.1", 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/117.0.2045.48 Version/17.0 Mobile/15E148 Safari/604.1", 
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1", 
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.105 Version/17.0 Mobile/15E148 Safari/604.1",
            ]),
            "Accept-Language": choice([
                "en-US,en;q=0.9", "fr-FR,fr;q=0.9", "es-ES,es;q=0.9", "de-DE,de;q=0.9",
                "it-IT,it;q=0.9", "pt-PT,pt;q=0.9", "ru-RU,ru;q=0.9", "ja-JP,ja;q=0.9",
                "zh-CN,zh;q=0.9", "ko-KR,ko;q=0.9", "nl-NL,nl;q=0.9", "ar-SA,ar;q=0.9",
                "hi-IN,hi;q=0.9", "tr-TR,tr;q=0.9", "sv-SE,sv;q=0.9", "da-DK,da;q=0.9",
                "fi-FI,fi;q=0.9", "no-NO,no;q=0.9", "el-GR,el;q=0.9", "th-TH,th;q=0.9",
                "hu-HU,hu;q=0.9", "ro-RO,ro;q=0.9", "cs-CZ,cs;q=0.9", "sk-SK,sk;q=0.9",
                "bg-BG,bg;q=0.9", "lv-LV,lv;q=0.9", "lt-LT,lt;q=0.9", "sl-SI,sl;q=0.9",
                "et-EE,et;q=0.9", "ms-MY,ms;q=0.9", "vi-VN,vi;q=0.9", "bn-BD,bn;q=0.9",
                "sw-KE,sw;q=0.9", "tl-PH,tl;q=0.9", "iw-IL,iw;q=0.9", "pa-PK,pa;q=0.9",
                "fa-IR,fa;q=0.9", "ne-NP,ne;q=0.9", "sq-AL,sq;q=0.9", "km-KH,km;q=0.9",
                "is-IS,is;q=0.9", "hy-AM,hy;q=0.9", "az-AZ,az;q=0.9", "ka-GE,ka;q=0.9",
                "mt-MT,mt;q=0.9", "cy-GB,cy;q=0.9", "tk-TM,tk;q=0.9", "xh-ZA,xh;q=0.9",
                "zu-ZA,zu;q=0.9", "ar-AE,ar;q=0.9", "uk-UA,uk;q=0.9", "si-LK,si;q=0.9",
                "mn-MN,mn;q=0.9", "la-VN,la;q=0.9", "pa-IN,pa;q=0.9", "sw-TZ,sw;q=0.9",
                "te-IN,te;q=0.9", "ta-LK,ta;q=0.9", "ml-IN,ml;q=0.9", "kn-IN,kn;q=0.9",
                "or-IN,or;q=0.9", "gu-IN,gu;q=0.9", "mr-IN,mr;q=0.9", "as-IN,as;q=0.9",
                "my-MM,my;q=0.9", "bs-BA,bs;q=0.9", "hr-HR,hr;q=0.9", "sr-RS,sr;q=0.9",
                "ca-ES,ca;q=0.9", "eo-EO,eo;q=0.9", "oc-FR,oc;q=0.9", "se-NO,se;q=0.9",
                "ay-PE,ay;q=0.9", "qu-PE,qu;q=0.9", "fy-NL,fy;q=0.9", "jv-ID,jv;q=0.9",
                "su-ID,su;q=0.9", "sc-IT,sc;q=0.9", "gd-GB,gd;q=0.9", "wa-BE,wa;q=0.9",
                "sm-WS,sm;q=0.9", "so-SO,so;q=0.9", "ku-TR,ku;q=0.9", "na-NR,na;q=0.9",
                "fj-FJ,fj;q=0.9", "ht-HT,ht;q=0.9", "ti-ER,ti;q=0.9", "sg-CF,sg;q=0.9",
                "br-FR,br;q=0.9", "gn-PY,gn;q=0.9", "af-ZA,af;q=0.9", "csb-PL,csb;q=0.9",
                "hsb-DE,hsb;q=0.9", "yue-HK,yue;q=0.9", "to-TO,to;q=0.9", "dz-BT,dz;q=0.9",
                "qu-BO,qu;q=0.9", "sa-IN,sa;q=0.9", "rw-RW,rw;q=0.9", "mi-NZ,mi;q=0.9",
                "fo-FO,fo;q=0.9", "haw-US,haw;q=0.9", "gl-ES,gl;q=0.9", "nv-US,nv;q=0.9",
                "arn-CL,arn;q=0.9", "kl-GL,kl;q=0.9", "en-NG,en;q=0.9", "tg-TJ,tg;q=0.9",
                "ps-AF,ps;q=0.9", "prs-AF,prs;q=0.9", "am-ET,am;q=0.9", "ig-NG,ig;q=0.9",
                "yo-NG,yo;q=0.9", "ha-NE,ha;q=0.9", "sh-BA,sh;q=0.9", "sr-ME,sr;q=0.9",
                "tt-RU,tt;q=0.9", "ky-KG,ky;q=0.9", "uz-UZ,uz;q=0.9", "ba-RU,ba;q=0.9",
                "kk-KZ,kk;q=0.9", "be-BY,be;q=0.9", "mo-MD,mo;q=0.9", "ab-GE,ab;q=0.9",
                "os-RU,os;q=0.9", "tt-RU,tt;q=0.9", "ts-BW,ts;q=0.9", "st-LS,st;q=0.9"
            ]),
            "DNT": "1",
            "Referer": choice([
                "https://www.google.com", "https://duckduckgo.com", "https://www.startpage.com",
                "https://www.bing.com", "https://www.qwant.com", "https://www.brave.com/search",
                "https://www.mojeek.com", "https://swisscows.com", "https://www.neeva.com"
            ]),
            "Origin": choice([
                "https://www.google.com", "https://duckduckgo.com", "https://www.startpage.com",
                "https://www.bing.com", "https://www.qwant.com", "https://www.brave.com/search",
                "https://www.mojeek.com", "https://swisscows.com", "https://www.neeva.com"
            ]),
        }

    def title(self):
        system('cls || clear')
        print(
            '''
\033[0;91m     __     \033[0;97m_____                _    
\033[0;91m  /\ \ \___\033[0;97m/__   \_ __ __ _  ___| | __
\033[0;91m /  \/ / _ \ \033[0;97m/ /\/ '__/ _` |/ __| |/ /
\033[0;91m/ /\  / (_) \033[0;97m/ /  | | | (_| | (__|   < 
\033[0;91m\_\ \/ \___/\033[0;97m\/   |_|  \__,_|\___|_|\_\\
            '''
        )

    def analyze_js_behavior(self, js_code):
        risks = []
        if search(r'navigator\.geolocation', js_code):
            risks.append("Access to geolocation detected.")
        if search(r'document\.cookie', js_code):
            risks.append("Access to cookies detected.")
        if search(r'canvas', js_code, IGNORECASE):
            risks.append("Usage of Canvas API detected (potential fingerprinting).")
        if search(r'webrtc', js_code, IGNORECASE):
            risks.append("WebRTC usage detected (potential IP leakage).")
        if search(r'window\.open', js_code):
            risks.append("Popup creation detected.")
        if search(r'fetch\(', js_code) or search(r'XMLHttpRequest', js_code):
            risks.append("Network request detected (fetch or XMLHttpRequest).")
        if search(r'document\.write', js_code):
            risks.append("Usage of document.write detected (potential DOM manipulation).")
        if search(r'localStorage|sessionStorage', js_code):
            risks.append("Access to localStorage or sessionStorage detected.")
        return risks

    def detect_malicious(self, js_code):
        malicious_signatures = []
        if search(r'window\.navigator\.share', js_code):
            malicious_signatures.append("Attempt to access sharing features (potential spyware).")
        if search(r'getUserMedia\(', js_code):
            malicious_signatures.append("Access to user media (camera/microphone) detected (potential spyware).")
        if search(r'setInterval\(', js_code):
            malicious_signatures.append("Potential use of interval timers for continuous actions (common in adware).")
        if search(r'cookie', js_code, IGNORECASE):
            malicious_signatures.append("Suspicious use of cookies (potential tracking).")
        if search(r'window\.location', js_code):
            malicious_signatures.append("Potential redirection detected (could be phishing or adware).")
        return malicious_signatures

    def extract_js_scripts(self, url):
        try:
            response = get(url, headers=self.headers, proxies=self.proxies, timeout=10)
            response.raise_for_status()
        except RequestException as e:
            print("\033[0;91m[+]\033[0;97m Error while fetching the URL: ", e)
            return
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script')
        noscript_tags = soup.find_all('noscript')
        report = []
        for script in scripts:
            script_info = {}
            if script.string:
                script_info['type'] = 'inline'
                script_info['content'] = script.string[:300] + ('...' if len(script.string) > 300 else '')
                script_info['risks'] = self.analyze_js_behavior(script.string)
                script_info['malicious'] = self.detect_malicious(script.string)
            elif script.get('src'):
                script_info['type'] = 'external'
                script_info['source'] = script['src']
                try:
                    external_response = get(script['src'], timeout=10)
                    if external_response.status_code == 200:
                        js_code = external_response.text
                        script_info['risks'] = self.analyze_js_behavior(js_code)
                        script_info['malicious'] = self.detect_malicious(js_code)
                    else:
                        script_info['risks'] = ["Failed to load the external script."]
                        script_info['malicious'] = []
                except RequestException as e:
                    script_info['risks'] = [f"Error while fetching the script: {e}"]
                    script_info['malicious'] = []
            else:
                script_info['type'] = 'unknown'
                script_info['risks'] = ["Script without content or source."]
                script_info['malicious'] = []
            report.append(script_info)
        for tag in noscript_tags:
            report.append({
                'type': 'noscript',
                'content': tag.text.strip()[:300] + ('...' if len(tag.text.strip()) > 300 else ''),
                'risks': ["Alternative content detected, may contain critical information."],
                'malicious': []
            })
        for i, script in enumerate(report, 1):
            print(f"\033[0;92m[+]\033[0;97m Script \033[0;96m{i}\033[0;97m:")
            print(f"  \033[0;91m→  \033[0;97mType           \033[0;96m :\033[0;97m {script['type']}")
            if 'source' in script:
                print(f"  \033[0;91m→  \033[0;97mSource          \033[0;96m:\033[0;97m {script['source']}")
            if 'content' in script:
                print(f"  \033[0;91m→\033[0;97m  Content        \033[0;96m : \033[0;95m{script['content']}")
            if script['risks']:
                print(f"  \033[0;91m→\033[0;97m  Risks          \033[0;96m :\033[0;95m {', '.join(script['risks'])}")
            if script['malicious']:
                print(f"  \033[0;91m→\033[0;97m  Malicious Signs \033[0;96m:\033[0;91m {', '.join(script['malicious'])}")
            print(f"\033[0;91m{'=' * 100}\033[0;97m")
        
try:
    track = NoTrack()
    track.title()
    url = input("\033[0;91m?\033[0;97m Enter the URL to analyze\033[0;96m :\033[0;97m ")
    track.extract_js_scripts(url)
except Exception as e:
    print('\033[0;91m[+]\033[0;97m Program Failed: ', e) 