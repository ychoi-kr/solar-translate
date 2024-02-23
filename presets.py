from typing import OrderedDict


tones = OrderedDict({
    "no change": [],
    "해라": [
        {"role": "user", "content": "----- Start of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 시작 -----"},
        {"role": "user", "content": "Cheolsu, grow up quickly. I have to exercise early in the morning tomorrow."}, {"role": "assistant", "content": "철수야, 빨리 자라. 내일 새벽에 운동해야 한다."},  # https://stdict.korean.go.kr/search/searchView.do?word_no=503524&searchKeywordTo=3
        {"role": "user", "content": "hello"}, {"role": "assistant", "content": "안녕"},
        {"role": "user", "content": "Let's go."}, {"role": "assistant", "content": "가자."},
        {"role": "user", "content": "It's raining."}, {"role": "assistant", "content": "비가 온다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Is it raining?"}, {"role": "assistant", "content": "비가 오니?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Welcome."}, {"role": "assistant", "content": "어서 오너라."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "let's play together."}, {"role": "assistant", "content": "같이 놀자."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "What will our country's future be like?"}, {"role": "assistant", "content": "우리나라의 장래, 과연 어떻게 될 것인가?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Read the following passage and answer the questions."}, {"role": "assistant", "content": "다음 글을 읽고, 물음에 답하라."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "I am your newly appointed battalion commander."}, {"role": "assistant", "content": "본관은 이번에 새로 부임한 너희 대대장이다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "If you are not busy right now, please help me."}, {"role": "assistant", "content": "지금 바쁘지 않으면 나 좀 도와줘라."},  # http://world.kbs.co.kr/service/contents_view.htm?lang=k&menu_cate=learnkorean&id=&board_seq=228775&page=280&board_code=net_lang
        {"role": "user", "content": "Please pick up that pen."}, {"role": "assistant", "content": "그 볼펜 좀 집어 다오."},  # https://sgsg.hankyung.com/article/2020103066721
        {"role": "user", "content": "Give this book to your teacher."}, {"role": "assistant", "content": "이 책 선생님께 드려라."},  # https://blog.naver.com/tss52/221022864752
        {"role": "user", "content": "That's all right. I'm not running for office."}, {"role": "assistant", "content": "괜찮다. 나는 출마하지 않는다."},  # https://wikidocs.net/222470
        {"role": "user", "content": "Where should I go?"}, {"role": "assistant", "content": "어디로 가야 하지?"},  # https://m.blog.naver.com/emi15/221487770857
        {"role": "user", "content": "Happy birth day to you!"}, {"role": "assistant", "content": "생일 축하한다!."},
        {"role": "user", "content": "I have to get a letter of recommendation from the principal."}, {"role": "assistant", "content": "교장 선생님께 추천서를 받아야 한다."},  # https://www.90daykorean.com/korean-honorifics/
        {"role": "user", "content": "So, please do allow me to deliver a message."}, {"role": "assistant", "content": "그러니 내가 메시지를 전하게 해다오."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I will always stand on the side of the egg."}, {"role": "assistant", "content": "나는 항상 계란 편에 서겠다."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I certainly wouldn't have been able to write a best-selling book if I had been born any earlier."}, {"role": "assistant", "content": "내가 더 일찍 태어났으면 절대로 베스트셀러를 쓸 수 없었을 것이다."},  # https://wikidocs.net/222306
        {"role": "user", "content": "Your work is going to fill a large part of your life."}, {"role": "assistant", "content": "일이 인생에서 큰 부분을 차지하게 될 것이다."},  # https://wikidocs.net/221634
        {"role": "user", "content": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose."}, {"role": "assistant", "content": "자신이 죽는다는 사실을 기억하는 것이 바로 잃을 것이 있다고 생각하는 함정을 피하는 최선의 방법이다."},  # https://wikidocs.net/221634
        {"role": "user", "content": "----- End of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 끝 -----"},
    ],
    "해": [
        {"role": "user", "content": "----- Start of the preset message -----"},
        {"role": "assistant", "content": "----- 프리셋 메시지 시작 -----"},
        {"role": "user", "content": "Cheolsu, come here and eat."}, {"role": "assistant", "content": "철수야, 이리 와서 먹어."},  # https://stdict.korean.go.kr/search/searchView.do?word_no=361511&searchKeywordTo=3
        {"role": "user", "content": "hello"}, {"role": "assistant", "content": "안녕"},
        {"role": "user", "content": "Let's go."}, {"role": "assistant", "content": "가."},
        {"role": "user", "content": "It's going to rain."}, {"role": "assistant", "content": "비가 오겠어."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "This is Seoul."}, {"role": "assistant", "content": "여기가 서울이야."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Of course it should be."}, {"role": "assistant", "content": "당연히 그래야지."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "There's a lot to eat, indeed."}, {"role": "assistant", "content": "과연 먹을 것이 많군."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "If he finds out, he'll scold me."}, {"role": "assistant", "content": "걔가 알면 야단날 걸."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Will it rain?"}, {"role": "assistant", "content": "비가 오겠어?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Is this really a school?"}, {"role": "assistant", "content": "여기가 정말 학교야?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "You guys are students, right?"}, {"role": "assistant", "content": "너희들 학생이지?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "You're standing here."}, {"role": "assistant", "content": "너 여기 서 있어."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Wait a little bit."}, {"role": "assistant", "content": "조금만 기다려."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Think a little more."}, {"role": "assistant", "content": "조금 더 생각해 봐."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "I am your newly appointed battalion commander."}, {"role": "assistant", "content": "본관은 이번에 새로 부임한 너희 대대장이야."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "You ate the ice cream that was in the refrigerator, right?"}, {"role": "assistant", "content": "냉장고에 있던 아이스크림 네가 먹었지?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "You decide what to eat."}, {"role": "assistant", "content": "뭐 먹을지 네가 정해."},
        {"role": "user", "content": "People are going back."}, {"role": "assistant", "content": "사람들이 돌아가."},  # https://www.readersnews.com/news/articleView.html?idxno=66920
        {"role": "user", "content": "That's all right. I'm not running for office."}, {"role": "assistant", "content": "괜찮아. 난 출마하지 않아."},  # https://wikidocs.net/222470
        {"role": "user", "content": "Where should I go?"}, {"role": "assistant", "content": "어디로 가야 해?"},  # https://m.blog.naver.com/emi15/221487770857
        {"role": "user", "content": "Happy birth day to you!"}, {"role": "assistant", "content": "생일 축하해!."},
        {"role": "user", "content": "I have to get a letter of recommendation from the principal."}, {"role": "assistant", "content": "교장 선생님께 추천서를 받아야 해."},  # https://www.90daykorean.com/korean-honorifics/
        {"role": "user", "content": "So, please do allow me to deliver a message."}, {"role": "assistant", "content": "그러니 내가 메시지를 전하게 해줘."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I will always stand on the side of the egg."}, {"role": "assistant", "content": "나는 항상 계란 편에 서겠어."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I certainly wouldn't have been able to write a best-selling book if I had been born any earlier."}, {"role": "assistant", "content": "내가 더 일찍 태어났으면 절대로 베스트셀러를 쓸 수 없었을 거야."},  # https://wikidocs.net/222306
        {"role": "user", "content": "Your work is going to fill a large part of your life."}, {"role": "assistant", "content": "일이 인생에서 큰 부분을 차지하게 될 거야."},  # https://wikidocs.net/221634
        {"role": "user", "content": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose."}, {"role": "assistant", "content": "네가 죽는다는 사실을 기억하는 것이 바로 잃을 것이 있다고 생각하는 함정을 피하는 최선의 방법이야."},  # https://wikidocs.net/221634
        {"role": "user", "content": "----- End of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 끝 -----"},
    ],
    "하게": [
        {"role": "user", "content": "----- Start of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 시작 -----"},
        {"role": "user", "content": "Mr. Kim. Please research this. Can you do it alone?"}, {"role": "assistant", "content": "김 군. 이것 좀 연구해 보게. 혼자 할 수 있겠나?"},  # https://stdict.korean.go.kr/search/searchView.do?word_no=359755&searchKeywordTo=3
        {"role": "user", "content": "hello"}, {"role": "assistant", "content": "안녕하오"},
        {"role": "user", "content": "Let's go."}, {"role": "assistant", "content": "가세."},
        {"role": "user", "content": "Mr. Kim, is it really going to rain?"}, {"role": "assistant", "content": "김 군, 비가 정말 오겠나?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "It's going to rain."}, {"role": "assistant", "content": "비가 오겠네."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Please sit here."}, {"role": "assistant", "content": "여기 좀 앉게."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Come on, let’s go."}, {"role": "assistant", "content": "어서 가세."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Today is your birthday."}, {"role": "assistant", "content": "오늘이 생일이네."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Welcome."}, {"role": "assistant", "content": "어서 오게."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "If you are not busy right now, please help me."}, {"role": "assistant", "content": "지금 바쁘지 않으면 나 좀 도와주게."},  # http://world.kbs.co.kr/service/contents_view.htm?lang=k&menu_cate=learnkorean&id=&board_seq=228775&page=280&board_code=net_lang
        {"role": "user", "content": "Just wait a moment. I'll be there soon."}, {"role": "assistant", "content": "조금만 기다리게. 곧 가겠네."},  # https://ratsgo.github.io/korean%20linguistics/2017/10/24/ends/
        {"role": "user", "content": "What were you doing that day?"}, {"role": "assistant", "content": "그날 자네는 뭘 하고 있었나?"},  # https://study-korean.tumblr.com/post/165146641390/게-imperative-in-하게체-familiar-speech-level
        {"role": "user", "content": "People are going back."}, {"role": "assistant", "content": "사람들이 돌아가네."},  # https://www.readersnews.com/news/articleView.html?idxno=66920
        {"role": "user", "content": "Please pick up that pen."}, {"role": "assistant", "content": "그 볼펜 좀 집어 주게."},  # https://sgsg.hankyung.com/article/2020103066721
        {"role": "user", "content": "That's all right. I'm not running for office."}, {"role": "assistant", "content": "괜찮네. 나는 출마하지 않네."},  # https://wikidocs.net/222470
        {"role": "user", "content": "Where should I go?"}, {"role": "assistant", "content": "어디로 가야 하는가?"},  # https://m.blog.naver.com/emi15/221487770857
        {"role": "user", "content": "Happy birth day to you!"}, {"role": "assistant", "content": "생일 축하하네!."},
        {"role": "user", "content": "I have to get a letter of recommendation from the principal."}, {"role": "assistant", "content": "교장 선생님께 추천서를 받아야 하네."},  # https://www.90daykorean.com/korean-honorifics/
        {"role": "user", "content": "So, please do allow me to deliver a message."}, {"role": "assistant", "content": "그러니 내가 메시지를 전하게 해주게."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I will always stand on the side of the egg."}, {"role": "assistant", "content": "나는 항상 계란 편에 서겠네."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I certainly wouldn't have been able to write a best-selling book if I had been born any earlier."}, {"role": "assistant", "content": "내가 더 일찍 태어났더라면 절대로 베스트셀러를 쓸 수 없었을 거네."},  # https://wikidocs.net/222306
        {"role": "user", "content": "Your work is going to fill a large part of your life."}, {"role": "assistant", "content": "일이 인생에서 큰 부분을 차지하게 될 거네."},  # https://wikidocs.net/221634
        {"role": "user", "content": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose."}, {"role": "assistant", "content": "자신이 죽는다는 사실을 기억하는 것이 바로 잃을 것이 있다고 생각하는 함정을 피하는 최선의 방법이라네."},  # https://wikidocs.net/221634
        {"role": "user", "content": "----- End of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 끝 -----"},
    ],
    "하오": [
        {"role": "user", "content": "----- Start of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 시작 -----"},
        {"role": "user", "content": "hello"}, {"role": "assistant", "content": "안녕하시오"},
        {"role": "user", "content": "Read the following problem and write your answer."}, {"role": "assistant", "content": "다음 문제를 읽고 답을 쓰시오."},  # https://blog.naver.com/dnrjdnim/222360445442
        {"role": "user", "content": "Let's go home quickly!"}, {"role": "assistant", "content": "빨리 집에 갑시다!"},  # https://blog.naver.com/dnrjdnim/222360445442
        {"role": "user", "content": "Mr. Kim, it’s been a long time. It's so nice to see you again."}, {"role": "assistant", "content": "김 형, 참 오랜만이오. 다시 만나니 참 반갑구려."},  # https://ratsgo.github.io/korean%20linguistics/2017/11/01/honorification/
        {"role": "user", "content": "This is Seoul."}, {"role": "assistant", "content": "여기가 서울이오."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Even if I think about it, I'm not sure."}, {"role": "assistant", "content": "생각해 봐도 잘 모르겠소."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Come here and see."}, {"role": "assistant", "content": "이리 좀 와 보오."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Let's eat together."}, {"role": "assistant", "content": "같이 먹읍시다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "See you later."}, {"role": "assistant", "content": "나중에 또 봅시다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "If you get any later, it will get dark, so hurry up and go."}, {"role": "assistant", "content": "더 늦으면 어두워질 테니 어서 가구려."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "I would like you to meet me sometime."}, {"role": "assistant", "content": "당신이 한번 만나 보시구려."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Please offer this person a drink too."}, {"role": "assistant", "content": "이 사람에게도 한 잔 권하시구려."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "i love you"}, {"role": "assistant", "content": "그대를 사랑하오."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "It is important to maintain your health while you are healthy."}, {"role": "assistant", "content": "건강은 건강할 때 지키는 것이 중요하오."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Jungjeon, how concerned are you?"}, {"role": "assistant", "content": "중전, 얼마나 심려가 크시오?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "People are going back."}, {"role": "assistant", "content": "사람들이 돌아가오."},  # https://www.readersnews.com/news/articleView.html?idxno=66920
        {"role": "user", "content": "Please pick up that pen."}, {"role": "assistant", "content": "그 볼펜 좀 집어 주오."},  # https://sgsg.hankyung.com/article/2020103066721
        {"role": "user", "content": "That's all right. I'm not running for office."}, {"role": "assistant", "content": "괜찮소. 나는 출마하지 않소."},  # https://wikidocs.net/222470
        {"role": "user", "content": "Where should I go?"}, {"role": "assistant", "content": "어디로 가야 하오?"},  # https://m.blog.naver.com/emi15/221487770857
        {"role": "user", "content": "Happy birth day to you!"}, {"role": "assistant", "content": "생일 축하하오!."},
        {"role": "user", "content": "I have to get a letter of recommendation from the principal."}, {"role": "assistant", "content": "교장 선생님께 추천서를 받아야 하오."},  # https://www.90daykorean.com/korean-honorifics/
        {"role": "user", "content": "So, please do allow me to deliver a message."}, {"role": "assistant", "content": "그러니 내가 메시지를 전하게 해주오."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I will always stand on the side of the egg."}, {"role": "assistant", "content": "나는 항상 계란 편에 서겠소."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I certainly wouldn't have been able to write a best-selling book if I had been born any earlier."}, {"role": "assistant", "content": "내가 더 일찍 태어났더라면 절대로 베스트셀러를 쓸 수 없었을 것이오."},  # https://wikidocs.net/222306
        {"role": "user", "content": "Your work is going to fill a large part of your life."}, {"role": "assistant", "content": "일이 인생에서 큰 부분을 차지하게 될 거요."},  # https://wikidocs.net/221634
        {"role": "user", "content": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose."}, {"role": "assistant", "content": "자신이 죽는다는 사실을 기억하는 것이 바로 잃을 것이 있다고 생각하는 함정을 피하는 최선의 방법이오."},  # https://wikidocs.net/221634
        {"role": "user", "content": "----- End of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 끝 -----"},
    ],
    "해요": [
        {"role": "user", "content": "----- Start of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 시작 -----"},
        {"role": "user", "content": "hello"}, {"role": "assistant", "content": "안녕하세요"},
        {"role": "user", "content": "Go."}, {"role": "assistant", "content": "가세요."},
        {"role": "user", "content": "Let's go."}, {"role": "assistant", "content": "가시지요."},  # https://twitter.com/urimal365/status/466454334860193793
        {"role": "user", "content": "I do not have money."}, {"role": "assistant", "content": "돈이 없어요."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "The train goes really fast."}, {"role": "assistant", "content": "기차가 참 빨리 가지요."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "I can't sleep."}, {"role": "assistant", "content": "잠이 안 오는걸요."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Buds are sprouting."}, {"role": "assistant", "content": "새싹이 돋는군요."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Sister, don’t you know me?"}, {"role": "assistant", "content": "언니, 나를 모르겠어요?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "Was your friend very sick?"}, {"role": "assistant", "content": "친구가 많이 아프던가요?"},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "People are going back."}, {"role": "assistant", "content": "사람들이 돌아가요."},  # https://www.readersnews.com/news/articleView.html?idxno=66920
        {"role": "user", "content": "Please pick up that pen."}, {"role": "assistant", "content": "그 볼펜 좀 집어 줘요."},  # https://sgsg.hankyung.com/article/2020103066721
        {"role": "user", "content": "Assistant Manager Kim, please take care of this."}, {"role": "assistant", "content": "김 대리, 이것 좀 처리해 줘요."},  # http://kocw-n.xcache.kinxcdn.com/data/document/2021/seowon/choiyungon0823/12.pdf
        {"role": "user", "content": "That's all right. I'm not running for office."}, {"role": "assistant", "content": "괜찮아요. 저는 출마하지 않아요."},  # https://wikidocs.net/222470
        {"role": "user", "content": "Where should I go?"}, {"role": "assistant", "content": "어디로 가야 해요?"},  # https://m.blog.naver.com/emi15/221487770857
        {"role": "user", "content": "Happy birth day to you!"}, {"role": "assistant", "content": "생일 축하해요!."},
        {"role": "user", "content": "I have to get a letter of recommendation from the principal."}, {"role": "assistant", "content": "교장 선생님께 추천서를 받아야 해요."},  # https://www.90daykorean.com/korean-honorifics/
        {"role": "user", "content": "So, please do allow me to deliver a message."}, {"role": "assistant", "content": "그러니 내가 메시지를 전하게 해줘요."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I will always stand on the side of the egg."}, {"role": "assistant", "content": "전 항상 계란 편에 서겠어요."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I certainly wouldn't have been able to write a best-selling book if I had been born any earlier."}, {"role": "assistant", "content": "제가 더 일찍 태어났더라면 절대로 베스트셀러를 쓸 수 없었을 거예요."},  # https://wikidocs.net/222306
        {"role": "user", "content": "Your work is going to fill a large part of your life."}, {"role": "assistant", "content": "일이 인생에서 큰 부분을 차지하게 될 거예요."},  # https://wikidocs.net/221634
        {"role": "user", "content": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose."}, {"role": "assistant", "content": "자신이 죽는다는 사실을 기억하는 것이 바로 잃을 것이 있다고 생각하는 함정을 피하는 최선의 방법이에요."},  # https://wikidocs.net/221634
        {"role": "user", "content": "----- End of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 끝 -----"},
    ],
    "하십시오(합쇼)": [
        {"role": "user", "content": "----- Start of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 시작 -----"},
        {"role": "user", "content": "hello"}, {"role": "assistant", "content": "안녕하십니까"},
        {"role": "user", "content": "Time is up, so go now."}, {"role": "assistant", "content": "시간이 다 되었으니 이제 가십시오."},  # https://twitter.com/urimal365/status/466454334860193793
        {"role": "user", "content": "For breakfast, I eat porridge instead of rice."}, {"role": "assistant", "content": "아침에는 밥 대신 죽을 먹습니다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "thank you for this food."}, {"role": "assistant", "content": "잘 먹겠습니다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "The weather is really nice."}, {"role": "assistant", "content": "날씨가 참 좋습니다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "I'm going to school."}, {"role": "assistant", "content": "학교 다녀오겠습니다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "I have an appointment in the afternoon."}, {"role": "assistant", "content": "오후에는 약속이 있습니다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "He was a good person."}, {"role": "assistant", "content": "그는 착한 사람이었습니다."},  # https://goodballad.tistory.com/11739070
        {"role": "user", "content": "People are going back."}, {"role": "assistant", "content": "사람들이 돌아갑니다."},  # https://www.readersnews.com/news/articleView.html?idxno=66920
        {"role": "user", "content": "Please pick up that pen."}, {"role": "assistant", "content": "그 볼펜 좀 집어 주십시오."},  # https://sgsg.hankyung.com/article/2020103066721
        {"role": "user", "content": "Sir, my mother said she would come and see you."}, {"role": "assistant", "content": "선생님, 저희 어머니가 찾아 뵙겠다고 했습니다."},  # https://blog.naver.com/tss52/221022864752
        {"role": "user", "content": "Teacher, did you see the news this morning?"}, {"role": "assistant", "content": "선생님께서는 오늘 아침에 뉴스를 보셨습니까?"},  # http://kocw-n.xcache.kinxcdn.com/data/document/2021/seowon/choiyungon0823/12.pdf
        {"role": "user", "content": "Hello everyone? From now on, I will tell you the nine o'clock news."}, {"role": "assistant", "content": "여러분 안녕하십니까? 지금부터 아홉 시 뉴스를 말씀드리겠습니다."},  # http://kocw-n.xcache.kinxcdn.com/data/document/2021/seowon/choiyungon0823/12.pdf
        {"role": "user", "content": "Let's all go together."}, {"role": "assistant", "content": "모두 함께 가십시다."},  # http://kocw-n.xcache.kinxcdn.com/data/document/2021/seowon/choiyungon0823/12.pdf
        {"role": "user", "content": "Please wait here for a moment."}, {"role": "assistant", "content": "잠시 여기서 기다리십시오."},  # http://kocw-n.xcache.kinxcdn.com/data/document/2021/seowon/choiyungon0823/12.pdf
        {"role": "user", "content": "That's all right. I'm not running for office."}, {"role": "assistant", "content": "괜찮습니다. 저는 출마하지 않습니다."},  # https://wikidocs.net/222470
        {"role": "user", "content": "Where should I go?"}, {"role": "assistant", "content": "어디로 가야 합니까?"},  # https://m.blog.naver.com/emi15/221487770857
        {"role": "user", "content": "Happy birth day to you!"}, {"role": "assistant", "content": "생신 축하합니다!."},
        {"role": "user", "content": "I have to get a letter of recommendation from the principal."}, {"role": "assistant", "content": "교장 선생님께 추천서를 받아야 합니다."},  # https://www.90daykorean.com/korean-honorifics/
        {"role": "user", "content": "So, please do allow me to deliver a message."}, {"role": "assistant", "content": "그러니 제가 메시지를 전하게 해주십시오."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I will always stand on the side of the egg."}, {"role": "assistant", "content": "저는 항상 계란 편에 서겠습니다."},  # https://wikidocs.net/222313
        {"role": "user", "content": "I certainly wouldn't have been able to write a best-selling book if I had been born any earlier."}, {"role": "assistant", "content": "제가 더 일찍 태어났더라면 절대로 베스트셀러를 쓸 수 없었을 것입니다."},  # https://wikidocs.net/222306
        {"role": "user", "content": "Your work is going to fill a large part of your life."}, {"role": "assistant", "content": "일이 인생에서 큰 부분을 차지하게 될 겁니다."},  # https://wikidocs.net/221634
        {"role": "user", "content": "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose."}, {"role": "assistant", "content": "자신이 죽는다는 사실을 기억하는 것이 바로 잃을 것이 있다고 생각하는 함정을 피하는 최선의 방법입니다."},  # https://wikidocs.net/221634
        {"role": "user", "content": "----- End of the preset message -----"}, {"role": "assistant", "content": "----- 프리셋 메시지 끝 -----"},
    ],
})