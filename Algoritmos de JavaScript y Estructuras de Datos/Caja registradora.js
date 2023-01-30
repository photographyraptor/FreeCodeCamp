/*
Diseña una función checkCashRegister() que acepte el precio de compra como primer argumento (price), la cantidad pagada como segundo argumento (cash), y el dinero en efectivo que tiene la caja (cid) como tercer argumento.

cid es un arreglo 2D que enumera las monedas disponibles.

La función checkCashRegister() siempre debe devolver un objeto con una clave status y una clave change.

Devuelve {status: "INSUFFICIENT_FUNDS", change: []} si el efectivo en caja es menor que el cambio necesario, o si no puedes devolver el cambio exacto.

Devuelve {status: "CLOSED", change: [...]} si el efectivo en caja como valor de la clave change es igual al cambio que se debe entregar.

En cualquier otro caso, devuelve {status: "OPEN", change: [...]}, con el cambio a entregar en monedas y billetes, ordenados de mayor a menor, como valor de la clave change.

Unidad Monetaria	Importe
Penny	$0.01 (PENNY)
Nickel	$0.05 (NICKEL)
Dime	$0.1 (DIME)
Quarter	$0.25 (QUARTER)
Dollar	$1 (ONE)
Five Dollars	$5 (FIVE)
Ten Dollars	$10 (TEN)
Twenty Dollars	$20 (TWENTY)
One-hundred Dollars	$100 (ONE HUNDRED)
A continuación, un ejemplo del efectivo en caja en formato de arreglo:

[
  ["PENNY", 1.01],
  ["NICKEL", 2.05],
  ["DIME", 3.1],
  ["QUARTER", 4.25],
  ["ONE", 90],
  ["FIVE", 55],
  ["TEN", 20],
  ["TWENTY", 60],
  ["ONE HUNDRED", 100]
]
*/

let coins = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.1,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100
  }
  
  function checkCashRegister(price, cash, cid) {
    let rest = cash - price;
    let calRest = rest;
    let candidates = [];
    for(let coin in coins) {
      if (rest >= coins[coin]) {
        candidates.unshift(coin);
      }
    }
  
    let change = [];
    for(let i=0; i<candidates.length; i++) {
      for(let j=cid.length -1;j>=0;j--) {
        if (cid[j][0] == candidates[i]) {
          let row = [];
          let toRemove = (Math.trunc(calRest / coins[cid[j][0]]) * coins[cid[j][0]]).toFixed(2);
          toRemove = toRemove > cid[j][1] ? cid[j][1] : toRemove;
          calRest = (calRest - toRemove).toFixed(2);
          if (toRemove > 0) {
            row.push(cid[j][0]);
            row.push(Number(Number(toRemove).toString()));
            change.push(row);
          }
          if (calRest <= 0) {
            cid[j][1] -= toRemove;          
            return calcRet(calRest, change, cid);
          }
        }
      }
    }
    return calcRet(calRest, change, cid);
  }
  
  function calcRet(calRest, change, cid) {
    let ret = {
      status: "",
      change: []
    }
  
    if (calRest > 0) {
      ret.status = "INSUFFICIENT_FUNDS";
      ret.change = [];
      return ret;
    }
    else {
      let formattedChange = [];
      for(let coin in coins) {
        let formattedRow = [];
        for(let i=0; i<change.length; i++) {
          if(change[i][0] == coin) {
            formattedRow.push(coin);
            formattedRow.push(change[i][1]);
            formattedChange.push(formattedRow);
          }
        }
        if (formattedRow.length == 0) {
          formattedRow.push(coin);
          formattedRow.push(0);
          formattedChange.push(formattedRow);
        }
      }
      
      for(let i=0; i<cid.length; i++) {      
        if (cid[i][1] > 0) {        
          ret.status = "OPEN";
          ret.change = change;
          return ret;
        }
      }
          
      ret.status = "CLOSED";
      ret.change = formattedChange;
      return ret;
    }
  }
  
  checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);