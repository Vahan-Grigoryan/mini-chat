<template>
    <ui-linking-message
    v-if="message.linking_message"
    :message="message.linking_message"
    />
    <h4
    v-else-if="message.author"
    >
        Author: {{message.author.first_name + " " + message.author.last_name}}
    </h4>
    <div
    v-if="message.images?.length"
    class="images"
    >
        <div
	    v-for="(image, i) in message.images"
        :key="image.id"
        @click="$emit('open_image_viewer', message.images, i)"
        class="image_info"
        >
            <img
	        :src="image.path"
            alt=""
            >
            <div class="text_note" v-if="image.desc">T</div>
        </div>
    </div>

    <div
    v-if="message.text"
    class="text"
    >
        <br>
        {{ message.text }}
    </div>
</template>

<script setup lang="ts">
import { Message } from "@/ts/interfaces/chat"


const group_message_props = defineProps<{
    message: Message
}>()
</script>

<style>
.images {
    margin-top: 10px;
    width: fit-content;
    display: grid;
    grid-template-columns: repeat(2, auto);
    grid-gap: 10px;
}
.linking_message h4 {
    margin: 0px;
}
.image_info {
    width: 100px;
    height: 100px;
    position: relative;
    cursor: pointer;
}
.image_info > img {
    width: 100%;
    height: 100%;
    border-radius: 10px;
}
.image_info > .text_note {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    position: absolute;
    left: 5px;
    top: 5px;
    display: flex;
    font-size: 14px;
    align-items: center;
    justify-content: center;
    padding: 5px;
    background: var(--dark-mode-bg-color);
    color: var(--dark-mode-ok-font-color);
}
</style>
