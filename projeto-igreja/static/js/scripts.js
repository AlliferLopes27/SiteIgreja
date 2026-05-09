

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

    // EVENTOS
    if (urlParams.get('evento') === 'criado') {
        mostrarToast("Evento criado com sucesso!", "success");
    }

    if (urlParams.get('evento') === 'editado') {
        mostrarToast("Evento atualizado com sucesso!", "success");
    }

    if (urlParams.get('evento') === 'excluido') {
        mostrarToast("Evento excluído com sucesso!", "danger");
    }

    // ✔ PEDIDOS (caso queira usar depois)
    if (urlParams.get('enviado') === '1') {
        mostrarToast("Pedido de oração enviado com sucesso!", "success");
    }
};