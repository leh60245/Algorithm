-- 코드를 입력하세요
SELECT NAME, COUNT(ANIMAL_ID) COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(ANIMAL_ID) >= 2
ORDER BY NAME