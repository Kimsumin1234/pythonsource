# request.method : http method 가져오기
# request.META : 가져올수있는 데이터 목록 https://docs.djangoproject.com/en/5.0/ref/request-response/ 참고 (HttpRequest.META)


# ip 가져오는 함수
def get_client_ip(request):
    ip = request.META.get("REMOTE_ADDR")  # == request.META["REMOTE_ADDR"]
    return ip
