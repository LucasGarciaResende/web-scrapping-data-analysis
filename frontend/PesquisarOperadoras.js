const pesquisar_operadoras = async (pesquisa) => {
    try {
        const resposta = await fetch("http://localhost:1250", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ busca: pesquisa })
        });
        const resultado = await resposta.json();
        return resultado;
    } catch (error) {
        console.error("Erro na pesquisa: ", error);
    }
}

export default pesquisar_operadoras;