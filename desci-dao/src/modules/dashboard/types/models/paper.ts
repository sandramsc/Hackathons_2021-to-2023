export interface IPaper {
    _id: string;
    title: string;
    author: string;
    description: string;
    pdfUrl: any;
    thumbnailUrl: any;
    uploadDate: Date;
}

// export type IPaperForm = Omit<IPaper, "id" | "uploadDate">;

export type IPaperForm = {
    title: string;
    author: string;
    description: string;
    paperFile: any;
    thumbnail: any;
}
