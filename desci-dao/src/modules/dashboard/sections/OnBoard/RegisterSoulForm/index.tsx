import { useContext, useState } from "react";
import { useForm } from "react-hook-form";
import { FormInput } from "../../../../../common/components/form/FormInput";
import { DashboardContext } from "../../../context/DashboardContext";
import { DashboardContextInterface } from "../../../types/context/dashboardContext";
import networkMapping from 'constants/networkMapping.json';
import EditorAbi from 'constants/EditorAbi.json';
import { useAccount, useContractWrite, usePrepareContractWrite, useWaitForTransaction } from "wagmi";
import { Loader } from "@/common/components/Loader";
import { IUserForm } from "@/common/@types/models/IUser";
import { createUser } from "@/common/services/models/user";

export const RegisterSoulForm = () => {
    const { setRequireOnboarding } = useContext(DashboardContext) as DashboardContextInterface;
    const { address } = useAccount();
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<IUserForm>();

    const handleRegisterSoul = handleSubmit(async (data: IUserForm) => {
        if (address) {
            setIsLoading(true)
            const user: IUserForm = { ...data, address }
            const response = await createUser({ data: user })

            if (response?.data?._id) {
                setRequireOnboarding(false)
            }

            setIsLoading(false)
        }
    })

    return <div className="w-full m-auto flex justify-center items-center">
        <div className="bg-white rounded-3xl p-8 mb-5 h-4/5 flex flex-col gap-12 items-center">
            <h2 className="text-gray-700 font-bold text-2xl">Please enter your information</h2>
            <p className="text-gray-500 text-center px-32">The information you provide in the form will be used to create a unique, soul-bound token. This token will securely store and hold the data you have provided, ensuring its integrity and accessibility.</p>
            <div className="flex flex-col justify-between w-full h-full items-center gap-16">
                <div className="w-full px-12 ">
                    <FormInput<IUserForm>
                        id="name"
                        type="text"
                        name="name"
                        label="Full Name *"
                        placeholder="e.x. Vitalik Buterin"
                        className="mb-2 w-full text-xl text-gray-700"
                        register={register}
                        rules={{ required: 'You must enter your full name.' }}
                        errors={errors}
                    />

                    <FormInput<IUserForm>
                        id="profession"
                        type="text"
                        name="profession"
                        label="Professional Title *"
                        placeholder="e.x. Doctor in Physics"
                        className="mb-2 w-full text-xl text-gray-700"
                        register={register}
                        rules={{ required: 'You must enter your profession title.' }}
                        errors={errors}
                    />

                    <FormInput<IUserForm>
                        id="email"
                        type="email"
                        name="email"
                        label="Email *"
                        placeholder="youremail@example.com"
                        className="mb-2 w-full text-xl text-gray-700"
                        register={register}
                        rules={{ required: 'You must enter your profession title.', pattern: { value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i, message: "Invalid email address" } }}
                        errors={errors}
                    />
                </div>
                <button onClick={handleRegisterSoul} disabled={isLoading} className='btn bg-transparent hover:bg-gray-200 text-gray-800 w-fit' style={{ cursor: `url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='40' height='48' viewport='0 0 100 100' style='fill:black;font-size:24px;'><text y='50%'>🥳</text></svg>")  16 0,  auto` }}>
                    {
                        isLoading ? <Loader /> :
                            <>Mint my soul token!</>
                    }
                </button>
            </div>
        </div>
    </div>
}