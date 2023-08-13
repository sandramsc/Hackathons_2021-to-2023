export interface IPaper {
    _id: string;
    title: string;
    author: string;
    description: string;
    pdfUrl: string;
    thumbnailUrl: string;
    ownerAddress: string;
}

export interface IPaperFilters {
    id?: string;
    title?: string;
    ownerAddress?: string;
}