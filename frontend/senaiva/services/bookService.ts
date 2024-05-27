import { BACKEND_URL } from "~/interfaces/app";
import type { Book, BookBody } from "~/interfaces/book";
import type { Pagination } from "~/interfaces/pagination";

export const postBooks = (book: BookBody): Promise<Book | null> => {
    return useFetch<Book>(`${BACKEND_URL}/book/`, {
        method: 'POST',
        body: book
    })
        .then(response => {
            return Promise.resolve(response.data.value);
        })
        .catch(error => {
            return Promise.resolve(null);
        });
}

export const getBooks = (pageNumber: number = 0): Promise<Pagination<Book> | null> => {
    return useFetch<Pagination<Book>>(`${BACKEND_URL}/book?page=${pageNumber}`)
        .then(response => {
            return Promise.resolve(response.data.value);
        })
        .catch(error => {
            return Promise.resolve(null);
        });
}

export const getBookById = (id: string): Promise<Book | null> => {
    return useFetch<Book>(`${BACKEND_URL}/book/${id}`)
        .then(response => {
            return Promise.resolve(response.data.value);
        })
        .catch(error => {
            return Promise.resolve(null);
        });
}