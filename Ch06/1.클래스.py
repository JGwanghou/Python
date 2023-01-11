"""
날짜 : 2023/01/11
이름 : 조광호
내용 : 파이썬 클래스 실습하기
"""

from sub1.Car import Car
from sub1.Account import Account

sonata = Car('소나타', '흰색', 3000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

bmw = Car('BMW', '검정', 5000)
bmw.speedUp()
bmw.speedDown()
bmw.show()


kb = Account('국민은행', '123-12-1234', '김길동', 5000)
kb.deposit(20000)
kb.withdraw(5000)

# 캡슐화
# kb.__balance += 1
kb.show()

wr = Account('우리은행', '0103-1024-12', '한김당', 25000)
wr.deposit(20000)
wr.withdraw(5000)
wr.show()