interface CommonRequestParams {
    url: string;
    method: string,
    data?: object;
    withCredentials?: boolean,
    headers?: {
        "Content-Type": string
    };
}
interface CommonRequestWithAuthParams {
    url: string
    method: string,
    data?: object
    headers?: {
        "Authorization": string
    };
}
interface AxiosErrorResponse<Fields> {
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

export type {
    CommonRequestParams,
    CommonRequestWithAuthParams,
    AxiosErrorResponse,
}
