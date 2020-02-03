let originalBoard;
let humanPlayer ='O';
let aiPlayer = 'X';
const winCombos =[
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 4, 8],
  [6, 4, 2],
  [2, 5, 8],
  [1, 4, 7],
  [0, 3, 6]
];

const cells = document.querySelectorAll('.cell');
startGame();

function selectSign(sign){
  humanPlayer = sign;
  aiPlayer = sign==='O' ? 'X' :'O';
  originalBoard = Array.from(Array(9).keys());
  for (let i = 0; i < cells.length; i++) {
    cells[i].addEventListener('click', outerStep, false);
  }
  if (aiPlayer === 'X') {
    innerStep(bestSpot(),aiPlayer);
  }
  document.querySelector('.selectSign').style.display = "none";
}

function startGame() {
  document.querySelector('.endgame').style.display = "none";
  document.querySelector('.endgame .text').innerText ="";
  document.querySelector('.selectSign').style.display = "block";
  for (let i = 0; i < cells.length; i++) {
    cells[i].innerText = '';
    cells[i].style.removeProperty('background-color');
  }
}

function outerStep(cell) {
  if (typeof originalBoard[cell.target.id] ==='number') {
    innerStep(cell.target.id, humanPlayer);
    if (!checkWin(originalBoard, humanPlayer) && !checkTie())
      innerStep(bestSpot(), aiPlayer);
  }
}

function innerStep(cellId, player) {
  originalBoard[cellId] = player;
  document.getElementById(cellId).innerText = player;
  let gameWon = checkWin(originalBoard, player);
  if (gameWon) gameOver(gameWon);
  checkTie();
}

function checkWin(board, player) {
  let plays = board.reduce((accumulator, boardElem, i) => (boardElem === player) ? accumulator.concat(i) : accumulator, []);
  let gameWon = null;
  for (let [index, winCombo] of winCombos.entries()) {
    if (winCombo.every(elem => plays.indexOf(elem) > -1)) {
      gameWon = {index: index, player: player};
      break;
    }
  }
  return gameWon;
}

function gameOver(gameWon){
  for (let index of winCombos[gameWon.index]) {
    document.getElementById(index).style.backgroundColor =
      gameWon.player === humanPlayer ? "#210B2C" : "#632124";
  }
  for (let i=0; i < cells.length; i++) {
    cells[i].removeEventListener('click', outerStep, false);
  }
  declareWinner(gameWon.player === humanPlayer ? "You won, yeyy!" : "You lost");
}

function declareWinner(who) {
  document.querySelector(".endgame").style.display = "block";
  document.querySelector(".endgame .text").innerText = who;
}

function emptyCells() {
  return originalBoard.filter((elem, i) => i===elem);
}

function checkTie() {
  if (emptyCells().length === 0){
    for (cell of cells) {
      cell.style.backgroundColor = "#4F4C54";
      cell.removeEventListener('click', outerStep, false);
    }
    declareWinner("Tie game");
    return true;
  }
  return false;
}

function minimax(newBoard, player) {
  var availSpots = emptyCells(newBoard);

  if (checkWin(newBoard, humanPlayer)) {
    return {score: -10};
  } else if (checkWin(newBoard, aiPlayer)) {
    return {score: 10};
  } else if (availSpots.length === 0) {
    return {score: 0};
  }

  var moves = [];
  for (let i = 0; i < availSpots.length; i ++) {
    var move = {};
    move.index = newBoard[availSpots[i]];
    newBoard[availSpots[i]] = player;

    if (player === aiPlayer)
      move.score = minimax(newBoard, humanPlayer).score;
    else
       move.score =  minimax(newBoard, aiPlayer).score;
    newBoard[availSpots[i]] = move.index;
    if ((player === aiPlayer && move.score === 10) || (player === humanPlayer && move.score === -10))
      return move;
    else
      moves.push(move);
  }

  let bestMove, bestScore;
  if (player === aiPlayer) {
    bestScore = -1000;
    for(let i = 0; i < moves.length; i++) {
      if (moves[i].score > bestScore) {
        bestScore = moves[i].score;
        bestMove = i;
      }
    }
  } else {
      bestScore = 1000;
      for(let i = 0; i < moves.length; i++) {
      if (moves[i].score < bestScore) {
        bestScore = moves[i].score;
        bestMove = i;
      }
    }
  }

  return moves[bestMove];
}

function bestSpot(){
  return minimax(originalBoard, aiPlayer).index;
}
