import { type User } from "./user";
import { type Book } from "./book";

export interface Loan {
    id: number;
    userFK: User;
    bookFK: Array<Book>;
    loanDate: string;
    expectedDate: string;
    deliverDate: string | null;
}

export interface LoanBody {
    userFK: string;
    bookFK: Array<string>;
}

export interface LoanUpdate {
    userFK: number;
    bookFK: Array<string>;
    loanDate: string;
    expectedDate: string;
    deliverDate: string;
}
