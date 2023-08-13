export const ProductDescription = () => {
  return <section className="text-gray-600 body-font">
    <div className="container px-5 py-24 mx-auto">
      <div className="flex flex-wrap sm:-m-4 -mx-4 -mb-10 -mt-4 md:space-y-0 space-y-6">
        <div className="p-4 md:w-1/3 flex">
          <div className="w-12 h-12 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 mb-4 flex-shrink-0">
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-6 h-6" viewBox="0 0 24 24">
              <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
            </svg>
          </div>
          <div className="flex-grow pl-6">
            <h2 className="text-gray-900 text-lg title-font font-medium mb-2">Store your PDF for Max Security</h2>
            <p className="leading-relaxed text-base">Once you create a credential token, you could propose documents you&apos;d like to share and keep. Note that your proposed PDF will get stored on the blockchain once it is approved by the community.</p>
          </div>
        </div>
        <div className="p-4 md:w-1/3 flex">
          <div className="w-12 h-12 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 mb-4 flex-shrink-0">
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-6 h-6" viewBox="0 0 24 24">
              <circle cx="6" cy="6" r="3"></circle>
              <circle cx="6" cy="18" r="3"></circle>
              <path d="M20 4L8.12 15.88M14.47 14.48L20 20M8.12 8.12L12 12"></path>
            </svg>
          </div>
          <div className="flex-grow pl-6">
            <h2 className="text-gray-900 text-lg title-font font-medium mb-2">Vote and Mange DAO Together (Soon)</h2>
            <p className="leading-relaxed text-base">Once you create your credential token, you could vote for the proposal PDFs you believe is worth storing and preserving for the future.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
}