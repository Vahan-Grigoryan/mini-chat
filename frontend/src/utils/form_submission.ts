/*
There are support functions for form submissiond
*/
import { AxiosErrorResponse } from "@/ts/interfaces"


function clearErrorData<DataType>(
    data: Partial<Record<keyof DataType, string>>
): void {
    // Clear all error fields in data,
    // pay attention that func changes fields in place!
    for(const key in data){
        data[key] = ""
    }
}

function fillErrorData<DataType>(
    axios_error_response: AxiosErrorResponse<DataType>,
    data?: Partial<Record<keyof DataType, string>>
): string | null {
    // Fill fields with error messages(in place) and return global error message or null
    if(Array.isArray(axios_error_response.response.data.detail) && data) {
        for(const {field, message} of axios_error_response.response.data.detail){
            data[field] = message
        }
    }
    else if(axios_error_response.response.data.detail){
        const message = axios_error_response.response.data.detail as { message: string }
        return message["message"]
    }
    return null
}

export {
    clearErrorData,
    fillErrorData,
}
