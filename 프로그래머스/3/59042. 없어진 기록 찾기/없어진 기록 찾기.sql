-- 코드를 입력하세요
-- 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별, 중성화 여부
-- 동물의 아이디, 생물 종, 입양일, 이름, 성별, 중성화 여부
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I 
RIGHT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID