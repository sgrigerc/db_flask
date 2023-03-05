window.onload = () => {
   let input = document.querySelector('#input');
   input.oninput = function() {
      console.log(this.value);
   };
};

// document.querySelector('#elastic').oninput = function(){
//    let val = this.value.trim();
//    let elasticItems = document.querySelectorAll('.elastic li');
//    if (val != ''){
//       elasticItems.forEach(function(elem){
//          if (elem.innerText.search(val) == -1) {
//             elem.classList.add('hide');
//          }
//          else {
//             elem.classList.remove('hide');
//          }
//       });
//    }
//    else {
//       elasticItems.forEach(function(elem){
//          elem.classList.remove('hide');
//       });
//    }
// }