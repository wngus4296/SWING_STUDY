from bs4 import BeautifulSoup

import urllib.request

html = urllib.request.urlopen("http://www.swu.ac.kr/www/swuniversity.html")
result = BeautifulSoup(html.read(), "html.parser")

print("**서울여자대학교 학과 및 홈페이지 정보**")
print("학과\t\t\t홈페이지")

search = result.findAll("a") #a태그만 찾는다.

for s in search:
    if s.text == "자율전공학부" or s.text == "공동기기실" or "교육원" in s.text or "대학원" in s.text: #a태그 중 텍스트가 자율전공학부, 공동기기실인 경우 출력하지 않는다.
        continue
    print(s.text + "\t\t", end="") #a태그의 텍스트를 출력하지만 개행 문자는 제거한다.
    
    html2 = urllib.request.urlopen("http://www.swu.ac.kr/" + s['href']) #해당 학과에 연결된 페이지에 들어간다.
    result2 = BeautifulSoup(html2.read(), "html.parser")
    search2 = result2.findAll("span") #span태그만 찾는다.
    
    if not search2:#span태그가 하나도 없는 경우 == 홈페이지도 없음
        print("홈페이지가 존재하지 않음")
        
    for s2 in search2:
        if "홈페이지" in s2.text:
            search3 = result2.find("a", {"class", "btn btn_xl btn_blue_gray"}) #a태그의 class속성이 btn ~ 인 것만 찾는다.
            print(search3['href']) #찾은 내용의 href를 출력(홈페이지 링크)
            break
        else:
            print("홈페이지가 존재하지 않음")
            break
