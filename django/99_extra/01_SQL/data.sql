-- Active: 1728554818115@@127.0.0.1@3306

-- 정상적으로 연결이 되었다면 1번째 줄에 있는 저런 문구가 작성된다.

-- Active Connecion 했는데, 연결이 안된다?
-- 1. 다른 DB가 있으면 다른 DB로 연결을 바꿨다가 다시 연결한다.
-- 2. vscode를 껏다가 킨다.

-- songs라는 테이블을 만든다.
  -- songs 테이블은 id, title, artist, album, genre, duration 이라는
  -- 다양한 데이터를 저장할 수 있는 공간을 필요로 한다.

-- 테이블을 생성하는데, songs라는 이름이고,
-- songs 테이블은 다양한 컬럼을 가지는데... 
-- 각 컬럼에 어떤 데이터가 저장 될 수 있어야 하는가?
CREATE TABLE songs (
  -- 아이디 -> 주로 기본키로 사용되는 고유값
  -- 내가 저장한 데이터의 유일한 (중복되지 않는) 값으로, 나의 식별자
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  artist TEXT,
  album TEXT,
  genre TEXT,
  -- 60초
  duration INTEGER
); -- SQL은 항상 세미콜론 (;) 으로 끝맺어 줘야한다.

-- 테이블을 생성한다 -> 내 데이터가 저장될 위치를 정의한다.
-- DDL 

-- 데이터 삽입
-- songs 테이블에 데이터를 삽입할 때, 어떤 데이터를 어디에 삽입할 것이냐?
                  -- 어디에
INSERT INTO songs (title, artist, album, genre, duration)
-- 무엇을
VALUES
 ('노래 1', '가수 1', '앨범 1', 'pop', 200);

-- 데이터를 동시에 여러개를 삽입한다.

INSERT INTO songs (title, artist, album, genre, duration)
-- 무엇을
VALUES
 ('노래 2', '가수 2', '앨범 2', 'pop', 300),
 ('노래 3', '가수 3', '앨범 3', 'rock', 330),
 ('노래 4', '가수 4', '앨범 4', 'rock', 400),
 ('노래 5', '가수 5', '앨범 5', 'hip hop', 500);

SELECT * FROM songs;

-- 데이터 업데이트 
-- 데이터를 수정하려고 한다 -> 수정하려는 대상이 누군지를 알아야 한다.

-- songs 테이블을 수정한다.
UPDATE songs
-- title column을 아래 문자열 값으로 변경한다.
SET title = 'NEW TITLE'
WHERE id = 1;

-- 데이터 삭제 -> 누구를?
DELETE FROM songs
WHERE id = 1;

-- 정렬 : 제목 기준으로 내림차순
SELECT * FROM songs
-- 정렬을 하려고 할때, 그냥 컬럼명만 적는 경우는... 왜 그런거냐?
-- 기본적으로 정렬의 기준은 오름차순으로 되어 있습니다. -> 오름 차순을 의미하는 ASC 보통 생략
ORDER BY title DESC; 

SELECT * FROM songs
ORDER BY title DESC, album; 

-- 필터링 : WHERE 절에 작성되는 조건 
  -- id를 기준으로 조회를 해야한다. -> id가 고유값인건 맞지만,
  -- 그렇다고 항상 모든 조회를 중복없이, 고유값으로만 조회해야 하지는 않다.
-- duration 값이 350 이상인 경우,
SELECT * FROM songs WHERE duration >= 350;

-- duration 값이 350 이상이거나, title이 `노래 2`인 경우의
-- title과 duration만 보여줘
SELECT title, duration FROM songs 
WHERE duration >= 350 OR title = '노래 2';

-- 그룹화
-- 장르를 기준으로 그룹화해서,
-- 각 장르별 데이터 수가 몇개 인지 보여주시오.\
-- GROUP BY를 사용한다 -> 집계함수도 보통 함께 사용하게 된다.

-- 내가 어떤 컬럼을 기준으로 그룹화 했는지 정보와 함께,
-- 집계 함수를 사용한 결과를 컬럼에 aggregate해서 보여준다 라고 하면,
  -- 그렇게 집계 함수로 처리한 컬럼명을 조금더 이해하기 쉬운 이름으로 바꿔주면 좋겠다.
-- AS 등을 설정할때, '총합' 이라는 값을 왜 '쿼트'로 감싸 주어야 하느냐
-- 안감싸도 잘만 되던데?
  -- HTML 공부할 때 처럼 SQL도 기본적으로 `공백` 을 기준으로 키워드를 구분한다.
  -- `총 합` 의 경우, 공백까지 포함한 문자열이라면 그때 '' 감싸서 문자열임을 표기한다.
SELECT genre, COUNT(*) AS '총 합' FROM songs
GROUP BY genre;

-- WHERE와 HAVING
-- WHERE절은 GROUP BY보다 먼저 한번 필터링을 진행하고,
  -- 그렇게 걸러진 데이터를 토대로 그룹화를 진행한다.
  -- 그렇게 그룹화하는 과정에 어떤 조건을 달고 싶다.
  -- HAVING 절을 사용해야한다.
SELECT genre, duration, COUNT(*) FROM songs WHERE duration <= 350
GROUP BY genre;

-- 데이터를 삭제한다 -> 1개를 삭제한다.
-- 데이터 삭제시에도, 특정 조건을 만족하는 다수의 데이터를 한번에 삭제 할 수도 있다.
DELETE FROM songs 
WHERE 
  id IN (
    -- 2, 3, 4, 5
    SELECT id FROM songs WHERE genre LIKE '장르%'
  );