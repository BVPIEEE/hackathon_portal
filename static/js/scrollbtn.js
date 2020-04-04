const btnScrollToTop = document.querySelector("#btnScrollToTop");

btnScrollToTop.addEventListener("click", function(){

  window.scrollTo({
    top: 50,
    left: 0,
    behavior: "smooth"
  });
}));
