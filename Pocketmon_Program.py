import random
x=0
y=0
guide=[['\/\/' for j in range(5)] for i in range(5)]
guide[1][1] = '****'
guide[3][1] = '****'
guide[4][3] = '****'
guide[0][3] = '****'
guide[2][3] = '****'
guide[x][y] = '----'


total_skillset={'잠자기':0,'몸통박치기':10,'전광석화':15,'댁댁이':20,'퀭퀭이:':22.5}
learning_skill=(('댁댁이','퀭퀭이'),('말퀭이','뚱퀭이'))
total_skillonly=tuple(total_skillset.keys())
exp_set=tuple(i**2+5 for i in range(10))
weight_list=[(0,1,-1,-1),(-1,0,1,0),(0,-1,0,1),(1,0,-1,0)]


def view_map():
    for i in guide:
        print(*i, end=' ')
        print()

def move():
    input_move=input('W:위,S:아래,A:왼쪽,D:오른쪽')
    global x
    global y
    setting={'w':(-1,0),'s':(1,0),'a':(0,-1),'d':(0,1)}
    if not input_move in setting.keys():
        print('w,s,a,d 중에서 입력하세요')
        return False
    dx,dy=setting.get(input_move)


    if 0<=x+dx and x+dx<5 and 0<=y+dy and y+dy<5 and guide[x+dx][y+dy]!='****':
        guide[x][y]='\/\/'
        guide[x+dx][y+dy]='----'
        x+=dx
        y+=dy
        view_map()
        return start_fighting()

    else:
        print('막혀있습니다')
        view_map()
        return False



def plus_hp(x):
    if x<0:
        return 0
    else:
        return x

def start_fighting():
    threshold=random.random()
    if threshold<0.5:
        return True
    else:
        return False
def hit_efficient(x):
    threshold=random.random()
    if threshold<0.2:
        return x*1.5
    else:
        return x

def converter_prop(x):
    if x=='물':
        return 0
    elif x=='불':
        return 1
    elif x=='땅':
        return 2
    else:
        return 3

def fighting():
    print('어..? 무언가가 내 발목을 잡았다....')
    print(f'{ggou.name}가 나타났다.')
    print(f'가랏 {pika.name}')
    rof=input('1)싸운다 2)도망간다 중에서 입력하세요')
    if rof=='2':
        if random.random()<0.35:
            print("도망쳐서 다행이다")
            return
        else:
            print('도망치기에 실패했다')



    if weight_list[converter_prop(pika.prop)][converter_prop(ggou.prop)]==1:
        weight=1.3
    elif weight_list[converter_prop(pika.prop)][converter_prop(ggou.prop)]==-1:
        weight=1/1.3
    else:
        weight=1

    ggou.hiddenhp=20

    while pika.hp>0 and ggou.hp>0:
        print('어떤 스킬을 쓸까??')
        print(*pika.skills)
        attack_input=input()
        if attack_input=='status':
            print(ggou.hp)
            print(pika.hp)
            continue
        print(f'{pika.name}의 {pika.skills[int(attack_input)-1]}!!')
        print(f'{ggou.name}의 hp: {ggou.hp:.2f} -> {plus_hp(ggou.hp-weight*total_skillset.get(pika.skills[int(attack_input)-1])):.2f}')
        if weight==1.3:
            print('효과가 굉장했다')
        if weight==1/1.3:
            print('효과가 미미했다')


        ggou.hp=-weight*total_skillset.get(pika.skills[int(attack_input)-1])
        if ggou.hp>0:
            count_attack=random.choice(ggou.skills)
            print(f'{ggou.name}의 {count_attack}!!')
            print(f'{pika.name}의 hp:{pika.hp:.2f} -> {plus_hp(pika.hp - 1/weight*total_skillset.get(count_attack)):.2f}')
            pika.hp=-weight*total_skillset.get(count_attack)
        else:
            print(f'{ggou.name}을 해치웠다!')

            print(f'경험치 {(pika.hiddenlevel+2)**(pika.calculate_standard()-ggou.calculate_standard())+2:.2f}을 얻었다')
            pika.exp=(pika.hiddenlevel+2)**(pika.calculate_standard()-ggou.calculate_standard()+2)
            while pika.hiddenexp > exp_set[pika.hiddenlevel]:
                pika.hiddenexp -= exp_set[pika.hiddenlevel]
                pika.hiddenlevel += 1
                print(f'{pika.name}이 레벨 했다!!')
                if len(pika.skills)==4:
                    print('스킬 4개를 이미 배워서 어느 한 스킬을 잊어야 한다')
                    print('무엇을 잊으시겠습니까?')
                    forget_input=input()
                    pika.skills.remove(forget_input)

                print(f'{pika.name}은 새로운 스킬을 배울 수 있다.. 어느 것을 배울까??')
                print(f'{learning_skill[pika.hiddenlevel - 2][0]},{learning_skill[pika.hiddenlevel - 2][1]}')
                learn_input = input()
                pika.skills.append(learn_input)
                print(f'{pika.name}은 {learn_input}을 배웠습니다')



            print(f'레벨:{pika.level} ,경험치 {pika.exp:.2f}/{exp_set[pika.level]}')




class Pocketmon:
    def __init__(self,input_name,hp,prop):
        self.hiddenname=input_name
        self.hiddenhp = hp
        self.prop=prop
        self.hiddenlevel=1
        self.skills=['잠자기','몸통박치기','전광석화']
        self.hiddenexp=0
        self.standard=0
        # if self.hiddenexp>exp_set[self.level]:
        #     self.hiddenexp-=exp_set[self.level]
        #     self.level+=1

    @property
    def name(self):
        return self.hiddenname
    @name.setter
    def name(self,input_name):
        self.hiddenname=input_name
    @property
    def hp(self):
        return self.hiddenhp
    @hp.setter
    def hp(self,dhp):
        self.hiddenhp+=dhp

    @property
    def exp(self):

        while self.hiddenexp>exp_set[self.hiddenlevel]:
            self.hiddenexp-=exp_set[self.hiddenlevel]
            self.hiddenlevel+=1

        return self.hiddenexp
    @exp.setter
    def exp(self,dexp):
        self.hiddenexp+=dexp
    @property
    def level(self):
        return self.hiddenlevel



    @level.setter
    def level(self,dlevel):
        self.hiddenlevel+=dlevel
    def calculate_standard(self):
        num=0
        for i in self.skills:
            num+=total_skillset.get(i)
        return num/3


    def show_properties(self):
        print(f"이름:{self.name}\nhp:{self.hiddenhp}\n상성:{self.prop}\n레벨:{self.level}")
        print('<스킬>')

        for i in self.skills:
            print(f"{i}:{total_skillset.get(i)}")
    def show_skill(self):
        for i in self.skills:
            print(f"{i}:{total_skillset.get(i)}")
pika=Pocketmon('피카추',100,'전기')
ggou=Pocketmon('꼬부기',20,'땅')
# pika.show_properties()
# print("level:",pika.level)
# print("current exp:",pika.exp)
# pika.exp=10
# print("current exp:",pika.exp)
# print('current lev:',pika.level)
# fighting()
# print("포켓몬의 협곡의 오신 걸 환영합니다")
while True:
    start_input=input('q:게임을 종료, g:지도를 보기 위해선 , m:움직이기')
    if start_input.isalpha():
        if start_input=='g':
            view_map()
    else:
        print('알파벳을 입력하세요')
        continue

    while True:
        if move():
            break
    fighting()



# while True:
#     a=random.random()
#     if a>0.5:
#         print('finish')
#         break
#     else:
#         print('one more time')




