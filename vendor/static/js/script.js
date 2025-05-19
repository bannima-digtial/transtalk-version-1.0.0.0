var s = 0;
function toggleSidebar(){
    if (s == 0){
        s=1;
        document.querySelector('#sidebar').style.display = "block";
    } 
    else{
        s=0;
        // alert('toggle close');
        document.querySelector('#sidebar').style.display = "none";
    }
}