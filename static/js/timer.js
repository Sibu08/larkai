console.log("timer")

var ecg = document.getElementById("startBtn")

var pcg = document.getElementById("startBtn2")
pcg.style.display = "none"

var generate=document.getElementById("generate")
generate.style.display="none"

var generate2=document.getElementById("generate2")
generate2.style.display="none"

const FULL_DASH_ARRAY = 283;
const WARNING_THRESHOLD = 10;
const ALERT_THRESHOLD = 5;

const COLOR_CODES = {
  info: {
    color: "green"
  },
  warning: {
    color: "orange",
    threshold: WARNING_THRESHOLD
  },
  alert: {
    color: "red",
    threshold: ALERT_THRESHOLD
  }
};

// const TIME_LIMIT = 15;
const TIME_LIMIT = 3;
let timePassed = 0;
let timeLeft = TIME_LIMIT;
let timerInterval = null;
let remainingPathColor = COLOR_CODES.info.color;

document.getElementById("app").innerHTML = `
<div class="base-timer">
  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g class="base-timer__circle">
      <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
      <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
      ></path>
    </g>
  </svg>
  <span id="base-timer-label" class="base-timer__label">${formatTime(
    timeLeft
  )}</span>
</div>
`;
var btn=document.getElementById("startBtn")

function runtimer(){
  timer_status=true
  done=false
  retake+=1
  if (retake>=2){
    save_data=[]
  }
  console.log('Inside runtimer :',timer_status)
  startTimer()
}
function runtimer2(){
  startTimer2()
}

function onTimesUp() {
  clearInterval(timerInterval);
  if (document.getElementById('startBtn').innerHTML == 'Retake ECG'){
    // const { alert, warning, info} = COLOR_CODES;
    // document.getElementById("base-timer-path-remaining").classList.remove(alert.color);
    // document.getElementById("base-timer-path-remaining").classList.add(info.color);
    generate.style.display='inline'
  }
  timer_status=false
  console.log('Inside onTimeup :',timer_status)
  timeLeft = TIME_LIMIT
  timePassed = 0
  document.getElementById("startBtn").innerHTML = 'Retake ECG'
  generate.style.display='inline'
}

function startTimer() {
  if (document.getElementById('startBtn').innerHTML == 'Retake ECG'){
    const { alert, warning, info} = COLOR_CODES;
    document.getElementById("base-timer-path-remaining").classList.remove(alert.color);
    document.getElementById("base-timer-path-remaining").classList.add(info.color);
  }
  timerInterval = setInterval(() => {
    timePassed = timePassed += 1;
    timeLeft = TIME_LIMIT - timePassed;
    document.getElementById("base-timer-label").innerHTML = formatTime(
      timeLeft
    );
    setCircleDasharray();
    setRemainingPathColor(timeLeft);

    if (timeLeft === 0) {
      onTimesUp();
    }
  }, 1000);
}

function onTimesUp2() {
  clearInterval(timerInterval);
  if (document.getElementById('startBtn2').innerHTML == 'Retake PCG'){
    generate2.style.display='inline'
  }
  timeLeft = TIME_LIMIT
  timePassed = 0
  document.getElementById("startBtn2").innerHTML = 'Retake PCG'
  generate2.style.display='inline'
  

}

function startTimer2() {
  if (document.getElementById('startBtn2').innerHTML == 'Retake PCG'){
    const { alert, warning, info} = COLOR_CODES;
    document.getElementById("base-timer-path-remaining").classList.remove(alert.color);
    document.getElementById("base-timer-path-remaining").classList.add(info.color);
  }
  timerInterval = setInterval(() => {
    timePassed = timePassed += 1;
    timeLeft = TIME_LIMIT - timePassed;
    document.getElementById("base-timer-label").innerHTML = formatTime(
      timeLeft
    );
    setCircleDasharray();
    setRemainingPathColor(timeLeft);

    if (timeLeft === 0) {
      onTimesUp2();
    }
  }, 1000);
}

function formatTime(time) {
  const minutes = Math.floor(time / 60);
  let seconds = time % 60;

  if (seconds < 10) {
    seconds = `0${seconds}`;
  }

  return `${minutes}:${seconds}`;
}

function setRemainingPathColor(timeLeft) {
  const { alert, warning, info } = COLOR_CODES;
  if (timeLeft <= alert.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(warning.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(alert.color);
  } else if (timeLeft <= warning.threshold) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(info.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(warning.color);
  }
}
function calculateTimeFraction() {
    const rawTimeFraction = timeLeft / TIME_LIMIT;
    return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
}
  
function setCircleDasharray() {
    const circleDasharray = `${(
      calculateTimeFraction() * FULL_DASH_ARRAY
    ).toFixed(0)} 283`;
    document
      .getElementById("base-timer-path-remaining")
      .setAttribute("stroke-dasharray", circleDasharray);
}

chr  =document.getElementById("chart")
chr2 = document.getElementById("chart2")
h1pcg = document.getElementById("h1pcg")
h1ecg = document.getElementById("h1ecg")

function show_pcg(){
  done=true
  pcg.style.display = "inline"
  chr.style.display = "none"
  chr2.style.display = "block"
  //h1pcg.style.display = "inline"
  h1ecg.innerHTML ="PCG Reading"
  ecg.style.display = "none"
  generate.style.display = "none"
  if (document.getElementById('startBtn2').innerHTML == 'Record PCG'){
    const { alert, warning, info} = COLOR_CODES;
    document.getElementById("base-timer-path-remaining").classList.remove(alert.color);
    document.getElementById("base-timer-path-remaining").classList.add(info.color);
    v=formatTime(timeLeft)
    //console.log(v)
    document.getElementById("base-timer-label").innerHTML = v
  }
}