import { type Book } from "~/interfaces/book";

export type Cart = {
  books: Array<Book>;
};

export const cart = defineStore('cartStore', {
  state: (): Cart => ({
    books: []
  }),
  actions: {
    addBookToCart(book: Book) {
      const bookExists = this.isInCart(book);
      if (bookExists == false) {
        if (this.books.length < 3) {
          this.books.push(book);
          return ['success', 'Book added to the cart!'];
        } else {
          return ['error', 'Yout cart exceed the limit of 3 books!'];
        }
      } else {
        console.log('Book already in the cart!');
        return ['error', 'Book already in the cart!'];
      }
    },
    removeBookFromCart(book: Book) {
      const bookIndex = this.getBookById(book);
      this.books.splice(bookIndex, 1);
    },
    emptyCart() {
      this.books = [];
    }
  },
  getters: {
    isInCart: (cart: Cart) => (book: Book): boolean => {
      return cart.books.findIndex(item => item.id === book.id) !== -1;
    },
    getCart: (cart: Cart) => (): Array<Book> => {
      return cart.books;
    },
    getBookById: (cart: Cart) => (book: Book) => {
      return cart.books.findIndex(item => item.id === book.id);
    },
    getCartPrice: (cart: Cart) => (): Number => {
      let fullPrice = 0;
      cart.books.forEach(book => {
        fullPrice += parseFloat(book.price);
      })
      return fullPrice;
    }
  }
})