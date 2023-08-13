import { IUser, IUserForm } from "@/common/@types/models/IUser";
import axiosClient from "../axiosClient";

export async function createUser({ data }: { data: IUserForm }) {
    axiosClient.defaults.headers.post['Content-Type'] = 'application/json';
    return axiosClient.post(`/user`, data)
        .then(response => response)
        .catch(error => console.log(error));
}

export async function getUser({ userAddress }: { userAddress: string }) {
    axiosClient.defaults.headers.post['Content-Type'] = 'application/json';
    return axiosClient.get<IUser>(`/user/${userAddress}`)
        .then(response => response)
        .catch(error => console.log(error));
}