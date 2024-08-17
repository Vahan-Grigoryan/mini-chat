<template>
    <div class="contact_box">
        <ui-user-thumbnail
        :first_name="first_name"
        :last_name="last_name"
        :photo="photo"
        />
        <div class="contact_info">
            <span class="username">{{ first_name + " " + last_name }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">
import { UserMiniInfo } from "@/ts/types/user";


const contact_data = defineProps<UserMiniInfo & {}>() // in "{}" will be last message in conversation in future
</script>

<style scoped>
.contact_box {
    width: 100%;
    display: flex;
    padding: 10px;
    height: 70px;
}
.contact_info {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.contact_info span{
    font-size: 16px;
    color: var(--dark-mode-ok-font-color);
    display: inline-block;
}
</style>
