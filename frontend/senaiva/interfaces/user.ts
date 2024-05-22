export interface User{
    id: number;
    first_name: string;
    last_name: string;
    email: string;
    groups: Array<string>;
    user_permissions: Array<string>;
}