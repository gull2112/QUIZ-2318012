class Bungeoppang:
    total_sales = 0  # 클래스 변수로 모든 인스턴스에서 공유됨

    def __init__(self, contents, price):
        self.contents = contents
        self.price = price  

    def sell(self):
        print(f"{self.contents} 붕어빵이 판매되었습니다. 가격은 {self.price}원입니다.")
        Bungeoppang.total_sales += self.price
        print(f"총 판매금은 {Bungeoppang.total_sales}원입니다.")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

# 슈크림 붕어빵 객체 생성
cream_bungeoppang = Bungeoppang("슈크림", 2000)

# 팥 붕어빵 객체 생성
red_bean_bungeoppang = Bungeoppang("팥", 1500)

# 판매
cream_bungeoppang.sell()
red_bean_bungeoppang.sell()

# 먹기
cream_bungeoppang.eat()
red_bean_bungeoppang.eat()
