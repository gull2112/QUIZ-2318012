class Bungeoppang:


    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total = 0

    def sell(self):
        print(f"{self.contents} 붕어빵이 판매되었습니다. 가격은 {self.price}원입니다.")
        Bungeoppang.total_sales = self.price + self.total
        print(f"총 판매금은 {Bungeoppang.total_sales}원입니다.")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")


cream_bungeoppang = Bungeoppang("슈크림", 2000)


red_bean_bungeoppang = Bungeoppang("팥", 1500)

# 판매
cream_bungeoppang.sell()
red_bean_bungeoppang.sell()

# 먹기
cream_bungeoppang.eat()
red_bean_bungeoppang.eat()
