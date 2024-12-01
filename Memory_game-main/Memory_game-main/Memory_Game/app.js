function runConfettiForTwoSeconds() {
    for (i = 0; i < 100; i++) {
        // Random rotation
        var randomRotation = Math.floor(Math.random() * 360);
        // Random Scale
        var randomScale = Math.random() * 1;
        // Random width & height between 0 and viewport
        var randomWidth = Math.floor(Math.random() * Math.max(document.documentElement.clientWidth, window.innerWidth || 0));
        var randomHeight = Math.floor(Math.random() * Math.max(document.documentElement.clientHeight, window.innerHeight || 500));

        // Random animation-delay
        var randomAnimationDelay = Math.floor(Math.random() * 15);
        // console.log(randomAnimationDelay);

        // Random colors
        var colors = ['#0CD977', '#FF1C1C', '#FF93DE', '#5767ED', '#FFC61C', '#8497B0']
        var randomColor = colors[Math.floor(Math.random() * colors.length)];

        // Create confetti piece
        var confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.top = randomHeight + 'px';
        confetti.style.right = randomWidth + 'px';
        confetti.style.backgroundColor = randomColor;
        // confetti.style.transform='scale(' + randomScale + ')';
        confetti.style.obacity = randomScale;
        confetti.style.transform = 'skew(15deg) rotate(' + randomRotation + 'deg)';
        confetti.style.animationDelay = randomAnimationDelay + 's';
        document.getElementById("confetti-wrapper").appendChild(confetti);
    }
    setTimeout(function() {
        var confettiWrapper = document.getElementById("confetti-wrapper");
        confettiWrapper.innerHTML = ''; // Clear inner HTML
    }, 2000);
    document.getElementById("score").innerText = score;
}

function runcont() {
    for (i = 0; i < 100; i++) {
        // Random rotation
        var randomRotation = Math.floor(Math.random() * 360);
        // Random Scale
        var randomScale = Math.random() * 1;
        // Random width & height between 0 and viewport
        var randomWidth = Math.floor(Math.random() * Math.max(document.documentElement.clientWidth, window.innerWidth || 0));
        var randomHeight = Math.floor(Math.random() * Math.max(document.documentElement.clientHeight, window.innerHeight || 500));

        // Random animation-delay
        var randomAnimationDelay = Math.floor(Math.random() * 15);
        // console.log(randomAnimationDelay);

        // Random colors
        var colors = ['#0CD977', '#FF1C1C', '#FF93DE', '#5767ED', '#FFC61C', '#8497B0']
        var randomColor = colors[Math.floor(Math.random() * colors.length)];

        // Create confetti piece
        var confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.top = randomHeight + 'px';
        confetti.style.right = randomWidth + 'px';
        confetti.style.backgroundColor = randomColor;
        // confetti.style.transform='scale(' + randomScale + ')';
        confetti.style.obacity = randomScale;
        confetti.style.transform = 'skew(15deg) rotate(' + randomRotation + 'deg)';
        confetti.style.animationDelay = randomAnimationDelay + 's';
        document.getElementById("confetti-wrapper").appendChild(confetti);
    }
    document.getElementById("score").innerText = score;
}
let score = 0;

let cardsArray = [

    {
        'name': 'Reyna',
        'img': '/pics/VALORANT_Reyna_Dark.jpg',
    },
    {
        'name': 'Astra',
        'img': '/pics/astra.png',
    },
    {
        'name': 'Omen',
        'img': '/pics/VALORANT_Omen_Dark.jpg',
    },
    {
        'name': 'jett',
        'img': '/pics/VALORANT_Jett_Dark.jpg',
    },
    {
        'name': 'Sage',
        'img': 'pics/VALORANT_Sage_dark.jpg',
    },
    {
        'name': 'Killjoy',
        'img': 'pics/KillJoy_Wallpapers_blue1.jpg',
    },
    {
        'name': 'Cypher',
        'img': 'pics/VALORANT_Cypher_Dark.jpg',
    },
    {
        'name': 'Brimm',
        'img': 'pics/VALORANT_Brimm_Dark.jpg',

    },
    {
        'name': 'Sove',
        'img': 'pics/VALORANT_Sova_Dark.jpg',
    },
    {
        'name': 'chamber',
        'img': 'pics/chamber.jpg',

    }
];
const parentDiv = document.querySelector('#card-section');
const gamecard = cardsArray.concat(cardsArray)
    // console.log("parent div")
    // console.log(parentDiv)


//stylinng the match card
const cardmatches = () => {

    let card_selected = document.querySelectorAll('.card_selected');

    card_selected.forEach((Element) => {
        Element.classList.add('card_match');
    })
}

const resetGame = () => {
    clickcount = 0;
    firstcard = "";
    secondcard = "";
    let kadho = document.querySelectorAll('.card_selected');
    kadho.forEach((Element) => {
        Element.classList.remove('card_selected');
    })
}

//card selection on selected make it yellow border
let clickcount = 0;
let firstcard = "";
let secondcard = "";

parentDiv.addEventListener('click', (event) => {
    let curCard = event.target;

    if (curCard.id === "card-section") { return false }

    clickcount++;

    if (clickcount < 3) {

        if (clickcount === 1) {
            firstcard = curCard.parentNode.dataset.name;
            curCard.parentNode.classList.add('card_selected');
        } else {
            var cardParent = curCard.parentNode;

            if (cardParent.classList.contains('card_selected')) {
                // If the class is present, remove it
                cardParent.classList.remove('card_selected');
                resetGame();
            } else {
                // If the class is not present, add it
                secondcard = curCard.parentNode.dataset.name;
                cardParent.classList.add('card_selected');
            }
        }

        if (firstcard !== "" && secondcard !== "") {
            if (firstcard === secondcard) {
                score += 5;
                // curCard.classList.add('card_match')
                setTimeout(() => {
                    cardmatches()
                    if (score != 50)
                        runConfettiForTwoSeconds();
                    else
                        runcont();

                    resetGame();
                }, 1000)

            } else {
                setTimeout(() => {
                    resetGame()
                }, 1000)
            }
        }

    }

})

parentDiv.addEventListener('mouseover', (event) => {
    let currcard = event.target;
    if (currcard.id != "card-section") {
        currcard.classList.add('card_howwer');
    }
})

parentDiv.addEventListener('mouseout', (event) => {
    let currcard = event.target;
    currcard.classList.remove("card_howwer");

})


//to suffle by every refresh using random() function 
let shuffledChild = Array.from(gamecard).sort(() => 0.5 - Math.random());

for (let i = 0; i < shuffledChild.length; i++) {

    const childDiv = document.createElement('div')
    childDiv.classList.add('card')
    childDiv.dataset.name = shuffledChild[i].name;
    // childDiv.style.backgroundImage = `url(${shuffledChild[i].img})`;

    const front_div = document.createElement('div');
    front_div.classList.add('front-card')

    const back_div = document.createElement('div');
    back_div.classList.add('back-card')

    back_div.style.backgroundImage = `url(${shuffledChild[i].img})`;
    back_div.style.backgroundSize = "100% 100%";

    parentDiv.appendChild(childDiv)

    childDiv.appendChild(front_div)
    childDiv.appendChild(back_div)
}