import { type User } from "./user";
import { type BookCategory, type Category } from "./category";
import type { Author } from "./author";

export enum PLATAFORM {
    'EBOOK' = 'EBOOK',
    'FÍSICO' = 'FÍSICO'
}

export enum STATUS {
    'APROVADO' = 'APROVADO',
    'PENDENTE' = 'PENDENTE',
    'CANCELADO' = 'CANCELADO'
}

export interface Book{
    id: number;
    title: string;
    image: string;
    description: string;
    pages: number;
    platform: string;
    edition: string;
    author: Author;
    publish_year: string;
    rating: number;
    price: number;
    status: string;
    qntInStock: number;
    categoryFK: Array<BookCategory>
}