function anchor_submit_left(){
    //leftsubmit()
    var curryear = localStorage.getItem("yearnow")
    var company = localStorage.getItem("companynow")
    var item = localStorage.getItem("itemnow")
    var year = (parseInt(curryear) - 1).toString()
    if (curryear=="2012"|curryear==null){
        //alert("AFDSFASDF")
        event.preventDefault();
    }
    else{
        document.getElementById("left_year").setAttribute('value',year); 
        document.getElementById("left_company").setAttribute('value',company); 
        document.getElementById("left_item").setAttribute('value',item); 
        //localstorage has to change
        localStorage.setItem("yearnow",year)    
        document.getElementById("leftinfo_item").innerHTML = item
        //document.getElementById("rightinfo_item").innerHTML = item
        //submit
        document.getElementById("leftform").setAttribute('method',"post");
        document.getElementById("leftform").submit();
    }
    

}
function anchor_submit_right(){
    //rightsubmit()
    var curryear = localStorage.getItem("yearnow")
    var company = localStorage.getItem("companynow")
    var item = localStorage.getItem("itemnow")
    var year = (parseInt(curryear) + 1).toString()
    //console.log("hereeeeeee")
    if (curryear=="2018" | curryear==null){
        event.preventDefault();
    }
    else{
        document.getElementById("right_year").setAttribute('value',year); 
        document.getElementById("right_company").setAttribute('value',company); 
        document.getElementById("right_item").setAttribute('value',item); 
        //localstorage has to change
        localStorage.setItem("yearnow",year)
        document.getElementById("leftinfo_item").innerHTML = item
        //document.getElementById("rightinfo_item").innerHTML = item
        //submit
        document.getElementById("rightform").setAttribute('method',"post");
        document.getElementById("rightform").submit();

        //console.log(document.getElementById("right_item"))
        //return True;
    }
    
    
    
}
