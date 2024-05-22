import { BACKEND_URL } from "~/interfaces/app";
import type { Book } from "~/interfaces/book";
import type { Pagination } from "~/interfaces/pagination";

export const getBooks = (pageNumber: number = 0): Promise<Pagination<Book>|null> => {
    return useFetch<Pagination<Book>>(`${BACKEND_URL}/book?page=${pageNumber}`)
    .then(response => {
        return Promise.resolve(response.data.value);
    })
    .catch(error => {
        return Promise.resolve(null);
    });
}