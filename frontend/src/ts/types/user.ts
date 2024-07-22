import {UserLoginData, UserRegistrationData} from "../interfaces";


type ReceivedUserType = Omit<UserRegistrationData, "password">
type UserLoginErrorData = Partial<UserLoginData>


export type {
    ReceivedUserType,
    UserLoginErrorData
}
