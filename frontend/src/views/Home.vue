<template>
    <ui-messages-viewer
    @open_image_viewer="open_images"
    @change_current_message="i => current_message_i = i"
    @del_message="del_message"
    :messages="current_group_message.messages"
    v-if="is_current_group_messages_viewer_visible"
    v-model:is_visible="is_current_group_messages_viewer_visible"
    />
    <ui-messages-viewer
    @open_image_viewer="open_images"
    :messages="[{
        text: 'some info...',
        author: {
            first_name: 'f_',
            last_name: 'l_',
        }
    }]"
    v-if="is_linking_message_visible"
    v-model:is_visible="is_linking_message_visible"
    />
    <ui-image-viewer
    :images="images_for_viewer"
    v-if="is_image_viewer_visible"
    v-model:current_image_i="current_image_i_for_viewer"
    v-model:is_visible="is_image_viewer_visible"
    />
    <div class="main_chat_box">
        <div class="contacts">
            <input type="text" placeholder="Find conversation/user">
            <ui-contact
            :first_name="'fname'"
            :last_name="'lname'"
            />
            <ui-contact
            :first_name="'fname2'"
            :last_name="'lname2'"
            />
            <ui-contact
            :first_name="'fname3'"
            :last_name="'lname3'"
            />
        </div>
        <div class="chat">
            <div class="messages">
                <ui-group-message
                alignment="left"
                @open_image_viewer="open_images"
                :group_message="{
                    id: 1,
                    author: {
                        first_name: 'f_',
                        last_name: 'l_',
                        photo: 'http://localhost:8000/images/photo_for_user_45.jpg',
                    },
                    messages: [
                        {
                            id: 1,
                            text: 'SOME OPTIONAL TEXT',
                            images: [
                                {
                                    id: 1,
                                    path: 'http://localhost:8000/images/photo_for_user_51.jpg',
                                    desc: 'desc1'
                                },
                                {
                                    id: 2,
                                    path: 'http://localhost:8000/images/photo_for_user_42.jpg',
                                    desc: 'desc2'
                                },
                                {
                                    id: 3,
                                    path: 'http://localhost:8000/images/photo_for_user_44.jpg',
                                    desc: 'desc3'
                                },
                            ],
                            linking_message: {
                                id: 2,
                                text: 'SOME OPTIONAL TEXT2',
                                images: [
                                    {
                                        id: 1,
                                        path: 'http://localhost:8000/images/photo_for_user_51.jpg',
                                        desc: 'desc1'
                                    }
                                ],
                                author: {
                                    first_name: 'lmaf_',
                                    last_name: 'lmal_',
                                }
                            },
                        },
                        {
                            id: 2,
                            text: 'SOME OPTIONAL TEXT',
                            images: [
                                {
                                    id: 1,
                                    path: 'http://localhost:8000/images/photo_for_user_51.jpg',
                                    desc: 'desc1'
                                },
                                {
                                    id: 2,
                                    path: 'http://localhost:8000/images/photo_for_user_42.jpg',
                                    desc: 'desc2'
                                },
                                {
                                    id: 3,
                                    path: 'http://localhost:8000/images/photo_for_user_44.jpg',
                                    desc: 'desc3'
                                },
                            ],
                        },
                        {
                            id: 3,
                            text: 'SOME OPTIONAL TEXT',
                        }
                    ]
                }"
                />
            </div>
            <div class="send_message_box">
                <div class="messaging_helpers">
                    <div @click="is_current_group_messages_viewer_visible=true">
                        <img src="@/assets/images/all_messages.png" alt="">
                    </div>
                    <div @click="add_message">
                        <img src="@/assets/images/add_message.png" alt="">
                    </div>
                    <div @click="is_linking_message_visible=true">
                        <img src="@/assets/images/linking_message.png" alt="">
                    </div>
                </div>
                <textarea
                    type="text" cols="70" rows="2"
                    v-model="current_group_message.messages[current_message_i].text"
                />
                <ui-ok-button class="submit_group_message">Send group of messages</ui-ok-button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { GroupMessage, MessageImage } from "@/ts/interfaces/chat";
import { reactive, ref } from "vue";


const is_image_viewer_visible = ref<boolean>(false)
const is_linking_message_visible = ref<boolean>(false)
const is_current_group_messages_viewer_visible = ref<boolean>(false)
const images_for_viewer: MessageImage[] = reactive([])
const current_image_i_for_viewer = ref<number>(0)
const current_message_i = ref<number>(0) // current message index for valid input binding
const current_group_message: GroupMessage = reactive({
    author: {
        first_name: "current_fn",
        last_name: "current_ln",
    },
    messages: [
        {
            id: 8,
            text: "(o\\_/o)",
            images: [],
        },
    ]
})


function open_images(images: MessageImage[], current_image_i: number){
    // Configure data for message images viewer and show it
    Object.assign(images_for_viewer, images)
    current_image_i_for_viewer.value = current_image_i
    is_image_viewer_visible.value = true
}
function add_message(){
    current_group_message.messages.push({
        text: "",
        images: [],
    })
    current_message_i.value = current_group_message.messages.length-1
}
function del_message(removable_message_i: number){
    current_message_i.value--
    current_group_message.messages =
        current_group_message.messages.filter((el, i) => removable_message_i != i)
}
</script>

<style scoped src="@/assets/css/home.css">
</style>
