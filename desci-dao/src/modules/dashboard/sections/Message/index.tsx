export const MessageSection = () => {

    return <div className="ml-60 max-h-24">
        <div className="px-6 py-8">
            <div className="max-w-6xl mx-auto  h-screen ">
                <div className="bg-white rounded-3xl p-8 mb-5 flex gap-8 justify-between h-4/5">
                    <section className="flex flex-col pt-3 w-1/3 bg-gray-50 h-full overflow-y-scroll">
                        <label className="px-3">
                            <input className="rounded-lg p-4 bg-gray-100 transition duration-200 focus:outline-none focus:ring-2 w-full"
                                placeholder="Search..." />
                        </label>

                        <ul className="mt-6">
                            <li className="py-5 border-b px-3 transition hover:bg-gray-100">
                                <a href="#" className="flex justify-between items-center">
                                    <h3 className="text-lg font-semibold">Akhil Gautam</h3>
                                    <p className="text-md text-gray-400">23m ago</p>
                                </a>
                                <div className="text-md italic text-gray-400">You have been invited!</div>
                            </li>
                            <li className="py-5 border-b px-3 bg-gray-400 text-white ">
                                <a href="#" className="flex justify-between items-center">
                                    <h3 className="text-lg font-semibold">Akhil Gautam</h3>
                                    <p className="text-md">23m ago</p>
                                </a>
                                <div className="text-md">You have been invited!</div>
                            </li>
                            <li className="py-5 border-b px-3 transition hover:bg-gray-100">
                                <a href="#" className="flex justify-between items-center">
                                    <h3 className="text-lg font-semibold">Akhil Gautam</h3>
                                    <p className="text-md text-gray-400">23m ago</p>
                                </a>
                                <div className="text-md italic text-gray-400">You have been invited!</div>
                            </li>
                            <li className="py-5 border-b px-3 transition hover:bg-gray-100">
                                <a href="#" className="flex justify-between items-center">
                                    <h3 className="text-lg font-semibold">Akhil Gautam</h3>
                                    <p className="text-md text-gray-400">23m ago</p>
                                </a>
                                <div className="text-md italic text-gray-400">You have been invited!</div>
                            </li>
                        </ul>
                    </section>
                    <section className="px-4 w-4/6 flex flex-col bg-white justify-between rounded-r-3xl overflow-y-scroll">
                        <div className="flex justify-between items-center ">
                            <div className="flex space-x-4 items-center">
                                <div className="h-12 w-12 rounded-full overflow-hidden">
                                    <img alt="image" src="https://bit.ly/2KfKgdy" loading="lazy" className="h-full w-full object-cover" />
                                </div>
                                <div className="flex flex-col">
                                    <h3 className="font-semibold text-lg">Your name</h3>
                                    <p className="text-light text-gray-400">0x3D279A9Da3Fc692495FfE14eF2ddCc25f4c33198</p>
                                </div>
                            </div>
                        </div>
                        <section className="h-full py-4 overflow-y-scroll">
                            <div className="chat chat-start">
                                <div className="chat-image avatar">
                                    <div className="w-10 rounded-full">
                                        <img alt="image" src="https://placeimg.com/192/192/people" />
                                    </div>
                                </div>
                                <div className="chat-header">
                                    <time className="text-xs opacity-50">12:45</time>
                                </div>
                                <div className="chat-bubble flex items-center bg-gray-200 text-slate-600">You were the Chosen One!</div>
                                <div className="chat-footer opacity-50">
                                    Delivered
                                </div>
                            </div>
                            <div className="chat chat-end">
                                <div className="chat-image avatar">
                                    <div className="w-10 rounded-full">
                                        <img alt="image" src="https://placeimg.com/192/192/people" />
                                    </div>
                                </div>
                                <div className="chat-header">
                                    <time className="text-xs opacity-50">12:46</time>
                                </div>
                                <div className="chat-bubble flex items-center bg-gray-300 text-slate-600">I hate you!</div>
                                <div className="chat-footer opacity-50">
                                    Seen at 12:46
                                </div>
                            </div>
                        </section>
                        <section className="mt-6 border rounded-xl bg-gray-50 mb-3">
                            <textarea className="w-full bg-gray-50 p-2 rounded-xl" placeholder="Type your reply here..." rows={3}></textarea>
                            <div className="flex items-center justify-between p-2">
                                <button className="h-6 w-6 text-gray-400">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                            d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
                                    </svg>
                                </button>
                                <button className="bg-purple-600 text-white px-6 py-2 rounded-xl">Reply</button>
                            </div>
                        </section>
                    </section>
                </div>
            </div>
        </div>
    </div>
}