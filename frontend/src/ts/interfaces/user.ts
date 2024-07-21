interface UserRegistrationData {
    first_name: string
    last_name: string
    email: string
    password: string
    age?: number
    tel?: string
    photo?: File
}
interface UserRegistrationDataErrors extends 
Partial<Omit<UserRegistrationData, "age" | "photo">> {
    age?: string
}


export type {
    UserRegistrationData,
    UserRegistrationDataErrors,
}
