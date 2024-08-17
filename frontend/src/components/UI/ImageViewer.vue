<template>
    <div class="image_slider_box">
        <div class="close" @click="e => is_visible = close_viewer(e, is_visible)">&#10006;</div>
        <div class="image_slider" @click="e => is_visible = close_viewer(e, is_visible)">
            <div class="img_with_desc">
                <img :src="images[current_image_i].path" alt="">
                <p v-if="images[current_image_i].desc">{{ images[current_image_i].desc }}</p>
            </div>
            <button class="prev" @click="change_img('prev')">&lt;</button>
            <button class="next" @click="change_img('next')">&gt;</button>
        </div>
        <div class="thumbs">
            <img
            v-for="(img, i) in images"
            :key="img.id"
            :src="img.path"
            @click="change_img(i)"
            alt=""
            >
        </div>
    </div>
</template>

<script setup lang="ts">
import { MessageImage } from "@/ts/interfaces/chat"
import { close_viewer } from "@/utils/utils"
import { onMounted } from "vue"


const image_viewer_props = defineProps<{
    images: MessageImage[]
}>()
const current_image_i = defineModel<number>("current_image_i")
const is_visible = defineModel<boolean>("is_visible") // this component visibility flag


function change_img(to?: "next" | "prev" | number){
    // Change image in viewer to next/previous/pointed image index
    if(current_image_i.value == undefined) return

    let future_index = current_image_i.value
    if(to === "next"){
        future_index++
    }
    else if(to === "prev"){
        future_index--
    }
    else if(typeof to === "number"){
        future_index = to
    }
    current_image_i.value =
        future_index <= image_viewer_props.images.length-1 && future_index >= 0?
        future_index: current_image_i.value
}

onMounted(()=>{
    document.body.addEventListener("keyup", e => {
        if(e.key === "ArrowRight"){
            change_img("next")
        }
        else if(e.key === "ArrowLeft"){
            change_img("prev")
        }
    })
})
</script>

<style scoped>
.image_slider_box {
    z-index: 5;
    position: absolute;
    left: 0px;
    top: 0px;
    width: 100%;
    height: 100vh;
    background: #00000099;
}
.image_slider {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 80%;
    text-align: center;
    color: var(--dark-mode-ok-font-color);
}
.image_slider .prev, .image_slider .next {
    position: absolute;
    top:50%;
    transform: translateZ(-50%);
    background: none;
    cursor: pointer;
    border: none;
    color: var(--dark-mode-ok-font-color);
    font-size: 30px;
}
.image_slider .prev {
    left: 0px;
}
.image_slider .next {
    right: 0px;
}
.img_with_desc {
    position: relative;
    height: 100%;
}
.img_with_desc p {
    position: absolute;
    bottom: 0px;
    width: 100%;
    margin: 0px;
    padding: 15px;
    background: linear-gradient(0deg, #00000099, transparent);
    display: none;
}
.img_with_desc *:hover ~ p, .img_with_desc p:hover{
    display: block;
}
.img_with_desc img {
    object-fit: cover;
    max-height: 100%;
    max-width: 100%;
}
.thumbs {
    width: 100%;
    height: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0px 10px
}
.thumbs img {
    width: 100px;
    height: 100px;
    border-radius: 7px;
    cursor: pointer;
}
.close {
    position: absolute;
    color: red;
    right: 0px;
    cursor: pointer;
    font-size: 30px;
    z-index: 2;
}
</style>
