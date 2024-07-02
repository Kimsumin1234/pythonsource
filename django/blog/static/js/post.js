document.querySelector("#like").addEventListener("click", (e) => {
  // e.target : 실제 이벤트가 일어난 대상 => span
  // e.currentTarget : 이벤트가 일어난 대상의 부모 => div #like

  // data-post="{{post.id}}" 가져오기
  const postId = e.currentTarget.dataset.post;
  const count = document.querySelector(".like-total span");
  fetch(`/blog/post/like/${postId}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      //   좋아요 수 : data.likes
      //   좋아요 표시 여부 : data.is_liked
      console.log(data.likes);
      console.log(data.is_liked);
      console.log(count);

      count.innerHTML = data.likes;

      if (data.is_liked) {
        document.querySelector(".like").classList.add("show");
        document.querySelector(".dislike").classList.remove("show");
      } else {
        document.querySelector(".like").classList.remove("show");
        document.querySelector(".dislike").classList.add("show");
      }
    });
});
