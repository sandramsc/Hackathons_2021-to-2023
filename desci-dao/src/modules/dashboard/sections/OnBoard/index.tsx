import { ContainerX } from '@/common/layout/Container';
import { NavBar } from '@/common/layout/NavBar';
import { useState } from 'react';
import { IntroMessage } from './IntroMessage';
import { RegisterSoulForm } from './RegisterSoulForm';

export const OnBoard = () => {
    const [showMessage, setShowMessage] = useState<boolean>(true)

    return <>
        <ContainerX>
            <NavBar />
        </ContainerX>
        <div className="w-full h-screen flex flex-col justify-center items-center">
            <div className="max-w-6xl w-full m-auto h-full flex justify-center items-center">
                {
                    showMessage ?
                        <IntroMessage changePage={() => setShowMessage(false)} /> :
                        <RegisterSoulForm />
                }
            </div>
        </div>
    </>
}