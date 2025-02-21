-- 코드를 입력하세요
-- 출하 번호(외래), 아이스크림 맛(기본), 상반기 아이스크림 총주문량
-- 출하 번호(기본, 공장 마다 다름), 아이스크림 맛(외래), 7월 아이스크림 총주문량
SELECT H.FLAVOR
FROM FIRST_HALF H
LEFT JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) JULY_TOTAL_ORDER
           FROM JULY
           GROUP BY FLAVOR) J ON H.FLAVOR = J.FLAVOR
ORDER BY H.TOTAL_ORDER + J.JULY_TOTAL_ORDER DESC
FETCH FIRST 3 ROWS ONLY;