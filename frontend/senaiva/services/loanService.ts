import { BACKEND_URL } from "~/interfaces/app";
import type { Loan, LoanBody, LoanUpdate } from "~/interfaces/loan";
import type { Pagination } from "~/interfaces/pagination";


export const getLoans = (pageNumber: number = 0): Promise<Pagination<Loan> | null> => {
    return useFetch<Pagination<Loan>>(`${BACKEND_URL}/loan?page=${pageNumber}`)
        .then(response => {
            return Promise.resolve(response.data.value);
        })
        .catch(error => {
            console.error("error when post Loan:", error);
            return Promise.resolve(null);
        })
}

export const putLoans = (loanPayload: LoanUpdate, id: number): Promise<Loan | null> => {
    return useFetch<Loan>(`${BACKEND_URL}/loan/${id}/`, {
        method: "PUT",
        body: loanPayload
    })
        .then(response => {
            return Promise.resolve(response.data.value);
        })
        .catch(error => {
            console.error("error when post Loan:", error);
            return Promise.resolve(null);
        })
}

export const postLoan = (loanPayload: LoanBody): Promise<Loan | null> => {
    return useFetch<Loan>(`${BACKEND_URL}/loan/`, {
        method: 'POST',
        body: loanPayload
    })
        .then(response => {
            return Promise.resolve(response.data.value);
        })
        .catch(error => {
            console.error("error when post Loan:", error);
            return Promise.resolve(null);
        })
}