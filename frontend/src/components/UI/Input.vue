<template>
    <input
	v-if="type == 'file'"
	:type="type"
	:placeholder="placeholder"
    @input="e => model = e.target.files[0]"
    accept="image/*"
    class="file_input"
	>
    <input
	v-else
	:type="type"
    :placeholder="placeholder"
    :value="model"
    @input="e => model = type=='number' ? Number(e.target.value) : e.target.value"
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
const model = defineModel()
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
