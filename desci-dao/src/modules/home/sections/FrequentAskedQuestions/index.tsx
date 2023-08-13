export const FrequentAskedQuestions = () => {
    return <section className=" dark:text-gray-100 mt-16 text-gray-700">
        <div className="container flex flex-col justify-center p-4 mx-auto md:p-8">
            <p className="p-2 text-sm font-medium tracking-wider text-center uppercase text-gray-700">How it works</p>
            <h2 className="mb-12 text-4xl font-bold leading-none text-center sm:text-5xl text-gray-700">Frequently Asked Questions</h2>
            <div className="grid gap-10 md:gap-8 sm:p-3 grid-cols-2 md:grid-cols-1 lg:px-12 xl:px-32">
                <div>
                    <h3 className="font-semibold text-gray-700">How does Soulsci work?</h3>
                    <p className="mt-1 dark:text-gray-400">Users can propose a PDF document to be added to the Filecoin blockchain. If the community of voters (DAO) believes the document is worth preserving, the proposal will be accepted and the PDF will be uploaded to the Filecoin blockchain for public access.</p>
                </div>
                <div>
                    <h3 className="font-semibold text-gray-700">Why use Soulsci?</h3>
                    <p className="mt-1 dark:text-gray-400">By using Soulsci, you can contribute to a decentralized public library where the community has control over what gets added. This allows for a more democratic and transparent process for preserving important PDF documents, as opposed to relying on centralized entities.</p>
                </div>
                <div>
                    <h3 className="font-semibold text-gray-700">How does SoulBound Token work?</h3>
                    <p className="mt-1 dark:text-gray-400">SoulBound Token is an identity credential that proves a user&apos;s ownership and accountability in the Soulsci system. To participate in the proposal and voting process, a user must hold and activate a SoulBound Token, which verifies their participation in the system. Importantly, SoulBound Tokens cannot be sold and are tied to the individual user&apos;s identity. </p>
                </div>
                <div>
                    <h3 className="font-semibold text-gray-700">What is a SBT identity credential?</h3>
                    <p className="mt-1 dark:text-gray-400">A SoulBound Token identity credential is a requirement for users to participate in the proposal and voting process of Soulsci. It allows for secure and accountable participation in the decision-making process.</p>
                </div>
            </div>
        </div>
    </section>
};