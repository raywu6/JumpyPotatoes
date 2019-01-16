var buttons = document.getElementsByClassName("flw btn btn-success");

var addFunc = (elem) => {
  elem.addEventListener('mouseover', function(){
    this.setAttribute("class", "flw btn btn-warning")
    this.innerHTML = "Unfollow";
  })
  elem.addEventListener('mouseout', function(){
    this.setAttribute("class", "flw btn btn-success")
    this.innerHTML = "Followed";
  })
}

for (i = 0; i < buttons.length; i ++)
  addFunc(buttons[i]);
