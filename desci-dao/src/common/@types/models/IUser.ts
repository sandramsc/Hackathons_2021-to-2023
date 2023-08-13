export type IUser = {
    _id: string;
    address: string;
    name: string;
    profession: string;
    email: string;
    papers: string[];
}

export type IUserForm = Omit<IUser, "id" | "papers">;