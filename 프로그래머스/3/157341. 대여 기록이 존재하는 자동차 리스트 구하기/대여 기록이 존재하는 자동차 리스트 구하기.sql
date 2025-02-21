-- 코드를 입력하세요
SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H 
ON C.CAR_ID = H.CAR_ID 
AND C.CAR_TYPE = '세단'
AND EXTRACT(MONTH FROM H.START_DATE) = 10
ORDER BY C.CAR_ID DESC
