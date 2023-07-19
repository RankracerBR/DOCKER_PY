// Função para carregar imagens visíveis quando a página é rolada
  function carregarImagensVisiveis() {
    const imagens = document.querySelectorAll('img[loading="lazy"]');
    imagens.forEach((imagem) => {
      if (imagem.getBoundingClientRect().top <= window.innerHeight) {
        imagem.src = imagem.dataset.src;
        imagem.removeAttribute('loading');
      }
    });
  }

  // Carregar imagens visíveis no carregamento inicial da página
  carregarImagensVisiveis();

  // Evento para carregar imagens à medida que a página é rolada
  window.addEventListener('scroll', carregarImagensVisiveis);

