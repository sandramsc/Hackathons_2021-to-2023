import { Loader } from "@/common/components/Loader";
import { Container, ContainerX } from "@/common/layout/Container";
import { getPapers } from "@/common/services/models/paper";
import { ProjectBox } from "@/modules/dashboard/components/ProjectBox";
import { IPaper } from "@/modules/dashboard/types/models/paper";
import { ErrorMessage } from "@hookform/error-message";
import _, { debounce } from "lodash";
import { useCallback, useEffect, useState } from "react";
import { useForm } from "react-hook-form";

interface IPaperSearcher {
    title: string;
}

export default function PaperSearchPage() {
    const [inputText, setInputText] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [papers, setPapers] = useState<IPaper[] | any>([]);

    useEffect(() => {
        const fetchPapers = async () => {
            const response = await getPapers({ title: inputText }, 10, true);
            if (response?.data) {
                setPapers(response?.data || [])
            }
        }

        fetchPapers();
    }, [inputText]);

    const {
        formState: { errors },
    } = useForm<IPaperSearcher>();

    const reFetchEvents = async (filter: any) => {
        setInputText(filter)
    }

    const handler = useCallback(debounce((reFetchEvents), 300), []);

    const handleOnSubmit = async (event: any) => {
        handler(event.target.value);
    };

    return (
        <Container>
            <div className="flex flex-col py-8 justify-start items-center w-full h-screen ">
                <div className="mb-3 w-3/6">
                    <div className="input-group relative flex w-full mb-4 gap-2">
                        <input
                            id='title'
                            type="text"
                            name="title"
                            defaultValue={''}
                            className="bg-transparent form-control relative flex-auto min-w-0 block w-full px-3 py-1.5 text-base font-normal text-gray-600 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-800  focus:border-blue-600 focus:outline-none"
                            placeholder="Paper title..."
                            aria-label="Search"
                            aria-describedby="button-addon2"
                            onChange={handleOnSubmit}
                        />
                    </div>

                    <ErrorMessage
                        errors={errors}
                        name={'title' as any}
                        render={({ message }: { message: string }) => (
                            <p className="mt-1 text-sm text-left block text-red-500">
                                {message}
                            </p>
                        )}
                    />
                </div>
                {
                    _.isEmpty(papers) ? <></>
                        : <ContainerX>
                            <div className="flex flex-wrap gap-16 justify-center items-center">
                                {
                                    papers.map((paper: IPaper, index: number) => {
                                        return <div className="w-fit" key={index}>
                                            <ProjectBox paper={paper} />
                                        </div>
                                    })
                                }
                            </div>
                        </ContainerX>
                }
            </div>
        </Container>
    );
}