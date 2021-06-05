# 요약문
### 데이터 전처리와 속성

- 데이터를 확인했을 때 'Rating', 'Votes', 'Reviews' column에 결측치가 존재하여 각 속성의 median 값을 채워주었습니다.
- "Rating" column에는 숫자가 아닌 값들이 존재하여 그 값들도 median 값으로 변경해주었습니다.
- "AverageCost" column에는 "1,000" 이라는 문자열과 "for"이라는 문자열이 들어있어 이 값을 median값으로 변경해주었습니다.
- "Cuisines" column에는 여러 categories가 동시에 포함되어있어 전부 ","를 기준으로 분리해 one-hot encoding을 진행했습니다.
- "Location" column 역시 ","를 기준으로 각 도시 혹은 도로 이름으로 one-hot encoding을 진행했습니다.

### 학습 모델과 손실함수
- 학습 모델로는 Scikit-learn의 DecisionTreeRegressor을 이용했습니다.
- DecisionTreeRegressor의 손실함수 $R^2$은 $(1-\frac{u}{v})$ , where $u$ is the residual sum of squares `((y_true - y_pred) ** 2).sum()` and $v$ is the total sum of squares `((y_true - y_true.mean()) ** 2).sum()`입니다.

### 테스트 데이터에 대한 평가지표
- Mean Absolute Error (MAE) : 5.83
- Under-Prediction의 비율 : 0.16
