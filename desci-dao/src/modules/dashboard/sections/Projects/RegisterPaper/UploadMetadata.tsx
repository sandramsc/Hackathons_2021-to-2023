
import { DragAndDrop } from "@/common/components/form/DragNDrop"
import { FormInput } from "@/common/components/form/FormInput"
import { ProjectSectionContext } from "@/modules/dashboard/context/ProjectSectionContext"
import { ProjectSectionContextInterface, ProjectSectionStateType } from "@/modules/dashboard/types/context/registerProjectFormContext"
import { IPaperForm } from "@/modules/dashboard/types/models/paper"
import { ErrorMessage } from "@hookform/error-message"
import { useContext } from "react"
import { FieldErrorsImpl, UseFormRegister } from "react-hook-form"

export const UploadMetadata = ({ register, errors, onSubmit, isSubmitting }: { register: UseFormRegister<IPaperForm>, errors: Partial<FieldErrorsImpl<IPaperForm>>, onSubmit: () => void, isSubmitting: boolean }) => {
    const { paper, setProjectSectionState } = useContext(ProjectSectionContext) as ProjectSectionContextInterface

    const updatePaperData = () => {
        onSubmit()
    }

    return <div className="ml-60 max-h-screen overflow-auto">
        <div className="px-6 py-8">
            <div className="max-w-6xl mx-auto">
                <div className="bg-white rounded-3xl p-8 mb-5">
                    <div className="flex flex-row items-center justify-between">
                        <div className="text-sm breadcrumbs">
                            <ul>
                                <li><a onClick={() => setProjectSectionState(ProjectSectionStateType.MyProjects)}>My Projects</a></li>
                                <li>Add Paper</li>
                            </ul>
                        </div>
                    </div>
                    <h1 className="text-black font-bold text-2xl py-3">ADD Research Paper</h1>

                    <ul className="w-full steps steps-horizontal lg:steps-horizontal self-center py-3">
                        <li className="step step-secondary">Upload Metadata</li>
                        <li className="step">Mint</li>
                    </ul>
                    <div>
                        <div>
                            <FormInput<IPaperForm>
                                id="title"
                                type="text"
                                name="title"
                                label="Title *"
                                placeholder="e.x. How I created Bitcoin"
                                className="mb-2 w-full text-xl"
                                register={register}
                                rules={{ required: 'You must enter a title.' }}
                                errors={errors}
                            />
                        </div>
                        <div>
                            <FormInput<IPaperForm>
                                id="author"
                                type="text"
                                name="author"
                                label="Author Name *"
                                placeholder="e.x. Vitalik Buterin"
                                className="mb-2 w-full text-xl"
                                register={register}
                                rules={{ required: 'You must enter an Author name.' }}
                                errors={errors}
                            />
                        </div>

                        <div className="form-control w-full">
                            <label className="label">
                                <span className="label-text">Paper description *</span>
                            </label>
                            <textarea
                                id="description"
                                placeholder="Description"
                                className="textarea card-bordered bg-transparent border-gray-200"
                                rows={3}
                                {...(register && register('description', { required: 'You must enter a description.', pattern: { value: /^.{50,}$/, message: "Description must have at least 50 characters"} }))}
                            />
                            <ErrorMessage
                                errors={errors}
                                name={'description' as any}
                                render={({ message }: { message: string }) => (
                                    <p className="mt-1 text-sm text-left block text-red-500">
                                        {message}
                                    </p>
                                )}
                            />

                        </div>

                        <div className="flex flex-row gap-5 w-full justify-start">
                            <DragAndDrop title={'Add your PDF *'} pdf={true} helperText={'PDF, Max. upload size : 100Mb'} memoryImage={paper?.paperFile} register={register} inputName={'paperFile'} className={"w-96 h-72 m-0"} label={'PDF'} />
                            <DragAndDrop title={'Upload thumbnail *'} helperText={'JPG or PNG, Max. upload size : 5Mb'} memoryImage={paper?.thumbnail} register={register} inputName={'thumbnail'} className={"w-96 h-72 m-0"} label={'thumbnail'} />
                        </div>

                        <div className="flex flex-row w-full justify-end pt-5">
                            <button className="btn btn-secondary bg-secondary" onClick={updatePaperData}>Upload Metadata</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div >
}