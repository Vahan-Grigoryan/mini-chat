<template>
    <ui-centered-content>
        <div class="login_box">
            <h2>Log in</h2>
            <span v-if="authorization_error">{{ authorization_error }}</span>
            <ui-input
            type="email"
            placeholder="email"
            v-model="user_login_data['username']"
            />
            <ui-input
            type="password"
            placeholder="password"
            v-model="user_login_data['password']"
            />
            <ui-ok-button @click="login_user">Log in</ui-ok-button>
        </div>
    </ui-centered-content>
</template>

<script setup lang="ts">
import { AxiosErrorResponse } from "@/ts/interfaces/request";
import { UserLoginData } from "@/ts/interfaces/user";
import { UserLoginErrorData } from "@/ts/types/user";
import { authorizeUser } from "@/utils/common_requests";
import { fillErrorData } from "@/utils/form_submission";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";


const router = useRouter()
const store = useStore()
const authorization_error = ref<string | null>(null)
const user_login_data: UserLoginData = reactive({
    username: "",
    password: ""
})


async function login_user(){
    authorization_error.value = null
    try{
        await authorizeUser(store, user_login_data)
    }catch(err){
        authorization_error.value = fillErrorData(
            err as AxiosErrorResponse<UserLoginErrorData>,
        )
    }
    router.push("/home")
}

</script>

<style scoped src="@/assets/css/login.css">
</style>
