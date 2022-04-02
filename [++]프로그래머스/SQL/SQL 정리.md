## 코테용 SQL 정리

### SQL 링크

- [sql 쿼리테스트](https://sqltest.net/#)
- [해커랭크 sql문제](https://www.hackerrank.com/domains/sql)
- [프로그래머스 sql문제](https://programmers.co.kr/)
- [좋은 블로그 글](https://dogsavestheworld.tistory.com/87?category=1004602)
- [좋은 블로그 글:JOIN편](https://dogsavestheworld.tistory.com/89?category=1004602)

<br />

### 키워드 리스트
- [컬럼체크] : `LIMIT`, `MAX`, `MIN`, `DISTINCT`
- [정렬조건] : `ORDER BY`, `GROUP BY` , `HAVING`
- [ETC] : `SET`, `BETWEEN`, `LIKE`, `IF`
- [NULL 체크] : `IS NULL`, `IFNULL`
- [JOIN] : `RIGHT`, `LEFT`, `INNER` `FULL OUTER`
- [날짜] : `DATE`, `DATE_FORMAT`


### LIMIT

#### 상위 N개 레코드

```sql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1
```

<br />

### MAX

#### 최댓값

```sql
SELECT MAX(DATETIME) FROM ANIMAL_INS

SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1
```

<br />

### MIN

#### 최솟값

```sql
SELECT MIN(DATETIME) FROM ANIMAL_INS

SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1
```

<br />

### DISTINCT

#### 중복 제거

```sql
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
```

<br />

### GROUP BY

#### 그룹핑 (SELECT한 테이블을 그룹 짓는다)

```sql
SELECT NAME, ID 
FROM ANIMAL_INS
GROUP BY NAME
ORDER BY NAME
```

- name의 인자가 'A', 'B', 'C', 'A', 'D', 'C'가 있다면
- 'A', 'B', 'C', 'D'로 그룹지어 준다.

<br />

#### 시간을 다루기 위한 group by

```sql
SELECT HOUR(DATETIME) AS H, COUNT(HOUR(DATETIME)) AS CNT
FROM ANIMAL_OUTS 
GROUP BY HOUR(DATETIME) 
HAVING H >= 9 AND H < 20 
ORDER BY H
```

<br />

### HAVING

#### GROUP BY 시행 후 조건 WHERE 대신 사용

```sql
SELECT NAME, COUNT(NAME) AS CNT 
FROM ANIMAL_INS
GROUP BY NAME
HAVING CNT > 1 
ORDER BY NAME
```

- NAME으로 그룹 지은 후 HAVING으로 조건을 지정한다.

<br />

### SET

#### 없는 값도 변수로 만들어 출력하는 방법

```sql
SET @H := -1;

SELECT (@H := @H+1) AS HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @H) AS COUNT
FROM ANIMAL_OUTS
WHERE @H < 23
```

<br />

### BETWEEN

#### 사이 조건

```sql
SELECT *
FROM contacts
WHERE contact_id BETWEEN 100 AND 200;
```

<br />

### 날짜 추출

#### YEAR, MONTH, DAY, HOUR, MINUTE, SECOND

```sql
SELECT HOUR(DATETIME)
HAVING HOUR BETWEEN 0 AND 19
```

- datetime에서 hour 추출 후 0 ~ 19 사이만 필터링 한다.

<br />

### NULL 체크

#### IS NULL (null을 찾는다)

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```

<br />

#### IFNULL (null값 찾아 치환)

```sql
SELECT IFNULL(NAME, 'ABC')
```

- NAME이 NULL이면 ABC로 변경한다.

<br />


### LIKE
#### 특정 문자열 포함하는 레코드 조회
```sql
-- 특정 문자열 시작 
SELECT * FROM 테이블명 WHERE 컬럼명 LIKE '문자열%';

-- 특정 문자열 제외 
SELECT * FROM 테이블명 WHERE 컬럼명 NOT LIKE '문자열%';

-- 특정 문자열로 끝
SELECT * FROM 테이블명 WHERE 컬럼명 LIKE '%문자열';

-- 특정 문자열이 중간 
SELECT * FROM 테이블명 WHERE 컬럼명 LIKE '%문자열%';

-- A로 시작하고 C로 끝나는 세 글자 (_ 사용)
SELECT * FROM 테이블명 WHERE 컬럼명 LIKE 'A_C';
```

<br />

### IN
#### 포함되는 것 찾기
```sql
-- 중략
WHERE NAME IN ('A', 'B', 'C')
```

<br />

### IF
#### 조건을 넣어 컬럼의 값을 변경
```sql
SELECT ANIMAL_ID, IF(NAME LIKE '%AB%', 'X', 'O')
```

<br />

### DATE
#### 문자열을 날짜로 변환하여 연산
```sql
-- DATETIME = '2020-01-01'
DATE(DATETIME)

-- 날짜로서 가능
DATE(YESTERDAY)=DATE(DATETIME)
```

<br />

### DATE_FORMAT
#### 원하는 날짜 출력 포맷 지정
```sql
-- DATETIME = '2020-01-01'
SELECT NAME, DATE_FORMAT(DATETIME, "%Y-%m")
```

<br />



## JOIN
![image](https://user-images.githubusercontent.com/70880695/161356959-ae1148b6-0e71-47ab-9df8-094b108195b4.png)


### RIGHT JOIN

#### 입양 간 (B) 기록 존재, but 보호소 들어 온 (A) 기록 X

```sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
RIGHT JOIN AMINAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
```

[//]: # (- A와 B를 Join하는 대신,)



