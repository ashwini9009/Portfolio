const nameText = "Hello, I'm Ashwini";
const nameElement = document.getElementById("typing-name");

let i = 0;

function typeName() {
  if (i < nameText.length) {
    nameElement.innerHTML += nameText.charAt(i);
    i++;
    setTimeout(typeName, 100);
  }
}

typeName();



const roles = [
"Java Developer",
"Spring Boot Developer",
"Full Stack Developer",
"Angular Developer"
];

let roleIndex = 0;
let charIndex = 0;
const roleElement = document.getElementById("typing-role");

function typeRole(){

if(charIndex < roles[roleIndex].length){

roleElement.innerHTML += roles[roleIndex].charAt(charIndex);
charIndex++;

setTimeout(typeRole,100);

}
else{

setTimeout(eraseRole,1500);

}

}

function eraseRole(){

if(charIndex > 0){

roleElement.innerHTML =
roles[roleIndex].substring(0,charIndex-1);

charIndex--;

setTimeout(eraseRole,50);

}
else{

roleIndex++;

if(roleIndex >= roles.length){
roleIndex = 0;
}

setTimeout(typeRole,200);

}

}

typeRole();

document.getElementById("contact-forms").addEventListener("submit", function(e){
    e.preventDefault();

    const data = {
        name: this.name.value,
        email: this.email.value,
        message: this.message.value
    };

    fetch("http://127.0.0.1:5000/contact-forms", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if(result.message){
            alert(result.message);
            this.reset();
        } else {
            alert(result.error);
        }
    })
    .catch(error => {
        console.log(error);
        alert("An error occurred while sending your message. Please try again later.");
    });
});
