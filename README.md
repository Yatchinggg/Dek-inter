# Dek-inter
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Team Logic - Thai Consonant Drill</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background-color: #f4f4f4;
        }

        h1 {
            margin-top: 20px;
        }

        #gameArea {
            margin-top: 30px;
        }

        button {
            font-size: 20px;
            margin: 5px;
            padding: 10px 15px;
            cursor: pointer;
        }

        #hearts {
            font-size: 25px;
            color: red;
        }

        #question {
            font-size: 30px;
            margin: 20px;
        }

        #result {
            font-size: 20px;
            margin-top: 15px;
        }
    </style>
</head>
<body>

<h1>Team Logic - Thai Consonant Drill</h1>

<div id="hearts">❤️❤️❤️</div>

<div id="gameArea">
    <div id="question">Press Start</div>
    <div id="options"></div>
    <div id="result"></div>
    <button onclick="startGame()">Start</button>
</div>

<script>

const consonants = [
{char:"ก", name:"ko kai"},
{char:"ข", name:"kho khai"},
{char:"ฃ", name:"kho khuat"},
{char:"ค", name:"kho khwai"},
{char:"ฅ", name:"kho khon"},
{char:"ฆ", name:"kho rakhang"},
{char:"ง", name:"ngo ngu"},
{char:"จ", name:"cho chan"},
{char:"ฉ", name:"cho ching"},
{char:"ช", name:"cho chang"},
{char:"ซ", name:"so so"},
{char:"ฌ", name:"cho choe"},
{char:"ญ", name:"yo ying"},
{char:"ฎ", name:"do chada"},
{char:"ฏ", name:"to patak"},
{char:"ฐ", name:"tho than"},
{char:"ฑ", name:"tho nangmontho"},
{char:"ฒ", name:"tho phuthao"},
{char:"ณ", name:"no nen"},
{char:"ด", name:"do dek"},
{char:"ต", name:"to tao"},
{char:"ถ", name:"tho thung"},
{char:"ท", name:"tho thahan"},
{char:"ธ", name:"tho thong"},
{char:"น", name:"no nu"},
{char:"บ", name:"bo baimai"},
{char:"ป", name:"po pla"},
{char:"ผ", name:"pho phueng"},
{char:"ฝ", name:"fo fa"},
{char:"พ", name:"pho phan"},
{char:"ฟ", name:"fo fan"},
{char:"ภ", name:"pho samphao"},
{char:"ม", name:"mo ma"},
{char:"ย", name:"yo yak"},
{char:"ร", name:"ro ruea"},
{char:"ล", name:"lo ling"},
{char:"ว", name:"wo waen"},
{char:"ศ", name:"so sala"},
{char:"ษ", name:"so rusi"},
{char:"ส", name:"so suea"},
{char:"ห", name:"ho hip"},
{char:"ฬ", name:"lo chula"},
{char:"อ", name:"o ang"},
{char:"ฮ", name:"ho nokhuk"}
];

let hearts = 3;
let current;

function startGame() {
    hearts = 3;
    updateHearts();
    nextQuestion();
}

function updateHearts() {
    document.getElementById("hearts").innerText = "❤️".repeat(hearts);
}

function nextQuestion() {
    document.getElementById("result").innerText = "";
    current = consonants[Math.floor(Math.random()*consonants.length)];
    document.getElementById("question").innerText = current.name;

    let optionsDiv = document.getElementById("options");
    optionsDiv.innerHTML = "";

    let shuffled = consonants.sort(()=>0.5-Math.random()).slice(0,4);

    if (!shuffled.includes(current)) {
        shuffled[0] = current;
    }

    shuffled.forEach(item => {
        let btn = document.createElement("button");
        btn.innerText = item.char;
        btn.onclick = function() { checkAnswer(item); };
        optionsDiv.appendChild(btn);
    });
}

function checkAnswer(selected) {
    if (selected.char === current.char) {
        document.getElementById("result").innerText = 
            "Correct! " + current.char + " = " + current.name;
        nextQuestion();
    } else {
        hearts--;
        updateHearts();
        document.getElementById("result").innerText = "Wrong!";
        if (hearts === 0) {
            document.getElementById("question").innerText = "Game Over";
            document.getElementById("options").innerHTML = "";
        }
    }
}

</script>

</body>
</html>
