-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, U.CITY || ' ' ||U.STREET_ADDRESS1 || ' ' || U.STREET_ADDRESS2 "전체주소", SUBSTR(U.TLNO, 1, 3) || '-' || SUBSTR(U.TLNO, 4, 4) || '-' || SUBSTR(U.TLNO, 8, 4) "전화번호"
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
GROUP BY U.USER_ID, U.NICKNAME, U.CITY, U.STREET_ADDRESS1, U.STREET_ADDRESS2, U.TLNO
HAVING COUNT(B.BOARD_ID) >= 3
ORDER BY U.USER_ID DESC