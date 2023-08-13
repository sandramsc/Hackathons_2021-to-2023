import Image from "next/image"

export const IntroMessage = ({ changePage }: { changePage: () => void }) => {
    return <div className="bg-white rounded-3xl p-8 mb-5 flex flex-col gap-16 justify-between items-center">
        <div className='flex flex-col gap-8 items-center'>
            <h2 className='text-3xl font-semibold text-gray-700'>Welcome to SoulSci!</h2>
            <Image
                alt='On boarding illustration'
                src={'/assets/illustrations/onboarding.png'}
                width={500}
                height={500}
            />
            <p className='text-gray-500 px-32 text-center'>Our platform provides secure storage and management of research papers in the decentralized web. With robust security features, your work is kept safe and organized. Join the Web3 community and simplify your research process with our Paper Storage application.</p>
        </div>
        <button className='btn bg-transparent hover:bg-gray-200 text-gray-800 w-fit' onClick={changePage}>lets go!</button>
    </div>
}