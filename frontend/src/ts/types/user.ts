import { UserLoginData, UserRegistrationData } from "../interfaces/user";


type UserRegistrationDataErrors = Partial<Omit<UserRegistrationData, "age" | "photo">>  & {
    age?: string
}
type UserMiniInfo = Pick<UserRegistrationData, "first_name" | "last_name"> & {
    photo?: string
}
type ReceivedUserType = Omit<UserRegistrationData, "password" | "photo"> & {
    photo?: string
}
type UserLoginErrorData = Partial<UserLoginData>


export type {
    ReceivedUserType,
    UserLoginErrorData,
    UserRegistrationDataErrors,
    UserMiniInfo,
}
