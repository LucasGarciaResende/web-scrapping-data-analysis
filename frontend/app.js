import importar_dados from './ImportarDados.js'
import pesquisar_operadoras from './PesquisarOperadoras.js'

const app = Vue.createApp({
    data() {
        return {
            relatorio: [],
            pesquisa: ''
        }
    },
    mounted() {
        this.carregar_dados()
    },
    methods: {
        async carregar_dados() {
            this.relatorio = await importar_dados()
        },
        async pesquisar() {
            this.relatorio = await pesquisar_operadoras(this.pesquisa)
        }
    }
})

app.mount('#app')