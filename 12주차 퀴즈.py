class Bungeoppang:
    def __init__(self, contents):
        self.contents = contents

    def sell(self):
        print(f"{self.contents} 붕어빵이 판매되었습니다.")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")


# 슈크림 붕어빵 객체 생성
cream_bungeoppang = Bungeoppang("슈크림")

# 팥 붕어빵 객체 생성
red_bean_bungeoppang = Bungeoppang("팥")

# 판매
cream_bungeoppang.sell()
red_bean_bungeoppang.sell()

# 먹기
cream_bungeoppang.eat()
red_bean_bungeoppang.eat()