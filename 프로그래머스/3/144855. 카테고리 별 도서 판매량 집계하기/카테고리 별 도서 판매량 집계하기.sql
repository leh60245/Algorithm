-- 코드를 입력하세요
SELECT B.CATEGORY, SUM(SALES) TOTAL_SALES
FROM BOOK B LEFT OUTER JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE BETWEEN DATE '2022-01-01' AND DATE '2022-01-31'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY 