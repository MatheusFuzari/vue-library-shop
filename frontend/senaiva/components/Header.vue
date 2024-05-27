<script setup lang="ts">
import type { User } from '~/interfaces/user';

const { data } = useAuth();

const isAuthor = computed<boolean>(() => {
  if (data.value) {
    const userdata: User = data.value.results[0];
    console.log(userdata);
    if (userdata.groups.includes('Author')) {
      return true
    }
    return false
  }
  return false
});

const isLibrarian = computed<boolean>(() => {
  if (data.value) {
    const userdata: User = data.value.results[0];
    console.log(userdata);
    if (userdata.groups.includes('Librarian')) {
      return true
    }
    return false
  }
  return false
});
</script>


<template>
  <navbar>
    <div class='w-full h-28 bg-[#050424] flex flex-row items-center justify-between'>
      <div>
        <img src="../assets/images/seraiva_logo.png" class="w-[22%] h-[30%] ml-2" />
      </div>
      <div class="flex flex-row gap-16 mr-10 text-white">
        <div v-if="isLibrarian">
          <span>
            <NuxtLink to="/loanmanager"><Button icon="pi pi-bookmark" label="Aba Bibliotecário" /></NuxtLink>
          </span>
        </div>
        <div v-if="isAuthor">
          <span>
            <NuxtLink to="/addbook"><Button icon="pi pi-bookmark" label="Aba Autor" /></NuxtLink>
          </span>
        </div>
        <span>
          <NuxtLink to="/"><Button icon="pi pi-home" label="Home" /></NuxtLink>
        </span>
        <span>
          <NuxtLink to="/checkout"><Button icon="pi pi-shopping-cart" label="Carrinho" /></NuxtLink>
        </span>
        <span>
          <NuxtLink to="/login"><Button icon="pi pi-user" label="Login" /></NuxtLink>
        </span>
      </div>
    </div>
  </navbar>
</template>