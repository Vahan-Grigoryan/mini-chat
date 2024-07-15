<template>
    <div class="wrapper">
        <div class="centered_box">
            <slot></slot>
        </div>
    </div>
</template>

<script lang="ts">

</script>

<style scoped>
.wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background: var(--dark-mode-bg-color);
    color: var(--dark-mode-ok-font-color);
}
.centered_box {
    text-align: center;
}
</style>
