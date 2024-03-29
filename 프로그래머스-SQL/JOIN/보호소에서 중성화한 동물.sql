/*

  [테이블]
  ANIMAL_INS : 보호
  ANIMAL_OUTS : 입양

  [외래키]
  ANIMAL_ID

  [알아낼 것]
  중성화 수술 거친 동물 정보 (SEX_UPON_INTAKE)
   - 보호소 : 중성화 X
   - 입양 : 중성화 O

  ANIMAL_ID, ANIMAL_TYPE, NAME
  ORDER BY ANIMAL_ID


*/

SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME
ORDER BY A.ANIMAL_ID



