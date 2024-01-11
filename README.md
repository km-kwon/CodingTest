## 코딩 테스트 대비 풀이 모음
---
# 프로그래머스

### 유형별
---
## 해쉬

- [폰켓몬](https://github.com/km-kwon/CodingTest/tree/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C/%ED%95%B4%EC%89%AC/%ED%8F%B0%EC%BC%93%EB%AA%AC)

```
딕셔너리 자료형 처리에 유용한 collection 라이브러리 사용
딕셔너리 자료형은 해쉬를 사용하여 속도가 빠름
```
- [완주하지 못한 선수](https://github.com/km-kwon/CodingTest/tree/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C/%ED%95%B4%EC%89%AC/%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80%20%EB%AA%BB%ED%95%9C%20%EC%84%A0%EC%88%98)

```
폰켓몬과 비슷한 유형의 문제이며 큰 차이는 존재X
```

---

## 스택 / 큐

- [같은 숫자는 싫어](https://github.com/km-kwon/CodingTest/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/%EC%9C%A0%ED%98%95%EB%B3%84%20%EB%AC%B8%EC%A0%9C/%EC%8A%A4%ED%83%9D/%ED%81%90/%EA%B0%99%EC%9D%80%20%EC%88%AB%EC%9E%90%EB%8A%94%20%EC%8B%AB%EC%96%B4/README.md)

```
큐를 실제로 구현.
```

---
### Level 1
- [달리기 경주](https://github.com/km-kwon/CodingTest/tree/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/Level%201/%EB%8B%AC%EB%A6%AC%EA%B8%B0%20%EA%B2%BD%EC%A3%BC)

```
dictionary 자료형의 시간 복잡도를 활용하여 시간 초과 줄임
.index 보다 dictionary 자료형이 시간 복잡도 훨씬 덜함
```

- [추억 점수](https://github.com/km-kwon/CodingTest/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/Level%201/%EC%B6%94%EC%96%B5%20%EC%A0%90%EC%88%98/README.md)

```
달리기 경주에서 풀었던 문제와 비스사게 시간 복잡도를
고려해 dictionary를 사용하여 해결
dictionary를 선언할때 서로 다른 배열을 페어로 선언 => zip사용
```

- [공원산책](https://github.com/km-kwon/CodingTest/tree/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/Level%201/%EA%B3%B5%EC%9B%90%20%EC%82%B0%EC%B1%85)

```
- 너무나 브루트포스 방법만을 고민함
- 수학적 센스를 생각해보는 고민을 해봐야할듯
```

- [PCCP 1번 붕대감기](https://github.com/km-kwon/CodingTest/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/Level%201/%5BPCCP%20%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C%5D%201%EB%B2%88%20%EB%B6%95%EB%8C%80%20%EA%B0%90%EA%B8%B0/README.md)

```
for 문 사용시 range 사용 지양
index로 접근 하지 않고 i, j 한번에 사용 가능
```

---
### Level 2
- [혼자서 하는 틱택토](https://github.com/km-kwon/CodingTest/tree/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/Level%202/%ED%98%BC%EC%9E%90%EC%84%9C%20%ED%95%98%EB%8A%94%20%ED%8B%B1%ED%83%9D%ED%86%A0)

```
성공에 대해 너무 어렵게 생각함
DP를 사용하려 풀려고 했지만 너무 어렵게 풀어서 실패
결국 1시간이 넘어 답을 봤지만 생각했던 풀이가 맞았음
```

- [두 원사이의 정수쌍](https://github.com/km-kwon/CodingTest/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/Level%202/%EB%91%90%EC%9B%90%20%EC%82%AC%EC%9D%B4%EC%9D%98%20%EC%A0%95%EC%88%98%EC%8C%8D/README.md)

```
math 라이브러리 사용
외부 라이브러리가 있을 것이란 생각을 망각
수학적 생각을 심도있게 해봤어야함
```
