﻿#Debug
init python:
    import random
#EndDebug

# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('수뭉이', color="#6ac1e4")
define me = Character("[name]")

screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5

# 점수 변수 설정
default score = 0

# 장소, 대상, 옷차림 변수 설정
default 장소 = ""
default 대상 = ""
default 옷차림 = ""

# 화면에 점수 출력
screen score_display():
    text "Score: [score]" align (0.98, 0.02)  # 오른쪽 상단에 점수를 표시   

#Debug-----------------------------------------------------------------------------

label debug:
    "timeout_label is None"
    return

default timeout_time = 5.0

screen debug_TimerScreen(timeout_label=None):
    default pass_time = 5.0
    timer 0.1 repeat True action SetScreenVariable("pass_time", pass_time - 0.1)

    bar:
        xalign 0.5
        ypos 100
        xsize 740
        value AnimatedValue(old_value=0.0, value=pass_time, range=timeout_time)  

    if (timeout_label is not None):
        if (2.0 < pass_time):
            text "[pass_time:.1f]s" xpos 0.1 ypos 0.1
        elif (0.0 < pass_time):
            text "{color=#FF0000}{b}[pass_time:.1f]s{/b}{/color}" xpos 0.1 ypos 0.1
        else:
            $ pass_time = timeout_time
            timer 0.01 action Jump(timeout_label)
    else:
        timer 0.01 action Jump(label_none)

#EndDebug----------------------------------------------------------------------------  

# 점수변동 구현완료
# 타이머 구현완료
# 캐릭터 이름 입력 구현완료
# 선택지 구현완료
# 엔딩 구현완료

# 여기에서부터 게임이 시작합니다.
label start:

    # 점수 표시 화면을 항상 띄움
    show screen score_display

    "시작 전 안내사항 (대화창을 클릭하거나 Enter를 누를 시 다음으로 넘어갑니다.)"
    "플레이어가 선택하는 것에 따라 최종 점수 및 결과가 달라집니다."
    "진행 중 현재 점수는 우측 상단의 Score에서 확인할 수 있습니다."
    "중간에 나오는 선택지는 상하 방향키 + Enter 혹은 마우스로 선택 가능합니다."
    "대화창 클릭 후 기다리시면 곧 게임을 시작합니다."
    scene black with dissolve

    e "맨날 과잠만 입고 있으니까 이젠 좀 질리네..."

    e "이번엔 기분전환도 할 겸, 학교 밖으로 나가 보는 거야!"

    e "그러려면 거기에 맞는 옷을 잘 골라 입어야겠지?"

    e "슴우야! 혹시 날 좀 도와줄 수 있을까?"

menu:
    "너 나 알아?":
        e "음...?"
    "도를 믿으세요?":
        e "오...?"
    "옷이 뭐야?":
        e "아...?"
    "난 오늘 핫six를 6개 마셨어.":
        e "예...?"
    "그리고 3일 동안 단 1시간도 못 잤지.":
        e "뭐라고...?"

e "아니이이, 그러지 말구...부탁할게."
e "아! 그 전에, 혹시 이름이 뭐야?"

# 플레이어 이름 입력받기
$ init_name = renpy.call_screen("set_name", title="슴우의 이름은?", init_name="핫six를 6개 마신 슴우")
$ me = Character(init_name, color="#b1f1cc")

e "아아, 그래 [init_name]야! 앞으로 그렇게 부르면 돼?"

menu:
    "응 그렇게 불러.":
        e "알겠어 [init_name]야~"
    "아니?":
        e "알겠, ...어?라... 그럼 진짜 이름이 뭐야?"
        $ init_name = renpy.call_screen("set_name", title="슴우의 이름은?", init_name="3일 동안 단 1시간도 못 잔 슴우")
        $ me = Character(init_name, color="#b1f1cc")

        e "이번엔 진짜지? ...좋아, [init_name]야!"
e "그...래서 혹시 날 도와줄 수 있어?"


# 아래로는 선택지입니다. 플레이어가 선택하는 것에 따라 최종 점수 및 결과가 달라집니다.

menu:
    "좋아!" :
        e "앗싸! 고마워!"
        e "근데 내가 학교 밖에 안 나간 지 좀 돼서 그런데..."
        e "이것저것 물어보고 싶은 게 많거든..."
        me "(불길하다...)"

        menu: 
            "얼마나?" :
                e "음... 좀 많은데... 한 100가지 정도?"
                me "불길하다 했다..."
                e "응? 뭐라고?"
                me "아니야."
                me "아무튼 그래서..."
                menu :
                    "조금이 아닌 것 같은데" :
                        e "으엥!"
                    "줄여" :
                        e "으엥!"
                    "혼자 할 수 있다는 거지?" :
                        e "으엥!"
                e "어어어 아니아니, 알겠어 그러면 3가지 정도로 줄여볼게!"
                me "좋은 생각이야."
                e "대신에 너도 나처럼 100가지가 나와도 3가지로 바로바로 추려야 하는 거다?!"
                me "뭐 얼마나 어렵다고. 알겠어."
                me "아니 뭐라고?"
                e "농담이야."
                e "그러며언 있지, 내가 앞으로 3가지를 물어볼 건데, 가장 좋을 것 같은 선택을 해주기만 하면 돼!"
                e "어때! 쉽지?"
                menu:
                    "쉽네!" :
                        e "좋아! 그럼 바로 물어볼게. 참고로 빠르게 대답해줘야 해, 고민하기엔 시간이 좀 촉박해서 널 부른 거거든!"
                        me "시간 제한이 있는 거야?"
                        e "응! 딱 3초 동안만 시간을 줄 건데, 그 안에 빠르게 대답해주면 고마울 거야."
                        me "아 좀 그런데... 나도 생각이 필요해."
                        e "그러면 {b}{color=#6ac1e4}5초 동안{/color}{/b} 기다릴게. 5초가 지나면 기다리다가 지쳐서 {b}{color=#6ac1e4}아무거나 막 입어{/color}{/b}버릴지도 몰라."
                        me "너 되게 참을성이 없구나."
                        e "그야, 모처럼 외출인데 시간은 한정적이고 고민하는데에 쓰는 시간이 너무 아깝잖아?"
                        me "(묘하게 합리적이다...)"
                        e "이제 물어볼게!"
                        me "이렇게 바로? ...앗"
                    "어려운데..." :
                        e "그럼 내가 힌트를 조금 줄게. 아니면 다시 설명해줄까?"
                        menu:
                            "힌트를 줘." :
                                e "그래 좋아."
                                e "우선 나는 {b}{color=#6ac1e4}장소, 대상, 옷차림 순서{/color}{/b}로 [init_name]한테 질문을 할 거야."
                                e "그러면 내가 일단은 들어본 다음에 마음에 들면 그렇게 하고, 아니면 다른 고려를 해볼거야."
                                e "이해가 됐지?"
                                me "응! 이해됐어."
                            "다시 설명해줘." :
                                e "알겠어 다시 설명해줄게."
                                e "내가 앞으로 {b}{color=#6ac1e4}각각 다른 3가지{/color}{/b}를 물어볼 건데, {b}{color=#6ac1e4}가장 좋을 것 같은 선택을 빠르게{/color}{/b} 답해주기만 하면 돼!"

                            "아니야 이해했어." :
                                e "그렇구나! 음음."
                        e "좋아! 그럼 바로 물어볼게. 참고로 빠르게 대답해줘야 해, 고민하기엔 시간이 좀 촉박해서 널 부른 거거든!"
                        me "시간 제한이 있는 거야?"
                        e "응! 딱 3초 동안만 시간을 줄 건데, 그 안에 빠르게 대답해주면 고마울 거야."
                        me "아 좀 그런데... 나도 생각이 필요해."
                        e "그러면 {b}{color=#6ac1e4}5초 동안{/color}{/b} 기다릴게. 5초가 지나면 기다리다가 지쳐서 {b}{color=#6ac1e4}아무거나 막 입어{/color}{/b}버릴지도 몰라."
                        me "너 되게 참을성이 없구나."
                        e "그야, 모처럼 외출인데 시간은 한정적이고 고민하는데에 쓰는 시간이 너무 아깝잖아?"
                        me "(묘하게 합리적이다...)"
                        e "이제 물어볼게!"
                        me "이렇게 바로? ...앗"
                
            "관둬 안 해" :
                e "힝... 너무해."
                jump bad_ending
    
    "싫어!" :
        e "장난이지?"

        menu:
            "장난이야!" :
                e "다행이다!!! 고마워!"
            "장난 아닌데~ 장난 아닌데~":
                e "인성이... 왜 그래?"
                jump bad_ending

        e "그러며언 있지, 내가 앞으로 3가지를 물어볼 건데, 가장 좋을 것 같은 선택을 해주기만 하면 돼!"
        e "어때! 쉽지?"
        menu:
            "쉽네!" :
                e "좋아! 그럼 바로 물어볼게. 참고로 빠르게 대답해줘야 해, 고민하기엔 시간이 좀 촉박해서 널 부른 거거든!"
                me "시간 제한이 있는 거야?"
                e "응! 딱 3초 동안만 시간을 줄 건데, 그 안에 빠르게 대답해주면 고마울 거야."
                me "아 좀 그런데... 나도 생각이 필요해."
                e "그러면 {b}5초 동안{/b} 기다릴게. 5초가 지나면 기다리다가 지쳐서 아무거나 막 입어버릴지도 몰라."
                me "너 되게 참을성이 없구나."
                e "그야, 모처럼 외출인데 시간은 한정적이고 고민하는데에 쓰는 시간이 너무 아깝잖아?"
                me "(묘하게 합리적이다...)"
                e "이제 물어볼게!"
            "어려운데..." :
                e "그럼 내가 힌트를 조금 줄게. 아니면 다시 설명해줄까?"
                menu:
                    "힌트를 줘." :
                        e "그래 좋아."
                        e "우선 나는 {b}장소, 대상, 옷차림 순서{/b}로 [init_name]한테 질문을 할 거야."
                        e "그러면 내가 일단은 들어본 다음에 마음에 들면 그렇게 하고, 아니면 다른 고려를 해볼거야."
                        e "이해가 됐지?"
                        me "응! 이해됐어."
                    "다시 설명해줘." :
                        e "알겠어 다시 설명해줄게."
                        e "내가 앞으로 {b}각각 다른 3가지{/b}를 물어볼 건데, {b}가장 좋을 것 같은 선택을 빠르게{/b} 답해주기만 하면 돼!"
                    "아니야 이해했어." :
                        e "그렇구나! 음음."
                e "좋아! 그럼 바로 물어볼게. 참고로 빠르게 대답해줘야 해, 고민하기엔 시간이 좀 촉박해서 널 부른 거거든!"
                me "시간 제한이 있는 거야?"
                e "응! 딱 3초 동안만 시간을 줄 건데, 그 안에 빠르게 대답해주면 고마울 거야."
                me "아 좀 그런데... 나도 생각이 필요해."
                e "그러면 {b}5초 동안{/b} 기다릴게. 5초가 지나면 기다리다가 지쳐서 아무거나 막 입어버릴지도 몰라."
                me "너 되게 참을성이 없구나."
                e "그야, 모처럼 외출인데 시간은 한정적이고 고민하는데에 쓰는 시간이 너무 아깝잖아?"
                me "(묘하게 합리적이다...)"
                e "이제 물어볼게!"

#Debug-------------------------------------------------------------------------------------------------------------
show screen debug_TimerScreen(random.choice(["club", "libr", "hof", "cafe"]))
#EndDebug----------------------------------------------------------------------------------------------------------

menu:
    "어떤 장소로 갈까?"

    "클럽":
        label club:
        hide screen debug_TimerScreen
        $ 장소 = "클럽"
        e "그래! 가끔은 클럽에 가서 신나게 춤추다 오는 것도 좋지!"

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["club_fam", "club_fri", "club_lov", "club_pub"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "어떤 사람과 함께 갈까?"

            "가족":
                label club_fam:
                hide screen debug_TimerScreen
                $ 대상 = "가족"
                e "가족...이랑 클럽을 간다고? 뭐, 그럴 수 있지..." # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "친구":
                label club_fri:
                hide screen debug_TimerScreen
                $ 대상 = "친구"
                e "좋아, 당장 친구한테 같이 가자고 연락해 봐야지!" # +3점
                $ score += 3
                "점수가 3점 올랐습니다."

            "연인":
                label club_lov:
                hide screen debug_TimerScreen
                $ 대상 = "연인"
                e "으음... 말 꺼내면 큰일날 것 같은데. 그래, 같이 가서 즐겁게 놀다 오자고 해야지!" # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "공적관계":
                label club_pub:
                hide screen debug_TimerScreen
                $ 대상 = "공적관계"
                e "뭐?" with vpunch
                e "...좋은 생각은 아닌 것 같아, 생각해보자... 교수님이랑 클럽...? 으음." # -3점
                $ score -= 3
                "점수가 3점 내려갔습니다."

        "현재 점수는 [score]점 입니다."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["club_sunny", "club_cloudy", "club_rain", "club_snow"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "오늘 날씨가 어떻지?"

            "맑음":
                label club_sunny:
                hide screen debug_TimerScreen
                e "날이 엄청 맑아! 햇빛도 좋고, 놀러가기 딱 좋은 날씨네." # +3점
                $ score += 3
                "점수가 3점 올랐습니다."

            "흐림":
                label club_cloudy:
                hide screen debug_TimerScreen
                e "날이 조금 흐리긴 한데, 딱히 비나 눈이 올 것 같진 않아." # 0점
                "점수에 변동이 없습니다."

            "비":
                label club_rain:
                hide screen debug_TimerScreen
                e "모처럼 오랜만에 놀러가는데 하필이면 비가 오네." #-1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

            "눈":
                label club_snow:
                hide screen debug_TimerScreen
                e "엥! 벌써 눈이 온다고? 지구가 망하긴 했구나." #-1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

        "현재 점수는 [score]점 입니다."

    # 도서관
    "도서관":
        label libr:
        hide screen debug_TimerScreen
        $ 장소 = "도서관"
        e "오! 도서관에서 공부도 하고, 책도 읽으면 좋겠다."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["lib_fam", "lib_fri", "lib_lov", "lib_pub"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "어떤 사람과 함께 갈까?"

            "가족":
                label lib_fam:
                hide screen debug_TimerScreen
                $ 대상 = "가족"
                e "가족이랑 도서관이라! 시간이 맞으려나." # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "친구":
                label lib_fri:
                hide screen debug_TimerScreen
                $ 대상 = "친구"
                e "전공 공부 같이 하자고 연락해 봐야겠다." # +3점
                $ score += 3
                "점수가 3점 올랐습니다."

            "연인":
                label lib_lov:
                hide screen debug_TimerScreen
                $ 대상 = "연인"
                e "도서관 데이트 너무 좋지~" # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "공적관계":
                label lib_pub:
                hide screen debug_TimerScreen
                $ 대상 = "공적관계"
                e "모여서 팀플을 하는 것도 좋겠다." # +3점
                $ score += 3
                "점수가 3점 올랐습니다."

        "현재 점수는 [score]점 입니다."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["lib_sunny", "lib_cloudy", "lib_rain", "lib_snow"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "오늘 날씨가 어떻지?"

            "맑음":
                label lib_sunny:
                hide screen debug_TimerScreen
                e "날이 엄청 맑아! 햇빛도 좋고, 따사롭게 공부에 집중할 수 있는 환경이겠다." # +3점
                $ score += 3
                "점수가 3점 올랐습니다."

            "흐림":
                label lib_cloudy:
                hide screen debug_TimerScreen
                e "날이 조금 흐리긴 한데, 딱히 비나 눈이 올 것 같진 않아." # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "비":
                label lib_rain:
                hide screen debug_TimerScreen
                e "모처럼 오랜만에 도서관에 가는데 비가 오네. 흐리고 눅눅해서 별론데." # -1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

            "눈":
                label lib_snow:
                hide screen debug_TimerScreen
                e "엥! 벌써 눈이 온다고? 지구가 망하긴 했구나." # -1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

        "현재 점수는 [score]점 입니다."

    # 술집
    "술집":
        label hof:
        hide screen debug_TimerScreen
        $ 장소 = "술집"
        e "술 한 잔 하면서 피로를 푸는 것도 좋은 선택인 것 같아."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["pub_fam", "pub_fri", "pub_lov", "pub_pub"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "어떤 사람과 함께 갈까?"

            "가족":
                label pub_fam:
                hide screen debug_TimerScreen
                $ 대상 = "가족"
                e "가족이 다 같이 모여서 술 한 잔 하는 것도 좋지. 아 나 근데 우리 아빠 감당 안 되는데..." # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "친구":
                label pub_fri:
                hide screen debug_TimerScreen
                $ 대상 = "친구"
                e "아 친구들 불러서 술 마시자고 할까? 너무 좋아! 완전 달리는 거야!" # +3점
                $ score += 3
                "점수기 3점 올랐습니다."

            "연인":
                label pub_lov:
                hide screen debug_TimerScreen
                $ 대상 = "연인"
                e "둘이서 느긋하게 얘기하면서 술 한 잔 하자고 해야지!" # +1점
                $ score += 1
                "점수가 1점 올랐습니다."

            "공적관계":
                label pub_pub:
                hide screen debug_TimerScreen
                $ 대상 = "공적관계"
                e "으악, 회식같아. 별로야." # -3점
                $ score -= 3
                "점수가 3점 내려갔습니다."

        "현재 점수는 [score]점 입니다."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["pub_sunny", "pub_cloudy", "pub_rain", "pub_snow"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "오늘 날씨가 어떻지?"

            "맑음":
                label pub_sunny:
                hide screen debug_TimerScreen
                e "날 되게 좋다! 기분이 좋아." # +3점
                $ score += 3
                "점수기 3점 올랐습니다."

            "흐림":
                label pub_cloudy:
                hide screen debug_TimerScreen
                e "날이 좀 흐려서 다운되는데, 뭐 크게 상관없을 거 같아." # 0점
                "점수에 변동이 없습니다."

            "비":
                label pub_rain:
                hide screen debug_TimerScreen
                e "술집 가는 길에 비 맞아도 기분 별로일 것 같은데." # -1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

            "눈":
                label pub_snow:
                hide screen debug_TimerScreen
                e "눈 맞으면서 가는 술집이라... 분위기는 좋은데 너무 추울 거야." # -1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

        "현재 점수는 [score]점 입니다."
        

    "카페":
        label cafe:
        hide screen debug_TimerScreen
        $ 장소 = "카페"
        e "헉! 수업때문에 테이크아웃은 자주 해봤는데, 매장을 이용하는 건 오랜만이야."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["cafe_fam", "cafe_fri", "cafe_lov", "cafe_pub"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "어떤 사람과 함께 갈까?"

            "가족" :
                label cafe_fam:
                hide screen debug_TimerScreen
                $ 대상 = "가족"
                e "학교 다니느라 바빠서 요즘 통 대화를 못했지." # +3점
                $ score += 3
                "점수기 3점 올랐습니다."

            "친구" :
                label cafe_fri:
                hide screen debug_TimerScreen
                $ 대상 = "친구"
                e "걔네가 카페를 좋아할까?" # -1점
                $ score -= 1
                "점수기 1점 내려갔습니다."

            "연인" :
                label cafe_lov:
                hide screen debug_TimerScreen
                $ 대상 = "연인"
                e "악, 사진 찍느라 바쁘겠네 또." # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "공적관계" :
                label cafe_pub:
                hide screen debug_TimerScreen
                $ 대상 = "공적관계"
                e "하... 이번에는 또 어떤 프로젝트 얘기를 하려나." # -3점
                $ score -= 3
                "점수기 3점 내려갔습니다."

        "현재 점수는 [score]점 입니다."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["cafe_sunny", "cafe_cloudy", "cafe_rain", "cafe_snow"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "오늘 날씨가 어떻지?"

            "맑음" :
                label cafe_sunny:
                hide screen debug_TimerScreen
                e "와! 사진 찍으면 완전 잘 나오겠다." # +3점
                $ score += 3
                "점수기 3점 올랐습니다."

            "흐림" :
                label cafe_cloudy:
                hide screen debug_TimerScreen
                e "날이 흐려서 조명에 의지해야겠네. 약간 축 쳐지는 것 같기도 하고...?" # -1점
                $ score -= 1
                "점수기 1점 내려갔습니다."

            "비" :
                label cafe_rain:
                hide screen debug_TimerScreen
                e "괜찮아, 운치있고 좋다!" # +1점
                $ score += 1
                "점수기 1점 올랐습니다."

            "눈" :
                label cafe_snow:
                hide screen debug_TimerScreen
                e "벌써 눈이 오나? 뭐 어때, 낭만있네!" # +3점
                $ score += 3
                "점수기 3점 올랐습니다."

        "현재 점수는 [score]점 입니다."

        

"(안내) 이제 마지막 분기점입니다."
"연습 한 번 해볼까요?"

menu:
    "어떤 걸 입을까?"

    "(클럽, 연인을 선택했다고 가정) 정장 셋업" :
        e "상황과 대상에 맞게 입어야 할 것 같아." 
        $ score -= 8
        "이렇게 상황에 맞지 않는 옷을 고를 경우 점수가 내려갑니다"
        "점수기 8점 내려갔습니다."
        $ 옷차림 = "정장 셋업"

"현재 점수는 [score]점 입니다."

"이런 식으로 점수가 계산되고, 고르는 선택지에 따라 결과가 달라집니다."
"(참고) 점수 합산에는 장소와 대상만 포함됩니다."
"날씨는 엔딩으로 넘어가기 위한 점수 세부 조정을 위한 것으로, 이 선택지에서는 고려하지 않습니다."
"이제 수뭉이가 한 말을 기억하고 신중하게 입을 옷을 골라주세요."

menu:
    "옷 고르러 가기" :
        $ score += 8

    "잠이나 자자" :
        jump bad_ending

#Debug-------------------------------------------------------------------------------------------------------------
show screen debug_TimerScreen(random.choice(["coat", "hood", "setup", "shirt"]))
#EndDebug----------------------------------------------------------------------------------------------------------

menu:
    "어떤 걸 입을까?"

    "코트에 긴바지" :
        label coat:
        hide screen debug_TimerScreen
        e "가을엔 역시 코트지."
        $ 옷차림 = "코트에 긴바지"

    "후드티에 츄리닝바지" :
        label hood:
        hide screen debug_TimerScreen
        e "편한 게 짱이야."
        $ 옷차림 = "후드티에 츄리닝바지"

    "정장 셋업" :
        label setup:
        hide screen debug_TimerScreen
        e "오늘은 격식차린 옷을 입어야겠다."
        $ 옷차림 = "정장 셋업"

    "셔츠에 청바지" :
        label shirt:
        hide screen debug_TimerScreen
        e "심플 이즈 베스트! 가장 무난한 것 같아."
        $ 옷차림 = "셔츠에 청바지"

"현재 점수는 [score]점 입니다."

# 장소와 대상, 복장별로 if문을 사용하여 정리 **(나올 수 있는 모든 경우의 수를 고려함)**

label final_score_check:

# 장소, 대상, 의상 선택에 따른 가산점/패널티 조건 설정
    if 장소 == "클럽":
        if 대상 == "친구":
            if 옷차림 == "코트에 긴바지": 
                $ score += 8  # 적합 +8점
                e "코트에 긴바지? 잘생긴 사슴처럼 보이려나! 좋았어, 오늘 우리 중에 잘생긴 놈 역할은 나다."
            elif 옷차림 == "후드티에 츄리닝바지": 
                $ score -= 8  # 부적합 -8점
                e "클럽에 츄리닝이라니... 입구컷 당할 수도 있을 걸."
            else:
                e "그냥 보면 나쁘진 않은데, 클럽 분위기에는 맞지 않네..." # 부적합 -8점
                $ score -= 8

        elif 대상 == "가족":
            if 옷차림 == "코트에 긴바지":
                $ score += 8  # 적합 +8점
                e "이게 그나마 봐줄만 하겠다! 너무 발랑 까져보이면 좀 그러니까."
            else:
                $ score -= 8  # 부적합 -8점
                e "클럽이 가족이랑 가기 좋은 데가 아닌데... 옷이라도 잘 입는 게 좋을 것 같아."

        # 연인 및 공적관계
        elif 대상 == "연인":
            if 옷차림 == "코트에 긴바지":
                e"딱 깔끔하고 좋게 입은 것 같아!"
                $ score += 8 # 적합 +8점
            
            elif 옷차림 == "셔츠에 청바지":
                $ score += 8 # 적합 +8점
                e "나름 캐주얼하고, 막 꾸민 것 보단 이게 편하게 춤추기 좋을 것 같아."
            else:
                $ score -= 8
                e "너무 격식있거나 너무 후줄근하면 나 깨질지도 몰라. 클럽가서 춤췄다가 구애의 춤을 다시 춰야할지도."

        elif 대상 == "공적관계":
            $ score -= 10  # 클럽에 어울리지 않는 조합으로 패널티 -10
            e "교수님이랑 클럽이라니, 아무리 생각해봐도 역시 이건 좀 아닌 것 같아... 뭘 입는지가 문제가 아니야..."
            jump bad_ending


    elif 장소 == "도서관":
        if 대상 == "친구":
            if 옷차림 == "정장 셋업":
                $ score -= 8 # 부적합 -8
                e "내가 직장인도 아니고...그냥 친구랑 도서관에 가는 건데 뭘 이렇게까지."
            else:
                $ score += 8  # 적합 +8
                e "이 정도면 도서관에서도 편하게 공부할 수 있을 거야."

        elif 대상 == "가족":
            if 옷차림 == "코트에 긴바지":
                $ score += 8  # 적합 +8
                e "가족들이랑 도서관에서 이렇게 입고 공부하면 대학생티내기 딱 좋긴 하지."
            else:
                $ score -= 8 # 부적합 -8
                e "그래도 좀 상황에 맞게 입는 게 낫지 않았을까?"

        # 연인 및 공적관계 경우 추가
        elif 대상 == "연인":
            if 옷차림 == "정장 셋업":
                $ score -= 8 # 부적합 -8
                e "야야, 그래도 이건 너무 차렸잖아."
            else:
                $ score += 8 # 적합 +8
                e "이게 딱 좋을 것 같아!"

        elif 대상 == "공적관계":
            if 옷차림 == "셔츠에 청바지":
                $ score += 8 # 적합 +8
                e "무난해서 마음에 들어."

            elif 옷차림 == "코트에 긴바지":
                $ score += 8 # 적합 +8
                e "적당히 꾸민 느낌이네!"

            else:
                $ score -= 8 # 부적합 -8
                e "괜찮은 거 맞지?"


    elif 장소 == "술집":
        if 대상 == "친구":
            if 옷차림 == "셔츠에 청바지":
                $ score += 8 # 적합 +8
                e "꾸안꾸 최고."

            elif 옷차림 == "정장 셋업":
                $ score -= 8 # 부적합 -8
                e "술집에 정장이라니, 너무 격식 차린 느낌인데?"

            else:
                $ score += 8 # 적합 +8
                e "이것도 좋아!"

        elif 대상 == "가족":
            if 옷차림 == "정장 셋업":
                $ score -= 8 # 부적합 -8
                e "아니, 뭔... 영업사원이야?"

            elif 옷차림 == "후드티에 츄리닝바지":
                $ score -= 8 # 부적합 -8
                e "이건 너무 편한 옷이잖아."

            else:
                $ score += 8 # 적합 +8
                e "너무 편하지도, 그렇다고 너무 격식차리지도 않은 딱 캐주얼한 룩이라서 좋아."

        # 연인 및 공적관계 경우 추가
        elif 대상 == "연인":
            if 옷차림 == "셔츠에 청바지":
                $ score += 8 # 적합 +8
                e "편안하게 술마시려면 이게 좋은 것 같아!"

            elif 옷차림 == "코트에 긴바지":
                $ score += 8 # 적합 +8
                e "가지고 있는 것들 중에 제일 괜찮다!"

            else:
                $ score -= 8 # 부적합 -8
                e "너무 튀거나 너무 편해 보이면 실망할지도 몰라."

        elif 대상 == "공적관계":
            $ score -= 8 # 부적합 -8
            e "뭘 입든 난 회식 싫어. 안 갈래."


    elif 장소 == "카페":
        if 대상 == "친구":
            if 옷차림 == "셔츠에 청바지":
                $ score += 8 # 적합 +8
                e "편한 거랑, 꾸민 걸 모두 챙겼다고 볼 수 있지. 꾸안꾸?"

            elif 옷차림 == "정장 셋업":
                $ score -= 8 # 부적합 -8
                e "왜 그래? 흑역사 만들 일 있어?"

        elif 대상 == "가족":
            if 옷차림 == "코트에 긴바지":
                $ score += 8 # 적합 +8
                e "너무 잘 어울리는 옷인 것 같다."

            elif 옷차림 == "셔츠에 청바지":
                $ score += 8 # 적합 +8
                e "코트랑 고민 많이 했는데, 이건 또 이것만의 매력이 있단 말이지."

            else:
                $ score -= 8 # 부적합 -8
                e "너무... 웃음거리가 될 것 같네."

        # 연인 및 공적관계 경우 추가
        elif 대상 == "연인":
            if 옷차림 == "코트에 긴바지":
                $ score += 8 # 적합 +8
                e "잘 어울리는 것 같은데 오늘 잘생겼다는 말 좀 들으려나?"

            else:
                $ score -= 8 # 부적합 -8
                e "너무 튀거나 너무 편해 보이면 실망할지도 몰라."

        elif 대상 == "공적관계":
            if 옷차림 == "후드티에 츄리닝바지":
                $ score -= 8 # 부적합 -8
                e "공적인 사이인데 이건 너무 편해보여."

            else:
                $ score += 8 # 적합 +8
                e "깔끔한 이미지를 줄 수 있을 것 같아."

    # 최종 점수 표시
    "최종 점수는 [score]점 입니다."

    if score >= 6:
        jump happy_ending

    else:
        jump bad_ending

    # 엔딩 분기 설정
label bad_ending:
        e "너 진짜 나쁜 아이구나?"
        e "어떻게 그럴 수가 있어? 너무해..."
        me "원래 인생이 그런 거다."

        # 화면 페이드아웃 효과
        scene black with fade

        me "인생이 원래 그런 거라니까."
        e "나 사슴이야."
        me "아."

        # 화면에 "배드엔딩" 텍스트 중앙에 출력
        show text "{color=#a0a0a0}{size=90}BAD ENDING - 수뭉이의 부탁을 들어주지 않았다.{/size}" at truecenter with dissolve    # 텍스트 크기 및 색상 설정

        # 3초 대기 후 게임 종료
        pause 3
        return

label happy_ending:
        # 해피엔딩
        e "어때? 잘 어울려?"
        menu:
            "잘 어울려!!!":
                e "와아아! 너무 좋아! 고마워 [init_name]야!"
                me "그래그래~"
            "귀찮아 말 걸지마. 진 다 빠졌어...":
                e "헉... 미안. 좀 정신없었지? 고생했어, 고마워!"
                me "응. 그래도 오랜만에 나간다니까 뭐든 잘 하고 와."
                e "응! 좋아."

        # 화면 페이드아웃 효과
        scene black with fade
        pause 1  # 1초 대기 후 이후 문장 출력

        e "진짜 정말 고마워, 슴우야!"

        # 화면에 "해피엔딩" 텍스트 중앙에 출력
        show text "{color=#ffcdcd}{size=90}HAPPY ENDING - 수뭉이의 코디를 올바르게 잘 도와줬다.{/size}" at truecenter with dissolve    # 텍스트 크기 및 색상 설정

        # 3초 대기 후 게임 종료
        pause 3
        return
return