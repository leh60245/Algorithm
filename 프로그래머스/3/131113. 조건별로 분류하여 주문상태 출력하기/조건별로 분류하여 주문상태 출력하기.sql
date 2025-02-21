-- 코드를 입력하세요
SELECT 
    F.ORDER_ID,
    F.PRODUCT_ID,
    TO_CHAR(F.OUT_DATE, 'YYYY-MM-DD'),
    (CASE 
        WHEN F.OUT_DATE IS NULL THEN '출고미정'
        WHEN F.OUT_DATE <= DATE '2022-05-01' THEN '출고완료'
        ELSE '출고대기'
    END) "출고여부"
FROM FOOD_ORDER F
ORDER BY F.ORDER_ID ASC;