<script setup lang="ts">
import type { Book } from '~/interfaces/book';
import type { Loan } from '~/interfaces/loan';
import { getBookById } from '~/services/bookService';
import { putLoans } from '~/services/loanService';

type propType = {
  loan: Loan
}

const props = defineProps<propType>();
const today = new Date();
const myBooks: Ref<Array<string>> = ref([]);
for (let i = 0; i < props.loan.bookFK.length; i++) {
  myBooks.value.push(props.loan.bookFK[i] as any);
}
console.log(myBooks);
const newBody = reactive({
  'userFK': props.loan.userFK.id,
  'bookFK': myBooks,
  'loanDate': props.loan.loanDate,
  'expectedDate': props.loan.expectedDate,
  'deliverDate': `${today.getFullYear()}-${('0' + (today.getMonth() + 1)).slice(-2)}-${('0' + today.getDate()).slice(-2)}`
})

const deliverLoan = () => {
  putLoans(newBody, props.loan.id)
    .then((res) => {
      console.log('Atualizado o status com sucesso!', res);
    })
    .catch((error) => {
      console.error('error ', error)
    })
}

</script>

<template>
  <div class="w-[80%] h-fit bg-slate-300 m-auto p-2 rounded-lg mb-5">
    <div class='flex flex-row justify-between items-center gap-5'>
      <div class='flex flex-col justify-center items-center'>
        <p class='text-xl'>{{ props.loan.userFK.first_name }} {{ props.loan.userFK.last_name }}</p>
        <p v-for="book in props.loan.bookFK">{{ book }}</p>
      </div>
      <Button label='Devolver!' @click='deliverLoan'></Button>
    </div>
  </div>
</template>