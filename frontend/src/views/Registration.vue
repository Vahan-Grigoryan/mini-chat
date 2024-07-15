<template>
    <ui-centered-content>
        <h2>Registration</h2>
        <ui-input
	    type="text"
	    placeholder="*first name"
	    />
        <ui-input
		type="text"
		placeholder="*last name"
		/>
        <ui-input
		type="email"
		placeholder="*email"
		/>
        <ui-input
		type="password"
		placeholder="*password"
		/>
        <ui-input
		type="number"
		placeholder="tel(with '+')"
		/>
        <ui-input
		type="number"
		placeholder="age"
		/>
        <ui-input
		type="file"
		/>
        <ui-ok-button>Sign up</ui-ok-button>
    </ui-centered-content>
</template>

<script setup lang="ts">

</script>

<style scoped src="@/assets/css/registration.css">
</style>
