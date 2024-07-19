import { createStore } from 'vuex'
import backend_actions from './actions'


export default createStore({
    state: {
        server_url: "http://localhost:8000/"
    },
    getters: {
    },
    mutations: {
    },
    actions: {
        ...backend_actions
    },
    modules: {
    }
})
