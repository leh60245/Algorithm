-- 코드를 입력하세요
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(B.PRICE * BS.SALES) TOTAL_SALES
FROM BOOK B 
LEFT OUTER JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID 
LEFT OUTER JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE TO_CHAR(BS.SALES_DATE, 'YYYY-MM') = '2022-01'
GROUP BY B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
ORDER BY B.AUTHOR_ID ASC, B.CATEGORY DESC
