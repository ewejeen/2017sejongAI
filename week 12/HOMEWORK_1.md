# Sentiment Analysis - Movie Reviews



## 영화 소개

![Image](https://cdn-images-1.medium.com/max/1200/1*ErHfNzwX8oBwSbcJALSxcw.jpeg)

 *스포트라이트*는 2015년에 개봉한 미국의 드라마 영화이다. 가톨릭 교회 사제에 의한 아동 성추행을 보도한 《보스턴 글로브》 기자들의 이야기를 다루고 있다. 실화에 기반한 영화로서, 실제로 이 기사를 보도한 스포트라이트 팀은 퓰리처 상을 수상하기도 했다. 2015년 제88회 아카데미 시상식 최우수작품상, 각본상 수상작이다.



## 리뷰 수집
영화 정보 모음 사이트 [IMDb](https://www.imdb.com/) 에서 리뷰를 수집하였다. 분석의 다양성을 위해 IMDb에서 제공하는 다양한 필터를 사용하여 여러가지 성격의 리뷰를 수집하였다.



## 가설 설정
- 가설 1. 주요 단어를 소문자에서 대문자로 바꿔 쓰면 정확도 점수가 더 높아질 것이다.

- 가설 2. ‘Best’ 필터에서 더 위에 위치한 리뷰일수록 정확도 점수가 더 높을 것이다.

- 가설 3. 긍정적인 리뷰들 중, 스포일러가 포함된 리뷰는 그렇지 않은 리뷰보다 정확도 점수가 더 높을 것이다.



## 가설 설정 이유
- 가설 1: 영어로 글을 쓸 때, 의미를 강조하기 위해서 강조하고자 하는 표현을 대문자로 쓰는 경우가 있다. 예를 들어 ‘이 배우의 연기는 정말 뛰어났다.’를 영어로 쓸 때, ‘The actor’s performance was outstanding.’ 보다는 같은 문장이어도 ‘The actor’s performance was OUTSTANDING.’이라고 쓰면 문장의 의미가 더욱 강조된다. 이와 같은 현상을 sentiment analyzer에서도 잡아낼 수 있을지 시험해보기 위해 가설 1을 설정하였다.

- 가설 2: IMDb의 유저 리뷰에서는 여러가지 필터를 제공한다. 그 중 Best 필터는 ~~(추정컨대)~~ 더 많은 사용자가 ‘도움이 되었다’는 평가를 준 순으로 리뷰를 보여준다. 그러므로 더 위에 위치한 리뷰일수록 정확도 점수가 더 높을 것이라 생각했고, 이를 시험해보기 위해 가설 2를 설정하였다.

- 가설 3: IMDb는 리뷰가 스포일러를 포함할 가능성이 있는 경우 *** This review may contain spoilers *** 라는 문구를 리뷰의 첫 줄에 보여준다. 긍정적인 리뷰가 스포일러를 포함할 경우에, 영화의 내용을 예로 들면서 ‘어느 부분이 재밌었다’는 식의 보다 자세하고 명확하게 긍정적인 표현을 썼을 것이라 생각해서 가설 3을 설정하였다.



## 리뷰 선정
가설 1의 증명을 위해서 긍정적 리뷰 한 개, 부정적 리뷰 한 개를 사용하였고, 가설 2와 3의 증명을 위해서는 긍정적 리뷰 두 개를 사용하였다.



## 긍정적 리뷰

1.

Everything about this movie is outstanding -- the performances, the way the true events are handled, the cinematography. In this day of digital news, this movie makes us stand back and realize what we may lose in the way of investigative journalism as we slowly kill off print media.
The focus remains the child abuse scandal in the archdiocese in Boston. That reflects the conflict the characters face and deal with when events make them rethink the focus of their article.
The movie is riveting, though we know the outcome.


2.

It won best film, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in riveting fashion by Tom Macarthy who does not waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals.
Just brilliant.


3.

*** This review may contain spoilers ***

For me this film was beautifully tragic; by this I mean it was a fantastically acted film and gripping; but I'm disgusted and mortified that it actually happened.
It was good that the film focused on how the conspiracy into the abuse was covered up; for me it was a preference than focusing on the victims and bringing any more agony to them. It brought a tear to my eye to know the depths that this went on (and probably still does) and the number of victims that were involved. As someone who has a criminology degree with a focus on child abuse this film was particularly poignant. The end provides a list of places where it has been uncovered; this is heartbreaking. 



## 부정적 리뷰
I get why movies like this get nominated for Best Picture. Seriously though, it's just dull. There is nothing in this movie that is cinematically interesting. Spotlight could have been done as a picture book with a few sentences of dialogue per page and Mark Ruffalo's happy face or sad face plastered on top.
3 stars though just because a very interesting subject.



## 가설 검증

### 가설 1. 주요 단어를 소문자에서 대문자로 바꿔 쓰면 정확도 점수가 더 높아질 것이다.

**증명 1-1.** 긍정적 리뷰

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/1-1.py)

- 결과

```
Number of training datapoints: 1600
Number of test datapoints: 400

Accuracy of the classifier: 0.735

Top 15 most informative words:
1. outstanding
2. insulting
3. vulnerable
4. ludicrous
5. uninvolving
6. avoids
7. astounding
8. fascination
9. darker
10. anna
11. seagal
12. affecting
13. symbol
14. animators
15. idiotic

Movie review predictions:

Review: It won best film, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in riveting fashion by Tom Macarthy who does not waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals. Just brilliant.
Predicted sentiment: Positive
Probability: 0.82
```

******************************************************************************************************************************

## 가설 검증 중에 알아낸 것 
1. 결과의 윗부분에 나타나는 Accuracy와 Informative words 등의 정보는 내가 입력한 리뷰에 대한 정보가 아니고, nltk.corpus의 movie_reviews에 저장되어 있는 1000개의 positive reviews와 1000개의 negative reviews에 대한 것이다. 즉, 이 내용들은 내가 입력한 리뷰들과 아무런 관련이 없다. **그러므로 이 뒤부터는 결과 부분의 'Movie review predictions: ' 이후만 표기하겠다.**

2. threshold(한계치)로 설정한 값은 test 데이터와 training 데이터를 나누는 기준이 되는 수치인데, 어떤 것을 나타내는 지는 정확히 파악하지 못했지만, accuracy of the classifier와 각각의 probability에 영향을 준다. 

******************************************************************************************************************************


**증명 1-1-1.** best film과 just brilliant 라는 표현을 대문자로 표현해 보았다.

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/1-1-1.py)

- 결과

```
Movie review predictions:

Review: It won BEST FILM, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in riveting fashion by Tom Macarthy who does NOT waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals. JUST BRILLIANT.
Predicted sentiment: Positive
Probability: 0.77
```
> Probaility 수치가 오히려 감소한 것을 볼 수 있다.


**증명 1-1-2.** best film, just brilliant, riveting을 대문자로 표현해 보았다.

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/1-1-2.py)

- 결과
```
Movie review predictions:

Review: It won BEST FILM, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in RIVETING fashion by Tom Macarthy who does not waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals. JUST BRILLIANT.
Predicted sentiment: Negative
Probability: 0.58
```
> Sentiment가 Negative로 바뀌었으며, Probaility 수치도 감소하였다.



**증명 1-2.** 부정적 리뷰

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/1-2.py)

- 결과
```
Movie review predictions:

Review: I get why movies like this get nominated for Best Picture. Seriously though, it's just dull. There is nothing in this movie that is cinematically interesting. Spotlight could have been done as a picture book with a few sentences of dialogue per page and Mark Ruffalo's happy face or sad face plastered on top. 3 stars though just because a very interesting subject.
Predicted sentiment: Positive
Probability: 0.5
```
>분명한 부정적 리뷰임에도 sentiment가 Positive로 감지되었다.


**증명 1-2-1.** Seriously though, it’s just dull과 nothing이라는 표현을 대문자로 변경해 보았다.

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/1-2-1.py)

- 결과
```
Movie review predictions:

Review: I get why movies like this get nominated for Best Picture. SERIOUSLY THOUGH, IT'S JUST DULL. There is NOTHING in this movie that is cinematically interesting. Spotlight could have been done as a picture book with a few sentences of dialogue per page and Mark Ruffalo's happy face or sad face plastered on top. 3 stars though just because a very interesting subject.
Predicted sentiment: Positive
Probability: 0.6
```

>부정적인 리뷰이지만 부정적인 단어를 사용하기보다는 비꼬는 듯한 표현을 사용했기 때문에 감정을 정확하게 잡아내지 못한 것으로 보인다.



### 가설 2. ‘Best’ 필터에서 더 위에 위치한 리뷰일수록 정확도 점수가 더 높을 것이다.

**증명 2-1.** 더 위에 위치한 리뷰

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/2-1.py)

- 결과
```
Movie review predictions:

Review: Everything about this movie is outstanding -- the performances, the way the true events are handled, the cinematography. In this day of digital news, this movie makes us stand back and realize what we may lose in the way of investigative journalism as we slowly kill off print media. The focus remains the child abuse scandal in the archdiocese in Boston. That reflects the conflict the characters face and deal with when events make them rethink the focus of their article. The movie is riveting, though we know the outcome.
Predicted sentiment: Positive
Probability: 1.0
```


**증명 2-2** 더 아래에 위치한 리뷰

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/2-2.py)

- 결과
```
Movie review predictions:

Review: It won best film, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in riveting fashion by Tom Macarthy who does not waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals. Just brilliant.
Predicted sentiment: Positive
Probability: 0.82
```
>필터에서 위에 위치한 리뷰의 점수가 더 게 나왔다.



### 가설 3. 긍정적인 리뷰들 중, 스포일러가 포함된 리뷰는 그렇지 않은 리뷰보다 정확도 점수가 더 높을 것이다.


**증명 3-1.** 스포일러가 포함된 리뷰

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/3-1.py)

- 결과
```
Movie review predictions:

Review: *** This review may contain spoilers *** For me this film was beautifully tragic; by this I mean it was a fantastically acted film and gripping; but I'm disgusted and mortified that it actually happened. It was good that the film focused on how the conspiracy into the abuse was covered up; for me it was a preference than focusing on the victims and bringing any more agony to them. It brought a tear to my eye to know the depths that this went on (and probably still does) and the number of victims that were involved. As someone who has a criminology degree with a focus on child abuse this film was particularly poignant. The end provides a list of places where it has been uncovered; this is heartbreaking.
Predicted sentiment: Positive
Probability: 1.0
```


**증명 3-2.** 스포일러가 포함되지 않은 리뷰

- [코드](https://github.com/ewejeen/2017sejongAI/blob/master/week%2012/3-2.py)

- 결과
```
Movie review predictions:

Review: It won best film, deservedly so. This is a film that resonated with me long after I watched it. The complicated tale of the investigation of paedophile priests in Boston and the publication of it is told in riveting fashion by Tom Macarthy who does not waste a frame or a scene. I never felt the running time or in any way disbelieved any of the actors in their portrayals. Just brilliant.
Predicted sentiment: Positive
Probability: 0.82
```
>스포일러가 포함된 리뷰가 정확도 점수가 더 높은 것을 볼 수 있다.



### 가설 검증 결과
- [ ] **가설 1**: 주요 단어를 소문자에서 대문자로 바꿔 쓰면 정확도 점수가 더 높아질 것이다.

- [x] **가설 2**: ‘Best’ 필터에서 더 위에 위치한 리뷰일수록 정확도 점수가 더 높을 것이다.

- [x] **가설 3**: 긍정적인 리뷰들 중, 스포일러가 포함된 리뷰는 그렇지 않은 리뷰보다 정확도 점수가 더 높을 것이다.


### 결론
이 글에 사용된 sentiment analyzer의 코드로 영화 리뷰의 완벽한 감정 분석을 하기에는 아직 어려움이 따랐다. 이유는 1) 위에서도 밝혔듯, 윗 부분의 코드가 패키지에 저장되어 있는 영화 리뷰만을 대상으로 하므로 실제 사용자가 입력한 리뷰를 반영하지 못했고, 2) 긍정적, 부정적 의미를 동시에 내포한 단어를 제대로 파악하지 못했으며, 3) 실제 사용되는 언어의 표현을 제대로 못하는 등의 한계를 보였기 때문이다. **하지만** 몇몇 가설의 증명에서는 유의미한 결과를 보여줬으므로, 좀 더 보완된다면 실제 감정 분석에 유용하게 쓰일 수 있을 것이다.
