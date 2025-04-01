const importar_dados = async () => {
    try {
        const resposta = await fetch('http://localhost:1250');
        const relatorio = await resposta.json();
        return relatorio;
    } catch (error) {
        console.error(error);
    }
}

 export default importar_dados;

