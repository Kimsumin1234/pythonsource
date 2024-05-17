PI = 3.1415192


class Test:
    def solv(self, r):
        return PI * (r**2)

    def sum1(self, a, b):
        return a + b


# 모듈 테스트 구문
if __name__ == "__main__":
    print(PI)
    a = Test()
    print(a.solv(2))
    print(a.sum1(2, 4))
