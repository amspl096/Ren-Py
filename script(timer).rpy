#Debug
init python:
    import random
#EndDebug

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('수뭉이', color="#6ac1e4")
define me = Character("[name]")

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

# 여기에서부터 게임이 시작합니다.
label start:

    hide screen debug_TimerScreen

    # 점수 표시 화면을 항상 띄움
    show screen score_display

    "debug"
    scene black with dissolve

# 아래로는 선택지입니다. 플레이어가 선택하는 것에 따라 최종 점수 및 결과가 달라집니다.

# 현재 점수변동 구현 중입니다.

menu:
    "어떤 장소로 갈까?"
    
    "클럽":
        $ 장소 = "클럽"
        e "timer"

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["fam", "fri", "lov", "pub"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "어떤 사람과 함께 갈까?"

            "가족":
                label fam:
                hide screen debug_TimerScreen
                $ 대상 = "가족"
                e "가족...이랑 클럽을 간다고? 뭐, 그럴 수 있지..." # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "친구":
                label fri:
                hide screen debug_TimerScreen
                $ 대상 = "친구"
                e "좋아, 당장 친구한테 같이 가자고 연락해 봐야지!" # +3점
                $ score += 3
                "점수가 3점 올랐습니다."
                
            "연인":
                label lov:
                hide screen debug_TimerScreen
                $ 대상 = "연인"
                e "으음... 말 꺼내면 큰일날 것 같은데. 그래, 같이 가서 즐겁게 놀다 오자고 해야지!" # 0점
                $ score += 0
                "점수에 변동이 없습니다."

            "공적관계":
                label pub:
                hide screen debug_TimerScreen
                $ 대상 = "공적관계"
                e "뭐?" with vpunch
                e "...좋은 생각은 아닌 것 같아, 생각해보자... 교수님이랑 클럽...? 으음." # -3점
                $ score -= 3
                "점수가 3점 내려갔습니다."
       
        "현재 점수는 [score]점 입니다."

        #Debug-------------------------------------------------------------------------------------------------------------
        show screen debug_TimerScreen(random.choice(["sunny", "cloudy", "rain", "snow"]))
        #EndDebug----------------------------------------------------------------------------------------------------------

        menu:
            "오늘 날씨가 어떻지?"

            "맑음":
                label sunny:
                hide screen debug_TimerScreen
                e "날이 엄청 맑아! 햇빛도 좋고, 놀러가기 딱 좋은 날씨네." # +3점
                $ score += 3
                "점수가 3점 올랐습니다."

            "흐림" :
                label cloudy:
                hide screen debug_TimerScreen
                e "날이 조금 흐리긴 한데, 딱히 비나 눈이 올 것 같진 않아." # 0점
                "점수가 0점 올랐습니다."
                "점수에 변동이 없습니다."

            "비" :
                label rain:
                hide screen debug_TimerScreen
                e "모처럼 오랜만에 놀러가는데 하필이면 비가 오네." #-1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

            "눈" :
                label snow:
                hide screen debug_TimerScreen
                e "엥! 벌써 눈이 온다고? 지구가 망하긴 했구나." #-1점
                $ score -= 1
                "점수가 1점 내려갔습니다."

        "현재 점수는 [score]점 입니다."