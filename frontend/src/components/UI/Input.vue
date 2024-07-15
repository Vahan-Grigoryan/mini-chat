<template>
    <input
	v-if="type!=='file'"
	:type="type"
	:placeholder="placeholder"
	>
    <input
	v-else
	:type="type"
    :placeholder="placeholder"
    accept="image/*"
    class="file_input"
    >
    <span
	v-if="error_message"
	class="error_message"
	>
        {{error_message}}
    </span>
</template>

<script setup lang="ts">
const props = defineProps<{
    type: string
    placeholder?: string
    error_message?: string
}>()
</script>

<style scoped>
input {
    display: block;
    margin-bottom: 15px;
    padding: 7px 15px;
    border:none;
    border-radius: 5px;
    font-size: 17px;
    width:100%;
}
.file_input {
    padding: 0px;
}
input:focus {
    outline: 3px solid var(--dark-mode-ok-btn-color);
}
.error_message {
    display: block;
    margin:-10px 0px 10px 0px;
    color: var(--dark-mode-no-font-color);
    text-align: left;
}
</style>
