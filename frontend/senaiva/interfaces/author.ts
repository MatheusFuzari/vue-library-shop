import { type User } from "./user";

export interface Author{
    id: number;
    photo: string;
    biography: string;
    userFK: User;
}