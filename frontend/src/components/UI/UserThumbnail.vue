<template>
    <img
    v-if="photo"
	:src="photo"
	alt=""
    >
    <div
    v-else
    class="photo_replacement"
    >
        {{ (first_name[0] + last_name[0]).toUpperCase() }}
    </div>
</template>

<script setup lang="ts">
import { UserMiniInfo } from "@/ts/types/user";


const thumbnail_data = defineProps<UserMiniInfo>()
</script>

<style scoped>
img, .photo_replacement {
    width: 50px;
    height: 50px;
    border-radius: 50px;
    margin-right: 10px;
    object-fit: cover;
}
.photo_replacement {
    display: flex;
    align-items: center;
    justify-content: center;
    background: gray;
    font-size: 15px;
    color: var(--dark-mode-ok-font-color);
}
</style>
