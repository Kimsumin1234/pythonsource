from django import template

# question_list.html 에서 일련번호 구하기
# 전체 게시물 개수 - 시작인덱스 - 현재인덱스 + 1
# => {{question_list.paginator.count|sub:question_list.start_index|sub:forloop.counter0|add:1}}
register = template.Library()

# template.Library() 에 add 는 만들어져 있어서 add 는 그냥 쓸수있지만
# sub 는 없어서 직접 만들어서 template.Library() 에 등록함
# question_list.html 에서 {% load board_filter %} 로 부를수있음


# 필터 만들기
@register.filter
def sub(value, arg):
    return value - arg
