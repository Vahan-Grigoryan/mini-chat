<template>
    <div
    class="linking_message"
    >
        <h5>
            {{message.author.first_name}}
            {{message.author.last_name}}
        </h5>
        <p v-if="message.images?.length">
            {{message.images?.length ? message.images.length+" images" : ""}}
        </p>
        <p>
            {{message.text || ""}}
        </p>
    </div>
</template>

<script setup lang="ts">
import { Message } from "@/ts/interfaces/chat";

const linking_message_props = defineProps<{
    message: Omit<Message, "linking_message">
}>()
</script>

<style scoped>
.linking_message {
    background: var(--dark-mode-bg-color4);
    border-radius: 10px 10px 0px 0px;
    cursor: pointer;
}
.linking_message > h5 {
    margin: 0px;
    padding: 5px 10px;
    background: var(--dark-mode-bg-color5);
    border-radius: 10px 10px 0px 0px;
}
.linking_message p {
    margin: 0px;
    padding: 5px;
}
.linking_message h5+p {
    font-weight: bold;
}

</style>
