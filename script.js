async function buscarUsuarios() {
  const lista = document.getElementById("listaUsuarios");

  try {
    const resposta = await fetch("https://avaliacaosw2-f0dy.onrender.com/usuarios");
    const usuarios = await resposta.json();

    lista.innerHTML = "";

    usuarios.forEach(usuario => {
      lista.innerHTML += `
        <div class="usuario">
          <h3>${usuario.nome}</h3>
          <p>Email: ${usuario.email}</p>
          <p>Telefone: ${usuario.telefone}</p>
        </div>
      `;
    });

  } catch (erro) {
    lista.innerHTML = "<p>Erro ao buscar usuários.</p>";
    console.error(erro);
  }
}