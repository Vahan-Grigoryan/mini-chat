import axios from "axios"


type CommonRequestParams = {
    url: string;
    method: string,
    data?: object;
    withCredentials?: boolean,
    headers?: {
        "Content-Type": string
    };
}
type CommonRequestWithAuthParams = {
    url: string
    method: string,
    data?: object
    headers?: {
        "Authorization": string
    };
}
export interface AxiosSuccessResponse {
    data: {
        [key: string]: any
    }
}
export interface AxiosErrorResponse<Fields> {
    data: {
        response: {
            data: {
                detail: {
                    field: keyof Fields
                    message: string
                }[] | {
                    message: string
                }
            }
        }
    }
}
export default {
    async commonRequest(
        {state}:{state: any},
        request_params:CommonRequestParams
    ){
        return await axios({
            ...request_params,
            baseURL: state.server_url,
        })
        
    },
    async commonRequestWithAuth(
        {state}:{state: any},
        request_params:CommonRequestWithAuthParams
    ){
        return await axios({
            ...request_params,
            baseURL: state.server_url,
            withCredentials: true,
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("access_token")}`
            }
        })
        
    }
}
