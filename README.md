# 풀스텍 어떻게 하는거지? 간좀 봐보자... 하고 시작하는 서비스
간단한 트위터를 모방하는 풀스텍 어플을 개발해보고 조금씩 피처를 추가해 가면서 감을 익히는 프로젝트.

# 참조
[Developing a Single Page App with FastAPI and Vue.js](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/#objectives)

[Figma](https://www.figma.com/file/X0Lge9GtYJF9FZK9rcfV5T/Twitter-bot?node-id=0%3A1)

# Todo

~~1. Landing Page에 모든 트윗 보일 수 있게~~
~~2. 트윗할때 private, public 정할 수 있게 하기~~
~~3. public만 보일 수 있도록 하기~~
4. Dashboard pagination
5. 트윗 작성 popup으로 하기
~~6. Update Password~~
7. 컴포넨트화 시켜보기
   ~~1. 트윗~~
   2. 트윗 상세 페이지 팝업
8. 좋아요 기능 추가하기
   1. 로그인 했을때는 좋아요 할 수 있고 아님 숫자만 볼 수 있다.
9.  댓글 기능 추가하기


# 고민 거리(현 상황)
- like db 오브젝트를 만들었는데 이거를 트위터 부속으로 날려야 하는지 고민중...흠냐


# 사용법
- [블로 참조](https://tech.visiodeibc.dev/2022/01/30/Twitter-clone-1-fastapi-setup/)
`docker-compose up -d --build`
http://127.0.0.1:8080/ 에서는 front end 확인
http://localhost:5001/docs 에서는 Swagger document를 확인할 수 있다.

## db변화가 있은 후에
`docker-compose exec backend aerich migrate`
`docker-compose exec backend aerich upgrade`
