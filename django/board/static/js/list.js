const actionForm = document.querySelector("#actionForm");
// 제목 클릭 시 actionForm 보내기 (2024-07-01)
document.querySelector("tbody").addEventListener("click", (e) => {
  e.preventDefault();
  // href 값 가져오기
  href = e.target.getAttribute("href");
  // actionForm 에 action 수정 board/310 이런식으로 가게끔
  actionForm.action = `/board/${href}`;
  actionForm.submit();
});

// 정렬 변화가 일어나면 value 가져온 후 (2024-07-01)
// actionForm 의 so value 변경
document.querySelector("select.so").addEventListener("change", (e) => {
  actionForm.querySelector("#so").value = e.target.value;
  actionForm.submit();
});

// 페이지 나누기 + 검색어 (2024-07-01)
// 페이지 나누기 클릭시 href 에 있는 값 가져온후
// actionForm 의 page value 변경하기
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();
  href = e.target.getAttribute("href");
  actionForm.querySelector("#page").value = href;
  actionForm.submit();
});

// 검색어(top_keyword) 가져오기
// 검색어가 없는경우 alert() 창 띄우기
// 있는경우 actionForm 에 keyword value 에 삽입, page value 는 1로 변경
document.querySelector("#btn_search").addEventListener("click", (e) => {
  const top_keyword = document.querySelector("#top_keyword");
  if (top_keyword.value == "") {
    alert("검색어를 입력해주세요");
    top_keyword.focus();
    return;
  } else {
    actionForm.querySelector("#keyword").value = top_keyword.value;
    actionForm.querySelector("#page").value = 1;
    actionForm.submit();
  }
});
