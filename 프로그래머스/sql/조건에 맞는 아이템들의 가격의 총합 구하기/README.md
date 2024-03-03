### 조건에 맞는 아이템들의 가격의 총합 구하기


---

성공 코드

```
select sum(PRICE) as TOTAL_PRICE
from ITEM_INFO
where RARITY like "%LEGEND%"

```

사용 개념

- where 문자열 포함 여부확인 조건 사용
