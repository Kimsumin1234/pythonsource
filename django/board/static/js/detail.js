const deleteAll = document.querySelectorAll(".delete");
const actionForm = document.querySelector("#actionForm");
// 목록 클릭시 actionForm 보내기 (2024-07-01)
document.querySelector("#list").addEventListener("click", (e) => {
  e.preventDefault();
  actionForm.action = e.target.getAttribute("href");
  actionForm.submit();
});

// delete 로 변수를 잡으면 에러가 난다
// deleteAll.forEach((delete) => {
//     delete.addEventListener("click", (e) => {
//         e.preventDefault();
//         if (confirm("정말로 삭제하시나요?")) {
//             location.href
//         }

//       })
// })

// delete => item 으로 변경
deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    // href 가져오기
    const href = e.target.getAttribute("href");
    if (confirm("정말로 삭제하시나요?")) {
      location.href = href;
    }
  });
});
