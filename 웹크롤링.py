from bs4 import BeautifulSoup

import urllib.request

html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result = BeautifulSoup(html.read(), "html.parser")

print("**서울여자대학교 학과 및 홈페이지 정보**")
print("학과\t\t\t홈페이지")

search = result.findAll("a")
for s in search:
    if s.text == "자율전공학부" or s.text == "공동기기실":
        continue
    if s.text == "바롬인성교육원":
        break
    print(s.text + "\t\t", end="")
    html = urllib.request.urlopen("http://www.swu.ac.kr/" + s['href'])
    result2 = BeautifulSoup(html.read(), "html.parser")
    search2 = result2.findAll("span")
    if not search2:
        print("홈페이지가 존재하지 않음")
    for s2 in search2:
        if "홈페이지바로가기" in s2.text or "홈페이지 바로가기" in s2.text:
            search3 = result2.find("a", {"class", "btn btn_xl btn_blue_gray"})
            print(search3['href'])
            break
        else:
            print("홈페이지가 존재하지 않음")
            break;
