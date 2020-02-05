var type="empty";
function clickFilters(id){
    // alert('I am Called');
    document.getElementById(id).style.display = "block";
}

function pay(){
    location.replace("https://p-y.tm/2-3Vlwp");
}

function getUserType(id){
    type = document.getElementById(id).value;

    if(type=="DHE"){
        document.getElementById("email").style.display="flex";
        document.getElementById("password").style.display="flex";
        document.getElementById("loginbtn").style.display="flex";


        document.getElementById("university").style.display="none";
        document.getElementById("clg").style.display="none";
        document.getElementById("prn").style.display="none";
    }
    else if(type=="DIR"){
        document.getElementById("university").style.display="flex";
        
        
        document.getElementById("clg").style.display="none";
        document.getElementById("prn").style.display="none";
        document.getElementById("email").style.display="none";
        document.getElementById("password").style.display="none";
        document.getElementById("loginbtn").style.display="none";
    }
    else if(type=="alumni" || type=="student"){
        document.getElementById("university").style.display="flex";
        
        
        document.getElementById("clg").style.display="none";
        document.getElementById("prn").style.display="none";
        document.getElementById("email").style.display="none";
        document.getElementById("password").style.display="none";
        document.getElementById("loginbtn").style.display="none";
    }

}

function getUniversityOrCollege(id){
    value = document.getElementById(id).value   ;
    if(value=="SRTMUN"){
        // alert("University");
        document.getElementById("clg").style.display="flex";
        

        document.getElementById("prn").style.display="none";
        document.getElementById("email").style.display="none";
        document.getElementById("password").style.display="none";
        document.getElementById("loginbtn").style.display="none";

    }
    else{

        if(type=="DIR"){
            document.getElementById("email").style.display="flex";
            document.getElementById("password").style.display="flex";
            document.getElementById("loginbtn").style.display="flex";

            document.getElementById("prn").style.display="none";
            document.getElementById("clg").style.display="none";
        }
        else if(type=="alumni" || type=="student"){
            document.getElementById("prn").style.display="flex";
            document.getElementById("password").style.display="flex";
            document.getElementById("loginbtn").style.display="flex";

            
            document.getElementById("clg").style.display="none";
            document.getElementById("email").style.display="none";    
        }
        
    }
}

function getCollege(id){
    value = document.getElementById(id);
    // alert(type);
    if(type=="DIR"){
        document.getElementById("email").style.display="flex";
        document.getElementById("password").style.display="flex";
        document.getElementById("loginbtn").style.display="flex";

        document.getElementById("prn").style.display="none";
    }
    else if(type=="alumni" || type=="student" ){
        document.getElementById("email").style.display="none";

        document.getElementById("prn").style.display="flex";
        document.getElementById("password").style.display="flex";
        document.getElementById("loginbtn").style.display="flex";
    }
}