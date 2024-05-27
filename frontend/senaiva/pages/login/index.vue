<script setup lang="ts">
import { reactive } from 'vue';


definePageMeta({
    layout: 'login',
})

const { signIn } = useAuth();

const credentials = reactive({
    email: '',
    password: ''
})

const handleLogin = () => {
    signIn(credentials, { redirect: false })
        .then(() => {
            console.log("logged with succes")
            navigateTo('/checkout');
        })
        .catch((error) => {
            console.error('error in login service ', error);
            credentials.email = "";
            credentials.password = "";
        })
}

</script>
<template>
    <section>
        <div class="w-screen h-screen bg-[#050424] flex flex-col justify-center items-center">
            <div class="w-1/4 h-1/2 bg-white flex flex-col items-center rounded-md shadow-md">
                <div class="mt-10">
                    <h2 class="text-3xl p-5 font-semibold text-[#E84B00]">Login</h2>
                </div>
                <div class="flex flex-row items-center justify-center w-full h-fit mt-10 gap-5">
                    <label class="text-lg">E-mail: </label>
                    <input v-model="credentials.email" type="text"
                        class="h-8 min-w-[calc(100%-15rem)] border-b-2 border-[#E84B00] outline-none focus:bg-slate-100" />
                </div>
                <div class="flex flex-row items-center justify-center w-full h-fit mt-16 gap-5">
                    <label class="text-lg">Senha: </label>
                    <input v-model="credentials.password" type="password"
                        class="h-8 min-w-[calc(100%-15rem)] border-b-2 border-[#E84B00] outline-none focus:bg-slate-100" />
                </div>
                <div class="h-10 w-3/6 mt-28">
                    <button @click="handleLogin"
                        class="bg-[#E84B00] rounded-sm h-full w-full text-white font-medium text-lg">Logar</button>
                </div>
            </div>
        </div>
    </section>
</template>