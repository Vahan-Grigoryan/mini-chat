<template>
    <div class="wrapper">
        <slot></slot>
    </div>
</template>

<script lang="ts">

</script>

<style scoped>
.wrapper {
    position: absolute;
    left: 0px;
    top: 0px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100vh;
    background: var(--dark-mode-bg-color);
}
</style>
