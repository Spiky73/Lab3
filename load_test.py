from locust import task, run_single_user
from locust import FastHttpUser


class apple_with_cookies(FastHttpUser):
    host = "https://apple.com"

    @task
    def t(self):
        with self.client.request(
            "GET",
            "https://www.apple.com/",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://securemvt.apple.com/m2/apple/mbox/json?mbox=target-global-mbox&mboxSession=ff127cfbd7014007ac85875fb7ad03d4&mboxPC=&mboxPage=2146d9fa80fa42c288f19c35d931b005&mboxRid=77bb80a668674b2dab55b60033af89ec&mboxVersion=1.5.0&mboxCount=1&mboxTime=1606601515689&mboxHost=www.apple.com&mboxURL=https%3A%2F%2Fwww.apple.com%2F&mboxReferrer=&browserHeight=618&browserWidth=1597&browserTimeOffset=60&screenHeight=1080&screenWidth=1920&colorDepth=24&devicePixelRatio=1&screenOrientation=landscape&webGLRenderer=Intel%20HD%20Graphics%205000%20OpenGL%20Engine",
            headers={
                "Referer": "https://www.apple.com/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://www.apple.com/us/shop/bag/status?apikey=SFX9YPYY9PPXCU9KH",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://www.apple.com/ac/localeswitcher/3/it_IT/content/localeswitcher.json",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://www.apple.com/search-services/suggestions/defaultlinks/?src=globalnav&locale=en_US",
            headers={
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://www.apple.com/favicon.ico",
            headers={
                "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(apple_with_cookies)