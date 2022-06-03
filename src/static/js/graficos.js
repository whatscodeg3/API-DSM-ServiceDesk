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

function graficoDinamico(solicitacoes_fechadas, solicitacoes_abertas, data_inicial, data_final) {
  console.log(solicitacoes_fechadas, solicitacoes_abertas);
  const total_dias = diasTotais(data_inicial, data_final);
  console.log(total_dias);
  const total_dias_array = Object.keys(new Array(total_dias + 1).fill(null).map(Number));
  console.log(total_dias_array.slice(1));
  const ctx1 = document.getElementById('grafico-especifico').getContext('2d');
  const myChart1 = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: total_dias_array.slice(1),
      datasets: [
        {
          label: 'Abertos',
          data: solicitacoes_abertas,
          backgroundColor: ['#FF4343'],
          borderColor: ['#292A2F'],
          borderWidth: 7,
          tension: 0.1
        },
        {
          label: 'Fechados',
          data: solicitacoes_fechadas,
          backgroundColor: ['#6CEC90'],
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

// Função para pegar o numero total de dias
function diasTotais(data_inicial, data_final) {
  const data_inicio = new Date(data_inicial);
  const data_fim = new Date(data_final);

  const diferenca = data_fim.getTime() - data_inicio.getTime();
  const dias_Totais = Math.ceil(diferenca / (1000 * 3600 * 24));
  return dias_Totais;

}