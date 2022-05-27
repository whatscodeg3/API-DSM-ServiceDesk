function graficoDinamico(data) {
  console.log(data)
  const ctx1 = document.getElementById('grafico1').getContext('2d');
  const myChart1 = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'],
      datasets: [
        {
          label: 'Chamados Abertos',
          data: [23, 31, 56, 76, 54, 74, 21],
          backgroundColor: ['#FF4343'],
          borderColor: ['#292A2F'],
          borderWidth: 1
        },
        {
          label: 'Chamados Fechados',
          data: [12, 54, 34, 87, 56, 43, 23],
          backgroundColor: ['#6CEC90'],
          borderColor: ['#292A2F'],
          borderWidth: 1
        }]
    },
    options: {
      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    }
  })
};