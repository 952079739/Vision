var menu = document.getElementsByTagName('span');
var count = 0;
var m = 0;

menu[0].onclick = function () {
    for (var i = 0; i < menu.length; i++) {
        menu[i].classList.remove("menu-click");
    }
    this.classList.add("menu-click");
    // if(count==1){
    //     remove();
    //     count =0;
    // }
    // if (m == 0) {
    //     clicks();
    //     m = 1;
    //     count=0;   
    // }
    document.getElementsByClassName("divs")[0].style.display = "block";
    document.getElementsByClassName("divs")[1].style.display = "none";
};

menu[1].onclick = function () {
    for (var i = 0; i < menu.length; i++) {
        menu[i].classList.remove("menu-click");
    }
    this.classList.add("menu-click");

    // remove();
    // m = 0;
    // count = 0;
    document.getElementsByClassName("divs")[0].style.display = "none";
    document.getElementsByClassName("divs")[1].style.display = "none";

};

menu[2].onclick = function () {
    for (var i = 0; i < menu.length; i++) {
        menu[i].classList.remove("menu-click");
    }
    this.classList.add("menu-click");
    // if(count==1){
    //     remove();
    //     count =0;
    // }
    // if (m == 0) {
    //     clicks1();
    //     m = 1;
    //     count=0;   
    // }
    document.getElementsByClassName("divs")[1].style.display = "block";
    document.getElementsByClassName("divs")[0].style.display = "none";
};
// function clicks() {
//     var div = document.createElement("div");
//     div.classList.add("divs");
//     div.style.display = "block";
//     document.body.appendChild(div);
//     var file1 = document.createElement("input");
//     file1.classList.add("file");
//     file1.setAttribute("type", "file");
//     div.appendChild(file1);
// }
// function clicks1() {
//     var div2 = document.createElement("div");
//     div2.classList.add("divs");
//     div2.style.display = "block";
//     document.body.appendChild(div2);
//     var file1 = document.createElement("input");
//     file1.classList.add("file");
//     file1.setAttribute("type", "text");
//     div.appendChild(file1);
// }
// function remove() {
//     var div1 = document.getElementsByClassName("divs");
//     document.body.removeChild(div1[0]);
//     document.body.removeChild(div1[1]);
// }
// function remove1() {
//     var div1 = document.getElementsByClassName("divs");
//     document.body.removeChild(div1[1]);
// }
// function remove2() {
//     var div1 = document.getElementsByClassName("divs");
//     document.body.removeChild(div1[0]);
// }
// var img  = document.getElementsByTagName("img")[0];
//
//
// var btn = document.querySelector('.singer.song')
// var audioElem = document.getElementsT
// btn.onclick = function () {
//
// }
var img = document.getElementsByTagName("img");
var names = document.getElementById('title')
var source = document.getElementsByTagName("audio")[0];
for (let i = 0; i < img.length; i++) {
    img[i].onclick = function () {
        source.setAttribute("src", img[i].dataset.url);
        names.innerText = img[i].dataset.name;
    }
}



