import { IPaper, IPaperForm } from "../../types/models/paper";
import Image from 'next/image'
import Link from "next/link";
import _ from "lodash";

export const ProjectBox = ({ paper, disableRedirect = false }: { paper?: any, disableRedirect?: boolean }) => {

    return <Link href={disableRedirect ? '#' : paper?.pdfUrl} target='_blank'>
        <div className="card card-side shadow-xl" style={{ width: '426px', height: '154px' }}>
            <figure className="w-2/6 relative">
                <Image
                    fill
                    style={{ objectFit: 'cover' }}
                    src={!_.isEmpty(paper?.thumbnail) ? URL?.createObjectURL(paper.thumbnail[0]) : paper?.thumbnailUrl ? paper?.thumbnailUrl : ''}
                    alt={paper?.title || ''}
                    className='absolute'
                />
            </figure>
            <div className="flex w-4/6 flex-col justify-start p-4 text-start">
                <h2 className="card-title text-gray-900">{paper?.title}</h2>
                <p className="text-sm text-gray-400">{paper?.author}</p>
                <p className="text-gray-700" style={{ overflowWrap: 'break-word'}}>{paper?.description.substring(0, 100)}</p>
            </div>
        </div>
    </Link>
}