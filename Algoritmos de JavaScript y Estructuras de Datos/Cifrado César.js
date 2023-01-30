/*
Uno de los cifrados más simples y conocidos es el cifrado César, también conocido como cifrado por desplazamiento. En un cifrado por desplazamiento los significados de las letras se desplazan por una cantidad determinada.

Un uso moderno común es el cifrado ROT13, donde los valores de las letras son desplazados por 13 lugares. Así que A ↔ N, B ↔ O y así sucesivamente.

Escribe una función que reciba una cadena codificada en ROT13 como entrada y devuelva una cadena decodificada.

Todas las letras estarán en mayúsculas. No transformes ningún carácter no alfabético (espacios, puntuación, por ejemplo), pero si transmítelos.
*/

function rot13(str) {
    let reg = /[^a-z0-9]/gmi;
    let res = "";
    let dic = {
      A:0,B:1,C:2,D:3,E:4,F:5,G:6,H:7,
      I:8,J:9,K:10,L:11,M:12,N:13,O:14,
      P:15,Q:16,R:17,S:18,T:19,U:20,V:21,
      W:22,X:23,Y:24,Z:25
    };
  
    for(let i=0; i<str.length; i++) {
      let c = str[i].replace(reg, " ");
      if (c == " ") {
        res = res.concat(str[i]);
      }
      else {
        let val = dic[str[i]];
        let newPos = (val + 13) > 25 ? val + 13 - 26 : val + 13;
        res = res.concat(Object.keys(dic).find(key => dic[key] === newPos));
      }
    }
  
    return res;
  }
  
  rot13("SERR CVMMN!");