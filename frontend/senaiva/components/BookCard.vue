<script setup lang="ts">
import type { Book } from '~/interfaces/book';

const { addBookToCart, getCart } = cart();

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
    <div class="w-96 h-72 rounded-sm m-2 p-3 border border-gray-300 flex flex-row items-center">
        <NuxtLink :to="`/book/${props.book.id}`">
            <div class="w-[100%]">
                <img :src="props.book.image" :alt="props.book.title" class="w-[100%] h-64 rounded-md" />
            </div>
        </NuxtLink>
        <div class="w-[45%] flex flex-col justify-center items-center">
            <p class="ml-3 mb-3 font-semibold text-xl">
                {{ props.book.title }}
            </p>
            <span class="font-medium text-lg">R$ {{ props.book.price }}</span>
            <div class="flex flex-col gap-2 w-full mt-20 ml-5 justify-end">
                <Button icon="pi pi-heart" severity="secondary" outlined class="p-1 border border-[#EB1B5D] w-[90%]" />
                <Button icon="pi pi-shopping-cart" class="p-1 bg-[#EB1B5D] w-[90%]"
                    @click="handleAddBook(props.book)" />
            </div>
        </div>
    </div>
</template>