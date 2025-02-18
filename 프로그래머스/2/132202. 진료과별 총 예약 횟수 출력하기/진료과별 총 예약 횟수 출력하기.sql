-- 코드를 입력하세요
-- APNT_YMD,    APNT_NO,    PT_NO,   MCDP_CD,   MDDR_ID, APNT_CNCL_YN, APNT_CNCL_YMD
-- 진료예약일시,  진료예약번호, 환자번호, 진료과코드,  의사ID, 예약취소여부, 예약취소날짜
SELECT MCDP_CD AS "진료과 코드",  COUNT(PT_NO) AS "5월예약건수"
FROM APPOINTMENT 
WHERE TO_CHAR(APNT_YMD, 'YYYY-MM') = '2022-05'
GROUP BY MCDP_CD
ORDER BY "5월예약건수", "진료과 코드"