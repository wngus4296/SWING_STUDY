from bs4 import BeautifulSoup
import requests
import os
import shutil #rmtree 사용하기 위한 모듈

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
#크롤링 우회하기 위한 헤더 수정

url = "https://comic.naver.com/webtoon/list.nhn?titleId=654774" #소녀의 세계 웹툰 이름, 회차 목록 확인
html1 = requests.get(url, headers = headers)
result1 = BeautifulSoup(html1.content, "html.parser")


webtoonName = result1.find("span", {"class", "wrt_nm"}).parent.get_text().strip().split('\n')
#class가 wrt_nm인 span태그의 부모 태그의 text가져와서 앞뒤 공백 제거 후 개행문자로 나눠서 배열에 저장
os.chdir(r"C:\Users\SAMSUNG\Desktop")

if os.path.isdir(r"C:\Users\SAMSUNG\Desktop\\" +  webtoonName[0]): #이미 디렉토리가 있을 경우
    shutil.rmtree(r"C:\Users\SAMSUNG\Desktop\\" +  webtoonName[0]) #지정된 디렉토리와 하위 디렉토리까지 모두 삭제
    
os.mkdir(webtoonName[0]) #웹툰 이름으로 디렉토리 만들기, webtoonName 배열의 인덱스 0이 웹툰 이름
print(webtoonName[0] + "   folder created successfully!")
os.chdir(r"C:\Users\SAMSUNG\Desktop\\" +  webtoonName[0]) #웹툰 제목 디렉토리로 이동


title = result1.findAll("td", {"class", "title"}) #class가 title인 td태그 모두 찾음

for t in title:
    os.mkdir((t.text).strip()) #웹툰 디렉토리 안에 회차별로 디렉토리 만들기, text가져와서 앞뒤 공백 제거
    os.chdir(os.getcwd() + "\\" + (t.text).strip()) #회차별 디렉토리로 이동

    url ="https://comic.naver.com" + t.a['href'] #회차 링크
    html2 = requests.get(url, headers = headers) #헤더 우회해서 링크 가져옴
    result2 = BeautifulSoup(html2.content, "html.parser") #html로 읽겠다

    webtoonImg = result2.find("div", {"class", "wt_viewer"}).findAll("img") #class가 wt_viewer인 div태그 찾고 거기서 img태그 모두 찾음
    num = 1 #이미지 저장 명

    for i in webtoonImg:
        saveName = os.getcwd() + "\\" + str(num) + ".jpg" #저장될 위치 + 저장 명 + 확장자
        with open(saveName, "wb") as file: #파일 열기, 이미지 저장할 것임
            src = requests.get(i['src'], headers = headers) #헤더 우회해서 이미지 src가져옴
            file.write(src.content) #이미지 저장
        num += 1 #저장 명 + 1

    os.chdir("..") #전 디렉토리로 이동

    print((t.text).strip() + "   saved completely!") #한 회차 이미지들 저장 완료
