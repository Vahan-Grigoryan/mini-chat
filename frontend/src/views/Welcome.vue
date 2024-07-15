<template>
    <ui-centered-content>
        <img src="@/assets/images/anonymous_emblem.png" alt="">
        <p>Welcome to <i>"chat name:)"</i></p>
        <p>Login to continue</p>
        <ui-ok-button @click="$router.push('/login')">Log in</ui-ok-button>
        <ui-ok-button @click="$router.push('/registration')">Sign up</ui-ok-button>
        <ui-ok-button @click="$router.push('/home')">Anonymous temporary chat</ui-ok-button>
    </ui-centered-content>
</template>

<script>
</script>

<style scoped src="@/assets/css/welcome.css">
</style>
