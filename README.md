# 장고 웹 프로그래밍 기초 프로젝트
# 0. install guide
## 0.1 python install
python을 [설치](https://www.python.org/downloads/windows/)합니다. 현재 장고 version에서는 python 3.8 이후 버전을 지원하기 때문에 3.8 이후 version 설치를 권장합니다. 설치 이후 cmd 창에서```python --version```
을 통해 version을 확인합니다.
## 0.2 django install
공식 릴리스 설치를 권장합니다. 가상 환경에 django를 설치하여 프로젝트들을 구분하여 관리할 수 있도록 합니다. 
1. cmd 창에서 virtual package를 설치합니다.   
```pip install virtualenv``` 
2. 프로젝트를 작업할 가상환경 파일을 만듭니다.   
```virtualenv [가상환경폴더]```   
```virtualenv myenv```   
3. 가상환경 폴더로 이동하여 activate.bat을 실행해줍니다. -> 가상환경을 실행   
```myenv\scripts activate.bat```   
4. Django pip를 설치해줍니다.   
```pip install Django```
5. cmd창에서 Python을 실행하여 Django가 설치가 잘 되었는지 확인합니다.   
```import Django```오류 없이 작동하였다면 설치가 잘 되었습니다.


## 참고문서
- [django guide](https://docs.djangoproject.com/ko/4.0/intro/tutorial01/)
- [명준MJ youtube](https://www.youtube.com/watch?v=9WctwW_Pe1o&list=PLi4xPOplIq7d1vDdLBAvS5PmQR-p6KwUz&index=2)
