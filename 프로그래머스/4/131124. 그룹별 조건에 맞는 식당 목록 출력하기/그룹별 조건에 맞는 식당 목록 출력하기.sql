-- 코드를 입력하세요
SELECT MM.MEMBER_NAME, RR.REVIEW_TEXT, TO_CHAR(RR.REVIEW_DATE, 'YYYY-MM-DD') REVIEW_DATE
FROM MEMBER_PROFILE MM
JOIN REST_REVIEW RR ON MM.MEMBER_ID = RR.MEMBER_ID
WHERE MM.MEMBER_ID IN (SELECT M.MEMBER_ID
FROM MEMBER_PROFILE M
JOIN REST_REVIEW R ON M.MEMBER_ID = R.MEMBER_ID
GROUP BY M.MEMBER_ID
ORDER BY COUNT(R.REVIEW_ID) DESC
FETCH FIRST 1 ROW ONLY)
ORDER BY RR.REVIEW_DATE ASC, RR.REVIEW_TEXT ASC