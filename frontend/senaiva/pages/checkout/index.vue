<script setup lang="ts">
import type { Book } from '~/interfaces/book';
import { postLoan } from '~/services/loanService';

const { getCart, getCartPrice, emptyCart } = cart();
const { data } = useAuth();

definePageMeta({
  middleware: "auth",
});

const userId = data.value?.results[0].id;
const fullPrice = computed(() => getCartPrice().toPrecision(5));
const mycart = computed(() => getCart());
const toast = useToast();

const handleLoan = () => {
  console.log(mycart.value);
  let cartIds: Array<string> = [];
  mycart.value.forEach((item) => {
    cartIds.push(item.id.toString())
  })
  postLoan({ userFK: userId, bookFK: cartIds })
    .then((result) => {
      toast.add({ severity: "success", summary: "Livros comprados com sucesso!!", life: 3000 });
      setTimeout(() => {
        emptyCart();
        navigateTo('/');
      }, 5000)
    })
    .catch((e) => {
      console.error(e)
      toast.add({ severity: "error", summary: "Ocorreu um erro ao comprar os livros!", life: 3000 });
    })
}

</script>
<template>
  <div class='w-[40%] h-fit bg-slate-200 rounded-md m-auto mt-5 p-10'>
    <Toast />
    <div v-for="book in mycart">
      <BookCartItem :book="book" class="mt-5" />
    </div>
    <div class='border border-t-slate-300 w-[100%] mt-5'>
      <div class='flex flex-row justify-between mt-5'>
        <Button label='Esvaziar carrinho' class='bg-red-500 p-3 px-5' @click='emptyCart' />
        <p class='text-black text-xl'>Total: R${{ fullPrice }}</p>
        <Button label='Comprar' class='bg-green-500 p-3 px-5' @click="handleLoan" />
      </div>
    </div>
  </div>
</template>