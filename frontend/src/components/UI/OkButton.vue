<template>
    <button><slot></slot></button>
</template>

<script setup>

</script>

<style scoped>
button {
    border: none;
    background: var(--dark-mode-ok-btn-color);
    padding: 10px 20px;
    border-radius: 5px;
    color: var(--dark-mode-ok-font-color);
    cursor: pointer;
    font-size: 17px;
}
</style>
