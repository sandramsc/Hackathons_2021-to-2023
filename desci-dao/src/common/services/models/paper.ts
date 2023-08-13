import { IPaper, IPaperFilters } from "@/common/@types/models/IPaper";
import axiosClient from "../axiosClient";

export async function createPaper(data: FormData) {
    axiosClient.defaults.headers.post['Content-Type'] = 'multipart/form-data';
    return axiosClient.post(`/paper`, data)
        .then(response => response)
        .catch(error => console.log(error));
}

export async function getPapers(filter: IPaperFilters, limit: number | null, useRegex: boolean) {
    axiosClient.defaults.headers.get['Content-Type'] = 'application/json';
    return axiosClient.get<IPaper[]>(`/paper`, {
        params: { filter, limit, useRegex }
    })
        .then(response => response)
        .catch(error => console.log(error));
}