function graficoChamados(id, dado) {
  console.log(dado)
  const ctx1 = document.getElementById(id).getContext('2d');
  const myChart1 = new Chart(ctx1, {
    type: 'pie',
    data: {
      labels: ['Abertos', 'Fechados'],
      datasets: [
        {
          label: 'Chamados',
          data: dado,
          backgroundColor: ['#FF4343', '#6CEC90'],
          borderColor: ['#292A2F'],
          borderWidth: 7,
          tension: 0.1
        }
      ]
    },
    options: {
      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    }
  });

};

function graficoAvaliacoes(id, dado) {
  console.log(dado)
  const ctx4 = document.getElementById(id).getContext('2d');
  const myChart4 = new Chart(ctx4, {
    type: 'bar',
    data: {
      labels: ['Otimo', 'Bom', 'Regular', 'Péssimo'],
      datasets: [
        {
          label: 'Avaliações',
          data: dado,
          backgroundColor: ['#6CEC90', '#dbaf20', '#C67020', '#FF4343'],
          borderColor: ['#292A2F'],
          borderWidth: 7,
          tension: 0.1
        },
      ]
    },
  });
}