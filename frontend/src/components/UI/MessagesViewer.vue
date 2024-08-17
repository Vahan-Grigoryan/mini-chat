<template>
    <ui-centered-content
    class="centered_content_wrapper"
    @click="e => is_visible = close_viewer(e, is_visible)"
    >
        <div class="close" @click="e => is_visible = close_viewer(e, is_visible)">&#10006;</div>
        <div
        class="linking_message"
        v-if="messages[0].author"
        >
            <ui-message-viewer
            :message="messages[0]"
            />
        </div>
        <div
        class="sending_messages"
        v-if="!messages[0].author"
        @click.stop
        >
            <div
            class="sending_message"
            v-for="(message, i) in messages"
            :key="message.id"
            >
                <div class="message_manipulators">
                    <ui-ok-button
                    @click="$emit('change_current_message', i)"
                    >
                        Edit this
                    </ui-ok-button>
                    <ui-ok-button
                    v-if="messages.length > 1"
                    @click="$emit('del_message', i)"
                    >
                        Remove this
                    </ui-ok-button>
                </div>
                <br>
                <ui-message-viewer
                :message="message"
                @open_image_viewer="(all_messages, i) => $emit('open_image_viewer', all_messages, i)"
                />
            </div>
        </div>
    </ui-centered-content>
</template>

<script setup lang="ts">
import { Message } from "@/ts/interfaces/chat";
import { close_viewer } from "@/utils/utils";


const messages_props = defineProps<{messages: Message[]}>()

const is_visible = defineModel<boolean>("is_visible") // this component visibility flag
</script>

<style scoped>
.centered_content_wrapper {
    z-index: 3;
    background: rgba(0, 0, 0, .5);
    color: var(--dark-mode-ok-font-color);
}
.sending_messages {
    width: 90%;
    display: flex;
    gap:1%;
    justify-content: center;
}
.sending_message, .linking_message {
    background: var(--dark-mode-bg-color3);
    padding: 10px;
    border-radius: 10px;
}
.sending_message {
    width: 19.5%;
}
.message_manipulators {
    display: flex;
    justify-content: center;
    gap:10px;
}
.close {
    position: absolute;
    color: red;
    right: 0px;
    top: 0px;
    cursor: pointer;
    font-size: 30px;
}
</style>
