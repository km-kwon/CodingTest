### 조건에 맞는 도서와 저자 리스트 출력하기

---

성공 코드

```
select BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE
from BOOK join AUTHOR
on BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
where CATEGORY like "%경제%"
order by PUBLISHED_DATE
```

사용 개념

- join을 활용하여 해결
