import { type User } from "./user";
import { type Book } from "./book";

export interface Loan{
    userFK: User;
    bookFK: Book;
    loanDate: string;
    expectedDate: string;
    deliverDate: string|null;
}

export interface LoanBody{
    userFK: string;
    bookFK: string;
}