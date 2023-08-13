import classnames from "classnames";
import _ from "lodash";
import { useState } from "react";
import { UseFormRegister } from "react-hook-form";
import { AiFillCheckCircle } from 'react-icons/ai';
import Image from "next/image";

interface Props {
    className: string,
    register: UseFormRegister<any>,
    inputName: string,
    label: string,
    helperText?: string,
    title?: string,
    square?: boolean,
    memoryImage?: any,
    pdf?: boolean
}

export const DragAndDrop = ({ register, inputName, className, label, helperText = '', title = 'Upload your file', square = false, memoryImage = null, pdf = false }: Props) => {
    const [image, setImage] = useState<string>('');

    const onChangeImage = (event: any) => {
        if (!pdf)
            setImage(URL?.createObjectURL(event.target?.files[0]) || '')
        else {
            setImage(event.target.files[0].name)
        }
    }

    return <div className={classnames(`${className} ${square ? 'w-96 h-96 sm:w-72 sm:h-72' : ''} flex flex-col justify- items-start w-full m-auto`)}>
        <label className="label">
            <span className="label-text">{title}</span>
        </label>
        <label htmlFor={inputName} className={classnames([`${square ? 'w-96 h-96 sm:w-72 sm:h-72' : 'sm:h-48 h-80'}  relative flex flex-col justify-center items-center w-full rounded-lg border-2 border-gray-300 border-dashed cursor-pointer dark:hover:bg-bray-900 hover:bg-gray-100`])}>
            {
                image !== '' || !_.isEmpty(memoryImage) ?
                    pdf ? <div className="flex flex-col justify-center items-center pt-5 pb-6">
                        <p className="mb-2 text-md text-gray-700 font-semibold w-72 text-center" style={{ wordWrap: 'break-word' }}>{image || memoryImage[0]?.name}</p>
                        <AiFillCheckCircle color="green" className="h-8 w-8" />
                    </div> :
                        <Image
                            alt={label}
                            src={image || URL?.createObjectURL(memoryImage[0])}
                            style={{ objectFit: 'contain' }}
                            fill
                        />
                    :
                    <div className="flex flex-col justify-center items-center pt-5 pb-6">
                        <svg aria-hidden="true" className="mb-3 w-10 h-10 text-gray-400" fill="none" stroke="#9FA6B2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
                        <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Click to upload a {label}</span></p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">{helperText}</p>
                    </div>
            }
            <input id={inputName} type="file" className="hidden" {...register(inputName, { onChange: onChangeImage })} accept={`${pdf ? '.pdf' : '.jpg,.png'}`} />
        </label>
    </div>
}