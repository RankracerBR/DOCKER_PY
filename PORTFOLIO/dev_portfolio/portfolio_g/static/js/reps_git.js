    // Token de acesso pessoal do GitHub
    const accessToken = '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';

    // Nome de usuário do GitHub
    const username = 'RankracerBR';

    // URL da API do GitHub para obter os repositórios do usuário
    const apiUrl = `https://api.github.com/users/${username}/repos`;

    // Função para obter e exibir os repositórios
    function showRepositories() {
        $.ajax({
          url: apiUrl,
          headers: {
            Authorization: `token ${accessToken}`
          },
          success: function (data) {
            // Limpar a lista de repositórios antes de exibir os novos
            $("#repos-list").empty();
  
            // Iterar sobre a lista de repositórios e adicioná-los à lista
            data.forEach(repo => {
              const listItem = `<li><a href="https://github.com/${username}/${repo.name}" target="_blank"onclick="showReadme('${repo.name}')">${repo.name}</a></li>`;
              $("#repos-list").append(listItem);
            });
          },
          error: function (error) {
            console.error('Erro ao obter repositórios:', error);
          }
        });
      }
  
      // Função para obter e exibir o conteúdo do README.md
      function showReadme(repoName) {
        const readmeUrl = `https://raw.githubusercontent.com/${username}/${repoName}/master/README.md`;
  
        $.ajax({
          url: readmeUrl,
          success: function (data) {
            const converter = new showdown.Converter();
            const htmlContent = converter.makeHtml(data);
            $("#readme-content").html(htmlContent);
          },
          error: function (error) {
            console.error('Erro ao obter o README:', error);
            $("#readme-content").html("<p>O README.md não foi encontrado para este repositório.</p>");
          }
        });
}
  

function showReadme(repoName) {
    const readmeUrl = `https://raw.githubusercontent.com/${username}/${repoName}/master/README.md`;

    $.ajax({
        url: readmeUrl,
        sucess: function (data) {
            const converter = new showdown.Converter();
            const htmlContent = converter.makeHtml(data);
            $('#readme-content').html(htmlContent);
        },
        error: function (error) {
            console.error('Error ao obter o README: ', error);
            $('#readme-content').html("<p>O README.md não foi encontrado para este repositório.</p>");
        }
    });
}
// Chamar a função para exibir os repositórios quando a página carregar
$(document).ready(function () {
  showRepositories();
});

$(document).ready(function () {
    showReadme();
});
