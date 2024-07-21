<template>
    <ui-centered-content>
        <h2>Registration</h2>
        <span v-if="db_integrity_error">{{db_integrity_error}}</span>
        <ui-input
	    type="text"
	    placeholder="*first name"
        v-model="user_data['first_name']"
        :error_message="user_data_errors['first_name']"
	    />
        <ui-input
		type="text"
		placeholder="*last name"
        v-model="user_data['last_name']"
        :error_message="user_data_errors['last_name']"
		/>
        <ui-input
		type="email"
		placeholder="*email"
        v-model="user_data['email']"
        :error_message="user_data_errors['email']"
		/>
        <ui-input
		type="password"
		placeholder="*password"
        v-model="user_data['password']"
        :error_message="user_data_errors['password']"
		/>
        <ui-input
		type="number"
		placeholder="tel(with '+')"
        v-model="user_data['tel']"
        :error_message="user_data_errors['tel']"
		/>
        <ui-input
		type="number"
		placeholder="age"
        v-model="user_data['age']"
        :error_message="user_data_errors['age']"
		/>
        <ui-input
		type="file"
        v-model="user_data['photo']"
		/>
        <ui-ok-button @click="authorize_user">Sign up</ui-ok-button>
    </ui-centered-content>
</template>

<script setup lang="ts">
import {
    AxiosErrorResponse,
    UserRegistrationData,
    UserRegistrationDataErrors,
    ReceivedAccessToken,
} from "@/ts/interfaces"
import { ReceivedUserType } from "@/ts/types"
import { reactive, ref } from "vue"
import { useStore } from "vuex"


const store = useStore()
const db_integrity_error = ref<string>("")
const user_data: UserRegistrationData = reactive({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
})
const user_data_errors: UserRegistrationDataErrors = reactive({
    first_name: undefined,
    last_name: undefined,
    email: undefined,
    password: undefined,
    age: undefined,
    tel: undefined,
})

async function create_user(): Promise<ReceivedUserType | undefined> {
    // Create new user, show invalid inserted fields error messages if needed
    try{
        for(const key in user_data_errors){
            // Clear error messages
            user_data_errors[(key as keyof UserRegistrationDataErrors)] = ""
        }
        db_integrity_error.value = ""
        const created_user: ReceivedUserType = await store.dispatch(
            "commonRequest",
            {
                url: "registration",
                method: "post",
                data: user_data,
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            }
        )
        return created_user
    }catch(err){
        const axiosError = err as AxiosErrorResponse<UserRegistrationDataErrors>
        if(Array.isArray(axiosError?.response?.data.detail)){
            for(const {field, message} of axiosError.response.data.detail){
                user_data_errors[field] = message
            }
        }
        else if(axiosError?.response?.data.detail){
            db_integrity_error.value = axiosError.response.data.detail["message"]
        }
    }
}
async function authorize_user(): Promise<void> {
    // Receive tokens, set access_token in LocalStorage
    const user: ReceivedUserType | undefined = await create_user()
    if(!user) return
    const { access_token }: ReceivedAccessToken = await store.dispatch(
        "commonRequest",
        {
            url: "tokens",
            method: "post",
            data: {
                username: user["email"],
                password: user_data["password"],
            },
            headers: {
                "Content-Type": "multipart/form-data"
            },
            withCredentials: true
        }
    )
    localStorage.setItem("access_token", access_token)
}
</script>

<style scoped src="@/assets/css/registration.css">
</style>
