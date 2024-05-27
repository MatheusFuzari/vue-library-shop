import { BACKEND_URL } from "~/interfaces/app";
import type { Category } from "~/interfaces/category";
import type { Pagination } from "~/interfaces/pagination";

export const getCategories = (): Promise<Pagination<Category> | null> => {
  return useFetch<Pagination<Category>>(`${BACKEND_URL}/category`)
    .then(response => {
      return Promise.resolve(response.data.value);
    })
    .catch(error => {
      console.log("error ", error)
      return Promise.resolve(error)
    })
}