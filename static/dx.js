var buttons = document.getElementsByClassName("flw btn btn-primary");

for (i = 0; i < buttons.length; i ++)
  buttons[i].addEventListener('click', function(){
    buttons[i].setAttribute("class", "flw btn btn-success");
  });
