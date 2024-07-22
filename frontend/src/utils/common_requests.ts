/*
There are request funcs which used in more than 1 places in project
*/
import { ReceivedAccessToken, UserLoginData } from "@/ts/interfaces";
import { Store } from "vuex";


async function authorizeUser(
    store: Store<any>,
    user_credentials: UserLoginData
): Promise<void> {
    // Authorize user by setting access_token in LS,
    // and receiving refresh_token in cookies
    const { access_token }: ReceivedAccessToken = await store.dispatch(
        "commonRequest",
        {
            url: "tokens",
            method: "post",
            data: user_credentials,
            headers: {
                "Content-Type": "multipart/form-data"
            },
            withCredentials: true
        }
    )
    localStorage.setItem("access_token", access_token)
}


export {
    authorizeUser
}
