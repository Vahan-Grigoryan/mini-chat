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
        <ui-ok-button @click="login_user">Sign up</ui-ok-button>
    </ui-centered-content>
</template>

<script setup lang="ts">
import {
    AxiosErrorResponse,
    UserRegistrationData,
    UserRegistrationDataErrors,
} from "@/ts/interfaces"
import { ReceivedUserType } from "@/ts/types"
import { authorizeUser } from "@/utils/common_requests"
import { clearErrorData, fillErrorData } from "@/utils/form_submission"
import { reactive, ref } from "vue"
import { useStore } from "vuex"


const store = useStore()
const db_integrity_error = ref<string | null>(null)
const user_data: UserRegistrationData = reactive({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
})
const user_data_errors: UserRegistrationDataErrors = reactive({ })


async function create_user(): Promise<ReceivedUserType | undefined> {
    // Create new user, show invalid inserted fields error messages if needed
    clearErrorData(user_data_errors)
    try{
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
        db_integrity_error.value = fillErrorData(
            err as AxiosErrorResponse<UserRegistrationDataErrors>,
            user_data_errors
        )
    }
}
async function login_user(): Promise<void> {
    // Receive tokens, set access_token in LocalStorage
    const user: ReceivedUserType | undefined = await create_user()
    if(!user) return
    authorizeUser(
        store,
        {
            username: user["email"],
            password: user_data["password"],
        }
    )
}
</script>

<style scoped src="@/assets/css/registration.css">
</style>
