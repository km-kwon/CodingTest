### 가격이 제일 비싼 식품의 정보 출력하기

---

성공 코드

```
select PRODUCT_ID,	PRODUCT_NAME	,PRODUCT_CD,	CATEGORY	,PRICE
from FOOD_PRODUCT
where PRICE = (
select max(PRICE)
from FOOD_PRODUCT
)

```

사용 개념

- where 절에 서브 쿼리 사용
