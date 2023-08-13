import { createPaper } from "@/common/services/models/paper"
import _ from "lodash"
import { useContext, useState } from "react"
import { useForm } from "react-hook-form"
import { useAccount } from "wagmi"
import { ProjectSectionContext } from "../../../context/ProjectSectionContext"
import { ProjectSectionContextInterface, ProjectSectionStateType } from "../../../types/context/registerProjectFormContext"
import { IPaperForm } from "../../../types/models/paper"
import { MintPaper } from "./MintPaper"
import { UploadMetadata } from "./UploadMetadata"

export const RegisterPaper = () => {
    const { projectSectionState, setProjectSectionState, setPaper, paper } = useContext(ProjectSectionContext) as ProjectSectionContextInterface
    const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
    const [isUpdating, setIsUpdating] = useState<boolean>(false);
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<IPaperForm>();
    const { address } = useAccount();

    const onSubmit = handleSubmit(async (data: IPaperForm) => {
        setIsSubmitting(true)
        console.log(data)
        switch (projectSectionState) {
            case ProjectSectionStateType.UploadMetadata:
                if (_.isEmpty(data.paperFile) || _.isEmpty(data.thumbnail)) {
                    alert('empty')
                } else {
                    setPaper(data)
                    setProjectSectionState(ProjectSectionStateType.Mint)
                }
                return

            case ProjectSectionStateType.Mint:
                setIsUpdating(true)
                const formData = new FormData();
                formData.append('title', paper?.title || '');
                formData.append('author', paper?.author || '');
                formData.append('description', paper?.description || '');
                formData.append('ownerAddress', address || '');
                formData.append('files', paper?.paperFile[0], paper?.paperFile[0].name);
                formData.append('files', paper?.thumbnail[0], paper?.thumbnail[0].name);

                const response = await createPaper(formData)

                if (response?.status === 200) {
                    setProjectSectionState(ProjectSectionStateType.MyProjects)
                }

                setIsUpdating(false)
                return

            default:
                break;
        }
        setIsSubmitting(false)
        return
    });

    return <>
        {projectSectionState === ProjectSectionStateType.UploadMetadata && < UploadMetadata register={register} errors={errors} onSubmit={onSubmit} isSubmitting={isSubmitting} />}
        {projectSectionState === ProjectSectionStateType.Mint && < MintPaper onSubmit={onSubmit} isUpdating={isUpdating} />}
    </>
}