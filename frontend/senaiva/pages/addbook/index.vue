<script setup lang="ts">
import type { Book, BookBody } from '~/interfaces/book';
import type { Category } from '~/interfaces/category';
import { postBooks } from '~/services/bookService';
import { getCategories } from '~/services/categoryService';

definePageMeta({
  middleware: 'auth',
})

const { data } = useAuth();
const toast = useToast();
const book = reactive({
  title: '',
  image: '',
  description: '',
  pages: 0,
  platform: '',
  edition: '',
  author: data.value?.results[0].id,
  publish_year: '',
  rating: 5,
  price: 0,
  qntInStock: 0,
  categoryFK: []
})

const allCategories: Ref<Array<Category>> = ref([]);

let dateModel: Date = new Date();

const categories = () => {
  getCategories()
    .then((res) => {
      allCategories.value = res?.results || [];
    })
    .catch(err => {
      console.log(err)
    })
}

const registerBook = () => {
  book.publish_year = `${dateModel.getFullYear()}-${('0' + (dateModel.getMonth() + 1)).slice(-2)}-${('0' + dateModel.getDate()).slice(-2)}`
  postBooks(book)
    .then((res) => {
      console.log(res)
      toast.add({ severity: "success", summary: "Livros craido com sucesso!!", life: 5000 });
    })
    .catch((error) => {
      console.error(error)
    })
}


categories();
</script>
<template>
  <div class='w-[30%] h-full m-auto bg-slate-300 mt-5 rounded-md p-5'>
    <Toast />
    <div class='flex flex-col justify-center items-center gap-8'>
      <p>Adicionar Livro!</p>
      <FloatLabel>
        <InputText id="title" v-model="book.title" />
        <label for="title">Título</label>
      </FloatLabel>
      <FloatLabel>
        <InputText id="image" v-model="book.image" />
        <label for="image">Imagem src</label>
      </FloatLabel>
      <label for='description'>Descrição</label>
      <Textarea v-model="book.description" id='description' rows="5" cols="30" />
      <FloatLabel>
        <InputNumber id="pages" v-model="book.pages" inputId="integeronly" />
        <label for="pages">N° de Página</label>
      </FloatLabel>
      <label for='platform'>Plataforma</label>
      <SelectButton v-model="book.platform" :options="['EBOOK', 'FÍSICO']" aria-labelledby="basic" id='platform' />
      <FloatLabel>
        <InputText id="edition" v-model="book.edition" />
        <label for="edition">N° da Edição</label>
      </FloatLabel>
      <label>Ano de publicação</label>
      <Calendar v-model="dateModel" view="year" dateFormat="yy-mm-dd" />
      <FloatLabel>
        <InputNumber id="price" v-model="book.price" :minFractionDigits="2" />
        <label for="price">Preço</label>
      </FloatLabel>
      <FloatLabel>
        <InputNumber id="qntInStock" v-model="book.qntInStock" inputId="integeronly" />
        <label for="qntInStock">Quantidade no estoque</label>
      </FloatLabel>
      <label>Categorias</label>
      <Listbox v-model="book.categoryFK" :options="allCategories" multiple optionValue="id" optionLabel="name"
        class="w-[60%]" />
      <Button label='teste' @click='registerBook' class='bg-green-300 w-[80%] h-12 text-white'></Button>
    </div>
  </div>
</template>