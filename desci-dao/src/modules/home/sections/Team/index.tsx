import Image from "next/image";
import Link from "next/link";
import { BsGithub, BsTwitter, BsLinkedin } from 'react-icons/bs';

interface ITeamMember {
    name: string;
    role: string;
    socialGitHub: string;
    socialTwitter?: string;
    socialLinkedin?: string;
}

const teamData: ITeamMember[] = [
    {
        name: 'Yuichi Okuhama',
        role: 'Project Management',
        socialGitHub: 'https://github.com/yuichi-9621',
        socialTwitter: 'https://twitter.com/0xYuichi',
        socialLinkedin: 'https://www.linkedin.com/in/yuichiokuhama/'
    },
    {
        name: 'Joseph Mello',
        role: 'Solidity Engineer',
        socialGitHub: 'https://github.com/MelloJ650',
        socialTwitter: 'https://twitter.com/JMellowDev',
        socialLinkedin: 'https://www.linkedin.com/in/josephmellocs/'
    }
    ,
    {
        name: 'Aryton Paredes',
        role: 'Frontend Engineer',
        socialGitHub: 'https://github.com/MrRaccxxn',
        socialTwitter: 'https://twitter.com/MrRaccxxn',
        socialLinkedin: 'https://www.linkedin.com/in/ayrtonparedes/'
    }, {
        name: 'Sandra Ashipala',
        role: 'Frontend Engineer',
        socialGitHub: 'https://github.com/sandramsc',
        socialLinkedin: 'https://linkedin.com/in/sandraashipala'
    },
    {
        name: 'Adarsh Chandran',
        role: 'Solidity Engineer',
        socialGitHub: 'https://github.com/adarshsc2000',
        socialLinkedin: 'https://www.linkedin.com/in/adarshsc2000/',
    }
];

export const Team = () => {
    return <div id="team" className="section relative pt-20 pb-8 md:pt-16 bg-transparent">
        <div className="container xl:max-w-6xl mx-auto px-4">
            <header className="text-center mx-auto mb-12">
                <h2 className="text-2xl leading-normal mb-2 font-bold text-gray-800 ">
                    Our Team
                </h2>
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 100 60" style={{ margin: '0 auto', height: ' 35px', }}>
                    <circle cx="50.1" cy="30.4" r="5" className="stroke-primary" style={{ fill: 'transparent', strokeWidth: '2', strokeMiterlimit: '10' }}></circle>
                    <line x1="55.1" y1="30.4" x2="100" y2="30.4" className="stroke-primary" style={{ strokeWidth: '2', strokeMiterlimit: '10' }}></line>
                    <line x1="45.1" y1="30.4" x2="0" y2="30.4" className="stroke-primary" style={{ strokeWidth: '2', strokeMiterlimit: '10' }}></line>
                </svg>
            </header>

            <div className="flex flex-wrap gap-12 justify-center items-center">
                {
                    teamData.map((teamMember: ITeamMember, index: number) => {
                        return <div key={teamMember.name} className="max-w-sm w-44">
                            <div className="relative mb-12 max-w-sm min-w-44 min-w-fit h-54">
                                <div className="relative  px-6">
                                    <Image
                                        alt={`${teamMember.name} illustration`}
                                        src={`/assets/illustrations/member-${index + 1}.png`}
                                        className="max-w-full h-auto mx-auto"
                                        width={140}
                                        height={140}
                                    />
                                </div>
                                <div className="pt-6 text-center">
                                    <p className="text-lg leading-normal font-bold mb-1">{teamMember.name}</p>
                                    <p className="text-gray-500 leading-relaxed font-light break-all">{teamMember.role}</p>
                                </div>
                                <div className="flex flex-row justify-center items-center gap-2 py-2">
                                    {teamMember.socialLinkedin && <Link href={teamMember.socialLinkedin} target='_blank'><BsLinkedin className="text-gray-600 hover:text-gray-400" /></Link>}
                                    <Link href={teamMember.socialGitHub} target='_blank'><BsGithub className="text-gray-600 hover:text-gray-400" /></Link>
                                    {teamMember.socialTwitter && <Link href={teamMember.socialTwitter} target='_blank'><BsTwitter className="text-gray-600 hover:text-gray-400" /></Link>}
                                </div>
                            </div>
                        </div>
                    })
                }
            </div>
        </div>
    </div>
}