<template>
    <div
    :class="{
        group_message: true,
        right_alignment: alignment == 'right',
        left_alignment: alignment == 'left',
    }">
        <ui-user-thumbnail
        v-if="alignment == 'left'"
        :first_name="group_message.author.first_name"
        :last_name="group_message.author.last_name"
        :photo="group_message.author.photo"
        />
        <div
        :class="{
            info_box: true,
            right_alignment: alignment == 'right',
        }"
        >
            <div
            v-for="message in group_message.messages"
            :key="message.id"
            class="message"
            >
                <ui-message-viewer
                :message="message"
                @open_image_viewer="(all_messages, i) => $emit('open_image_viewer', all_messages, i)"
                />
            </div>
        </div>
        <ui-user-thumbnail
        v-if="alignment == 'right'"
        :first_name="group_message.author.first_name"
        :last_name="group_message.author.last_name"
        :photo="group_message.author.photo"
        />
    </div>
</template>

<script setup lang="ts">
import { GroupMessage } from "@/ts/interfaces/chat";


const group_message_props = defineProps<{
    group_message: GroupMessage
    alignment: "left" | "right"
}>()


</script>

<style scoped>
.group_message {
    background: transparent;
    display: flex;
    max-width: 70%;
}
.left_alignment {
    float: left;
    margin-left: 10px;
}
.right_alignment {
    float: right;
    margin-right: 10px;
}
.info_box {
    padding: 15px;
    border-radius: 10px;
    background: var(--dark-mode-bg-color3);
    color: var(--dark-mode-ok-font-color);
    max-width: calc(100% - 60px);
}
.message {
    border-bottom: 2px solid red;
    margin-bottom: 10px;
}
.message:last-child {
    border:none;
}

</style>
