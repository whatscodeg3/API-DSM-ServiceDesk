function abreModal(modalID) {
   const modal = document.getElementById(modalID);
   modal.classList.add('mostrar');
   
   // para fechar
   modal.addEventListener('click', (e) => {
      if(e.target.id == modalID || e.target.className == 'fechar') {
         modal.classList.remove('mostrar')
      };
   });
}

