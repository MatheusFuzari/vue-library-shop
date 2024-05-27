<script setup lang="ts">
import type { Book } from '~/interfaces/book';

const { addBookToCart, getCart, removeBookFromCart } = cart();

type propType = {
  book: Book
}

const props = defineProps<propType>();
const emit = defineEmits(['cartResponse'])

const handleAddBook = (book: Book) => {
  const response = addBookToCart(book);
  emit('cartResponse', response);
  console.log('My Cart: ', getCart());
}

</script>

<template>
  <div class="w-[80%] h-fit bg-slate-300 m-auto p-2 rounded-lg">
    <div class='flex flex-row justify-between items-center gap-5'>
      <Button icon="pi pi-minus" class='rounded-full bg-red-600 w-8 h-8 text-white'
        @click='removeBookFromCart(props.book)' />
      <div class='flex flex-col justify-center items-center'>
        <p class='text-xl'>{{ props.book.title }}</p>
        <p>- {{ props.book.author.userFK.first_name }} {{ props.book.author.userFK.last_name }}</p>
      </div>
      <p class='text-lg text-green-700'>R${{ props.book.price }}</p>
    </div>
  </div>
</template>