import {UserRegistrationData} from "../interfaces";


type ReceivedUserType = Omit<UserRegistrationData, "password">


export type {
    ReceivedUserType,
}
