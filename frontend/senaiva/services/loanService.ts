import { BACKEND_URL } from "~/interfaces/app";
import type { Loan, LoanBody } from "~/interfaces/loan";


export const postLoan = (loanPayload: LoanBody): Promise<Loan | null> => {
    return useFetch<Loan>(`${BACKEND_URL}/loan/`,{
        method: 'POST',
        body: loanPayload
    })
    .then(response => {
        return Promise.resolve(response);
    })
    .catch(error => {
        console.error("error when post Loan:", error);
        return Promise.resolve(error);
    })
}