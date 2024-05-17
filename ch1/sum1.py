def sum1(a, b):
    return a + b


def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 없습니다.")
        return
    else:
        result = sum1(a, b)

    return result


# 모듈 안의 함수 테스트
# 1차 확인
# 이렇게 하면 다른대서 호출해도 테스트 구문이 같이 호출되는 상황이 안된다
if __name__ == "__main__":
    print(sum1(50, 75))
    print(safe_sum(50, "75"))
    print(safe_sum(50, 75))
