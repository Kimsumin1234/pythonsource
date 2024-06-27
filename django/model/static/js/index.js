// 로그아웃 클릭시 a 태그 기능 중지후 form 전송
document.querySelector("#logout").addEventListener("click", (e) => {
  e.preventDefault();
  document.querySelector("form").submit();
});
