var email=document.forms['form']['contact_email'];
var name1=document.forms['form']['contact_name'];
var phone=document.forms['form']['contact_phone'];
var msg=document.forms['form']['contact_message'];

var error=document.getElementById('email_message');
var error1=document.getElementById('name_message');
var error2=document.getElementById('phone_message');
var error3=document.getElementById('msg_message');


function validated(){
if(name1.value.length <9){
    name1.style.border="3px solid red";
    error1.style.display="block";
    name1.focus();
    return false;
}
if(email.value.length <9){
    email.style.border="3px solid red";
    error.style.display="block";
    email.focus();
    return false;
}
if(phone.value.length <9){
    phone.style.border="3px solid red";
    error2.style.display="block";
    phone.focus();
    return false;
}
if(msg.value.length <9){
    msg.style.border="3px solid red";
    error3.style.display="block";
    msg.focus();
    return false;
}

}

// Getting inputData from user input
// var inputData=document.getElementsByTagName("input");
// // Getting form elements
// var Form = document.getElementsByTagName("form")[0];
// // Getting message class
// var message = document.getElementsByClassName("message");

// function validated(){
//     var fullname=inputData['fullname'].value;
//     var email=inputData['email'].value;

//     // fullname validation
// 	if(fullname===""){
//         message[0].innerText="**Full Name Required";
//       }else{
//         message[0].innerText="";
//     }
  
//   // Email validation
//     if(email===""){
       
//        message[1].innerText="**Email Address Required";
//     }else{
//        message[1].innerText="";
//     }
   
//     if(fullname===""||email===""){
//         return false;
//       }
//       return true;
//         }