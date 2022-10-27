document.getElementById('container');

document.querySelector('#container');

document.getElementsByClassName('second');

document.querySelector('ol li.third');

const greeting = document.getElementById('container');
greeting.innerText = "Hello!";

const mainClass = document.querySelector('.footer');
mainClass.classList.add('main');

mainClass.classList.remove('main');

const newLiElement = document.createElement('li');

newLiElement.innerText = "four";

const ul = document.querySelector('ul');
ul.append(newLiElement);

const li = document.querySelectorAll('ol li');
for(let ls in li){
    ls.style.backgroundColor = "green";
}

const footer = document.querySelector(".footer");
footer.remove();