import React from "react";

// components

import CardStats from "components/Cards/CardStats.js";

export default function HeaderStats() {
  return (
    <>
      {/* Header */}
      <div className="relative bg-lightBlue-600 md:pt-32 pb-32 pt-12">
        <div className="px-4 md:px-10 mx-auto w-full">
          <div>
            {/* Card stats */}
            <div className="flex flex-wrap">
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
         
              </div>
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">
     
              </div>
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">

              </div>
              <div className="w-full lg:w-6/12 xl:w-3/12 px-4">

              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}