### 인기있는 아이스크림

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
