import { CommonRequestParams, CommonRequestWithAuthParams } from "@/ts/interfaces"
import axios from "axios"


export default {
    async commonRequest(
        {state}:{state: any},
        request_params:CommonRequestParams
    ){
        return (await axios({
            ...request_params,
            baseURL: state.server_url,
        })).data
        
    },
    async commonRequestWithAuth(
        {state}:{state: any},
        request_params:CommonRequestWithAuthParams
    ){
        return (await axios({
            ...request_params,
            baseURL: state.server_url,
            withCredentials: true,
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            }
        })).data
        
    }
}
