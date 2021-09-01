# visipedia annotation tool 사용하기

###  visipedia annotaton tool github

[https://github.com/visipedia/annotation_tools](https://github.com/visipedia/annotation_tools)


설명 영상 
> [https://youtu.be/zaMGxfJ9UcA](https://youtu.be/zaMGxfJ9UcA)

## 1. 코드 다운

~~위 페이지에서 코드를 다운 받습니다.~~

현재 레파지토리를 다운받습니다
다운받은 폴더안에 annotation_tools 폴더가 있습니다.

다운 받을 폴더에 아래 코드 입력 
~~~
$ ~~git clone https://github.com/visipedia/annotation_tools.git~~
$ git clone https://github.com/khw11044/Annotation.git
$ cd annotation_tools
~~~

annotation_tools 폴더에서 아래 코드를 입력 
~~~
$ pip install -r requirements.txt
~~~

## 2. MongoDB 설치 

MongoDB 설치는 아래 블로그에 잘 설명되어 있습니다.

[https://velog.io/@seungsang00/Ubuntu-MongoDB-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-Ubuntu-20.04](https://velog.io/@seungsang00/Ubuntu-MongoDB-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-Ubuntu-20.04)

- 우분투의 경우 

1). 패키지 관리 시스템에서 사용하는 public key 가져오기
~~~
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
~~~

2). MongoDB를 위한 List 파일 만들기
~~~
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
~~~

3). 로컬 패키지 데이터베이스 불러오기
~~~
$ sudo apt-get update
~~~

4). MongoDB 패키지 설치하기
~~~
$ sudo apt-get install -y mongodb-org
~~~

5). MongoDB 실행하기
~~~
$ sudo systemctl start mongod
$ mongo
~~~

- 맥의 경우 

## 3. Annotation tool 실행하기 

### 1) 터미널에서 mongodb 실행 

~~~
$ sudo systemctl start mongod
$ mongo
~~~

### 2) annotation_tools 폴더에 python3 run.py 실행 

~~~
$ python3 run.py
~~~

### 3) json 파일 load하기 
python3 -m annotation_tools.db_dataset_utils --action load --dataset .json파일 위치 --normalize

~~~
$ python3 -m annotation_tools.db_dataset_utils --action load --dataset /home/khw11044/golf/me/extract_data/f_label_input/bad_front_swing0549.json --normalize
~~~

### 4) 이미지 파일 load하기
이미지 파일이 있는 폴더에서 터미널을 열고 아래 코드 실행

~~~
$ python3 -m http.server 8007
~~~

## 4. Annotation하기 

웹에서 아래 주소로 접속

[http://localhost:8008/edit_task/?category_id=1](http://localhost:8008/edit_task/?category_id=1)

오른쪽이 left_elbow, left_hip 등 

왼쪽이 right_elbow, left_hip 등 

![1](/img/1.png)
![2](/img/2.png)
​

안보이는 관절은 occluded로 표시 
![3](/img/3.jpg)
​

골프 클럽헤드가 화면 밖으로 나가는경우가 많은데 그런경우 골프 클럽헤드가 있을곳이라고 예상되는 곳의 화면끝에 point를 놓고 occluded 표시 
![4](/img/4.jpg)
​

또한 화면안에 있어도 안보이는 경우는 있을곳이라고 예상되는곳에 point를 찍고 occluded

occluded 상태인 경우 바운딩박스는 치지않습니다.
​

골프 클럽헤드가 완전히 보이면 'New' 버튼 또는 키보드 n을 눌러 바운딩박스를 처줍니다.

​![5](/img/5.png)
​

골프공의 경우 한 이미지당 하나를 초과하지 않으며 여러개가 보이는경우 칠려는 골프공만 바운딩박스를 해주시면 됩니다. 

​

발뒤꿈치, 어깨, 팔꿈치, 손목, 골반등 안보이면 있을것이라 생각되는 위치에 찍고, occluded  

​

한장을 끝내시며 Next 버튼을 누릅니다

## 5. Annotation 저장하기

한 영상(20장의 이미지)가 끝나면 Save를 누르고 json파일을 load한 터미널에서 아래 코드를 입력해줍니다.

​
### annotation한 파일 export하기
~~~
$ python3 -m annotation_tools.db_dataset_utils --action export --output 저장할.json파일 위치와 이름 --denormalize
~~~

### 이후 load한 json을 drop해야합니다. 아래 코드를 입력해줍니다.
~~~
$ python3 -m annotation_tools.db_dataset_utils --action drop
~~~

계속해서 load, annotate, export, drop 을 반복해줍니다.

## Remind

1. mongodb 실행  
아무 터미널이나 열고 

> sudo systemctl start mongod
> mongo

​

2. annotation tool run  
annotation_tools 폴더에 python3 run.py 실행 

> python3 run.py

​

3. json load   
annotation_tools 폴더에서 터미널 열고 아래 코드

> python3 -m annotation_tools.db_dataset_utils --action load --dataset .json파일 위치 --normalize

​

4. 이미지 load  
이미지가 있는 폴더에 터미널 열고 아래 코드  

> python3 -m http.server 8007

​
5. 라벨링

​6. json export  
저장할 위치에 저장 

> python3 -m annotation_tools.db_dataset_utils --action export --output 저장할.json파일 위치와 이름 --denormalize

​

7. json drop  
> python3 -m annotation_tools.db_dataset_utils --action drop

​
8. 3,4,5,6,7 반복

시범 영상 

[![이미지 텍스트](/img/youtube.png)](https://www.youtube.com/watch?v=bG3YGntzLMU)

