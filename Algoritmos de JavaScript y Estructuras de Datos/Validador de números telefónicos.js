/*
Devuelve true si la cadena pasada concuerda con un número de teléfono válido en Estados Unidos.

El usuario puede completar el campo del formulario de la forma que elija, siempre que tenga el formato de un número estadounidense válido. Los siguientes ejemplos son de formatos válidos para números estadounidenses (consulte las pruebas a continuación para otras variantes):

555-555-5555
(555)555-5555
(555) 555-5555
555 555 5555
5555555555
1 555 555 5555
Para este desafío se te presentará una cadena como 800-692-7753 o 8oo-six427676;laskdjf. Tu trabajo es validar o rechazar el número de teléfono estadounidense basado en cualquier combinación de los formatos proporcionados arriba. El código de área es obligatorio. Si el código de país es proporcionado, debes confirmar que el código de país es 1. Devuelve true si la cadena es un número de teléfono estadounidense valido; de lo contrario devuelve false.
*/

function telephoneCheck(str) {
    let reg = /(^\d{10}$)|(^1{1}\(\d{3}\))|(^1{1}\s\d{3}\s)|(^\d{3}-{1}\d{3}-{1}\d{4})|(^\({1}\d{3}\){1}\d{3}-{1}\d{4})|(^\d{1}\s\d{3}-\d{3}-\d{4})|(^1{1}\s\(\d{3}\)\s\d{3}-\d{3})/; 
    return reg.test(str);
  }
  
  telephoneCheck("(555)5(55?)-5555");