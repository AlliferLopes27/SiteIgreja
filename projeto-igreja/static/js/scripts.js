// FUNÇÃO DO TOAST (BOOTSTRAP)
function mostrarToast(mensagem, tipo = "success") {

    const toastEl = document.getElementById('liveToast');

    if (!toastEl) return;

    // muda texto
    toastEl.querySelector('.toast-body').innerText = mensagem;

    // muda cor dinamicamente (opcional)
    toastEl.classList.remove("text-bg-success", "text-bg-danger", "text-bg-warning");
    toastEl.classList.add("text-bg-" + tipo);

    const toast = new bootstrap.Toast(toastEl);

    toast.show();
}

// DETECTA PARÂMETROS DA URL (FLASK)
window.onload = function () {

    const urlParams = new URLSearchParams(window.location.search);

    let temMensagem = false;

    // EVENTOS
    if (urlParams.get('evento') === 'criado') {
        mostrarToast("Evento criado com sucesso!", "success");
        temMensagem = true;
    }

    if (urlParams.get('evento') === 'editado') {
        mostrarToast("Evento atualizado com sucesso!", "success");
        temMensagem = true;
    }

    if (urlParams.get('evento') === 'excluido') {
        mostrarToast("Evento excluído com sucesso!", "danger");
        temMensagem = true;
    }

    // PEDIDOS
    if (urlParams.get('enviado') === '1') {
        mostrarToast("Pedido de oração enviado com sucesso!", "success");
        temMensagem = true;
    }

    // LOGIN
    if (urlParams.get('auth') === 'login_success') {
        mostrarToast("Login realizado com sucesso!", "success");
        temMensagem = true;
    }

    if (urlParams.get('auth') === 'login_error') {
        mostrarToast("Email ou senha inválidos!", "danger");
        temMensagem = true;
    }

    if (urlParams.get('auth') === 'logout_success') {
        mostrarToast("Logout realizado com sucesso!", "info");
        temMensagem = true;
    }

    // LIMPA URL PARA NÃO REPETIR AO RECARREGAR
    if (temMensagem) {
        window.history.replaceState(
            {},
            document.title,
            window.location.pathname
        );
    }
};

// Seleciona botão
const btnTopo = document.getElementById("btn-topo");

// Mostrar botão ao rolar
window.onscroll = function () {

    if (document.body.scrollTop > 200 ||
        document.documentElement.scrollTop > 200) {

        btnTopo.style.display = "block";

    } else {

        btnTopo.style.display = "none";
    }
};

// Voltar ao topo
btnTopo.addEventListener("click", function () {

    window.scrollTo({

        top: 0,

        behavior: "smooth"
    });
});
