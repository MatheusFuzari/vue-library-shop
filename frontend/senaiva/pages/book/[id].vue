<script setup lang="ts">
import type { Book } from '~/interfaces/book';
import { getBookById } from '~/services/bookService';

const router = useRoute();
const bookId = router.params.id;
const book: Ref<Book | undefined> = ref();


const getBooks = () => {
  getBookById(bookId as string)
    .then((res) => {
      book.value = res ?? undefined;
      console.log(book);
    })
    .catch((error) => {
      console.log('error ', error)
    })
}

getBooks();
</script>
<template>
  <div class="h-full w-full">
    <div class='bg-slate-300 w-[80%] h-fit m-auto mt-5 p-16 rounded-md'>
      <div class='flex flex-row items-center justify-center gap-0'>
        <div class='flex flex-col items-center justify-center w-[50%]'>
          <div class='w-[30%]'>
            <img :src="book?.image" class='rounded-md' />
          </div>
          <div class='mt-12 w-[80%] m-auto flex flex-row justify-center items-center gap-5'>
            <div class='flex flex-col items-center justify-center'>
              <p>Nome do Autor: <span class='text-lg'>{{ book?.author.userFK.first_name }} {{
                book?.author.userFK.last_name }}</span></p>
              <div class="w-[80%]">
                <img :src="book?.author.photo" />
              </div>
            </div>
            <div class='flex flex-col items-center justify-center'>
              <p>Biografia: </p>
              <p>{{ book?.author.biography }}</p>
            </div>
          </div>
        </div>
        <div class='flex flex-col w-[50%] items-start'>
          <p class='text-3xl font-bold'>{{ book?.title }}</p>
          <p class='text-3xl'>R${{ book?.price }}</p>
          <Rating :model-value="book?.rating" readonly :cancel="false" />
          <p>{{ book?.qntInStock }}</p>
          <div class='flex flex-row gap-5 mt-5'>
            <p>{{ book?.platform }}</p>
            <p>{{ book?.pages }}</p>
            <p>{{ book?.publish_year }}</p>
          </div>
          <div class='w-[50%] mt-5'>
            <p>{{ book?.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>