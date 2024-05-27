<script setup lang="ts">
import { type Ref, ref } from 'vue';
import type { Book } from '~/interfaces/book';
import { getBooks } from '~/services/bookService';

const books: Ref<Array<Book>> = ref([]);
const toast = useToast();

const approvedBooks = (book: Book) => {
    return book.status == "APROVADO";
}

const updateBooks = () => {
    getBooks()
        .then((res) => {
            books.value = res?.results ?? [];
            books.value = books.value.filter(approvedBooks);
            console.log(books.value);
        })
        .catch(e => {
            console.log('error', e);
        })
};

updateBooks();

const show = (res: Array<string>) => {
    toast.add({ severity: res[0] as "success" || "error", summary: res[1], life: 3000 });
};

</script>

<template>
    <main>
        <div class='w-full h-screen'>
            <Toast />
            <div class="flex flex-wrap gap-5 justify-center mt-28">
                <div v-for="book in books">
                    <BookCard :book="book" @cart-response="show($event)" />
                </div>
            </div>
        </div>
    </main>
</template>