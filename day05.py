#9.16
# def good():
#     a=input().split()
#     return a
#
# print(good())

#9.2
# def get_odds(n): # return int
#     for i in range(1,n+1,2):
#         yield i
# get_odds=(x for x in range(10) if x%2==1)
# get=1
# for i in get_odds:
#     if get==3:
#         print(i)
#         break
#     else:
#         get+=1
#9.3
#시작할 떄 출력,끝날 때 출력... 뭔 말인쥐??
def test(f): #decorator
    def func(*args,**kwargs):
        print('start')
        gogo()
        print('end')




    return func
def gogo():
    for i in range(3):
        print(i)

start_func=test(gogo)
start_func()



