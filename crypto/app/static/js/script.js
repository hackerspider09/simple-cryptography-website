let keyinput = document.getElementById("numinput");
let opt= document.querySelector(".selector");
let ipdiv = document.querySelector(".ip");

opt.addEventListener("change",()=> {

    console.log("Dropdown Menu");
    // keyinput.placeholder="Key";
    console.log(opt.value);
    // if (keyinput.classList === "vnumip"){

    // }
    if (opt.value === "opt1"){
        keyinput.placeholder="Enter shift";
        // keyinput.classList.toggle("vnumip");
        keyinput.removeAttribute("style");
        // keyinput.style.display="initial";
    }else if (opt.value === "opt2"){
        keyinput.placeholder="Key/Keyword";
        // keyinput.classList.toggle("vnumip");
        keyinput.removeAttribute("style");
        // keyinput.style.display="initial";
    }
})