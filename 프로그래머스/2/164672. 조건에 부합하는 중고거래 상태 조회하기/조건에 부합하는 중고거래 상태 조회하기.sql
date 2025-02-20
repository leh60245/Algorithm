-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, DECODE(status, 'SALE', '판매중', 'RESERVED', '예약중', '거래완료') status
FROM USED_GOODS_BOARD 
WHERE CREATED_DATE = DATE '2022-10-05'
ORDER BY board_id DESC