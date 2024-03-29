### 조언 1
 [1] 10-20분 문제 잡고 모르면 답을 본다.
 
 [1-5] 답을 봤을때 깨달은 것은 필기 도구로 정리해둔다. 노션 같은 걸로.

 [2] 해법을 떠올린 상태에서 개발한다. 
   - (아 이거써서 이렇게 하면 아 이런 시간 복잡도 내에 되겠구나!)

 [3] 두괄식으로 접근한다.
   - (선언 하지 않고 추상화된 함수를 먼저 작성을 하고 구체적인 함수를 밑에 적어 나가기.)

 [4] 어려운 문제는 쉬운문제로 변환하여 단계적으로 접근한다.

 [5] 종이와 펜으로 그림을 그려본다.


## 개념 공부법

1. 개념 공부를 먼저하면서 쉬운 문제를 푼다.
2. 보통문제를 푼다.
3. 어느순간부터 보통문제가 빨리풀리면 다음 개념으로 넘어간다.
(문제 보자마다 어떤 알고리즘 사용하는지, 내가 이렇게 치면 문제가 풀리는걸 알아서 코드치는게 귀찮아지는 타이밍)

## 문제 풀때 가지는 마인드

1. 문제 풀 때 개념을 모르고 풀기 시작하면 의미가 없다. 개념이 무조건 우선
- 미분개념 모르고 미분문제 풀기와 동일
2. 30분 이하는 고민해보자
- 문제해결능력에 도움
- 타임어택을 해야하는 코테에 도움
- 시간 복잡도 계산이나 예외처리 로직, 알고리즘 흐름을 손으로 작성해 보는것을 추천
3. 30분 이상 고민해도 로직이 안떠오르거나, 시간복잡도를 못 줄인다
- 지금 문제에 어떤 알고리즘을 써야하는지 모르거나
- 모르는 문제풀이 개념이다, 뒤도 안보고 구글링을 한다.
==> 제일 최악의 상황, 개념부터 공부해야한다.

## 문제 풀고 가지는 마인드

1. 상위 100위권 정도 사람의 코드를 확인한다.
- 내가 모르는 함수를 사용해서 문제를 빨리 풀었나 확인
- 내가 잘 풀었나 확인
- 다른 개념으로 문제를 풀었나 확인
- 특정 STL 사용으로 속도나 메모리를 줄인것에는 연연하지 않는다.
1. 새롭게 알게된 함수 사용 정리
- 다른 사람 2중 for문 돌릴때 나는 함수 하나로 가능, ex: 순열과 조합, 소팅 등
1. 개선점이 있으면 고쳐본다.
- 문제 input값이 여유롭게 주어져서 작성한 코드가 통과하는 경우가 있다. 개선점 있으면 찾기
- 극단적인 리팩토링은 필요가없다(상위 1~50등 코드가 대부분 그럼)
- 쉬운 문제면 깔끔하게 넘어간다.

## 김경문의 문제 푸는 법

1. 문제를 읽으며 입력값의 범위, 알고리즘 후보군을 파악한다.
2. 알고리즘 후보군의 시간복잡도와 입력값의 범위를 비교하며 사용 가능한 알고리즘을 파악한다.(반복 1억이면 1초로 계산)
3. 손으로 대략의 코드를 작성한다.(예외는 어디서 잡을지, 함수는 몇개로 구성할지)
4. 작성한다.

### 코테 준비

1. 습관 만들기
* 하루에 딱 1문제 만 푼다. 더 풀고 싶어도 1개만 푼다
* 대신에 매일매일 한다
* 모르는 문제가 나오면 고민을 해보고, 1시간이 넘어간다 싶으면 답을 본다
* 답을 보고 내 코드와 비교하며 반성해보고 블로그에 남긴다

2. 유형 분석 & 유형별 풀이
* 기본적인 규칙인 습관 만들기와 똑같이 가져간다
* 1번이 어느정도 익숙해지면, 유명 기업들의 코딩테스트 문제들을 살펴본다
* 자주 나오는 유형을 파악한다.
* 유형을 파악했다면, 해당 유형에 대해서 익숙해질 때까지 문제를 꾸준히 푼다.

3. 난이도 올리기
* 기본적인 규칙인 습관 만들기와 똑같이 가져간다
* 자주 나오는 유형을 파악했다면, 이제는 기존 보다 조금 난이도 있는 문제를 풀어본다.

4. 매일매일 꾸준히 계속 풀기
* 3번까지 되었다면, 이것을 매일매일 꾸준하게 하여 감을 유지한다.

이때 중요한 것은 답이 맞고 틀리고는 중요하지 않다고 생각합니다. 내가 문제를 풀어봤을 때, 맞으면 좋은 것이고, 틀리면 내 코드와 비교하고, 다음에 더 개선시켜 나가면 됩니다.

코딩 테스트를 잘보기 위한 방법은 오직 문제 많이 풀어보고, 다른 사람의 코드를 보고 배우고, 나의 코드를 개선해보는 것의 반복 밖에 없다고 생각합니다.

이 글을 읽고 실천해 볼 Action Item

1. 백준 온라인에 가입해서 오늘 당장 내 수준에 맞는 혹은 더 낮은 1문제를 푼다. 
이걸 매일매일 실천해본다.
2. 자체 코딩테스트를 치루고, 문제도 공개되어있는 유명 회사들(카카오, 삼성)의 문제들을 
보고 어떤 유형이 나오는지 파악해본다.
3. 코딩 테스트 관련된 공부법이 나와있는 아래 링크를 쭉 읽어보고 나만의 코딩테스트 
학습전략을 짜본다.
4. 내가 푼 문제를 블로그에 남겨본다.
---
### 자주 읽어보기
**고민방법**

(20분 이하는 고민해볼 것)
(20분 고민해도 어떤 알고리즘을 써야할 지 감을 못 잡거나 모르는 문제풀이 개념이라면 구글링)
(다시 개념부터 공부할 것, 문제 풀면서 새롭게 알게 된 함수는 사용방법을 정리한다.)


**알고리즘문제푸는법**
1) 문제를 읽으며 입력값 범위, 알고리즘 후보군 파악
2) 알고리즘 후보군의 시간복잡도와 입력값의 범위를 비교하며 사용  가능한 알고리즘 파악
    ( 1억번 연산은 1초 )
3) 손으로 대략의 코드를 작성한다. ( 예외는 어디서 잡을지, 함수는 몇 개로 할 지 )
4) 코딩 

 **학습 순서**
1. 백준에 있는 알고리즘을 가지고 문제를 풀어본다. => 개념 쉬운 문제를 푼다.
 => 아니면 이것이 코딩테스트다 책 문제를 봐도 좋다.

2. 개념이 어느정도 익혀지면 보통문제를 푼다.
 => 개념이 익혀지고 보통문제도 빨리 풀리면 다음으로 넘어간다.
 => 내가 어떻게 치면 문제가 풀리는걸 알아서 코드치는게 귀찮아질 때

