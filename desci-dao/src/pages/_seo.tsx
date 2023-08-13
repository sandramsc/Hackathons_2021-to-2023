import Head from 'next/head';

export interface MetadataProps {
    siteTitle?: string | undefined,
    title?: string | undefined,
    description?: string | undefined,
    url?: string | undefined,
    image?: string | undefined,
}

const MetaData = ({ siteTitle, title, description, url, image }: MetadataProps) => {
    return (
        <Head>
            <title>{siteTitle}</title>
            <meta property="og:type" content="website" />
            <meta name="description" content={description} />

            <meta name="og:title" property="og:title" content={title} />
            <meta name="og:description" property="og:description" content={description} />
            <meta name="og:site_name" content="Even3" />
            <meta name="og:url" content={url} />
            <meta name="og:image" content={image} />

            <meta name="twitter:title" content={title} />
            <meta name="twitter:description" content={description} />
            <meta name="twitter:card" content="summary_large_image" />
            <meta name="twitter:url" content={url} />
            <meta name="twitter:image" content={image} />
            <meta name="twitter:site" content='@_even3' key="twhandle" />
            <meta name="twitter:creator" content='@MrRaccxxn' key="twhandle" />
        </Head>
    )
}

export default MetaData;

MetaData.defaultProps = {
    siteTitle: 'SoulSci - Public Library',
    title: 'SoulSci - Public Library',
    description: 'Create an identity token to securely identify yourself, protect important documents, and keep them organized and accessible.',
    url: "https://soulsci.vercel.app/",
    image: "https://gateway.lighthouse.storage/ipfs/QmYu4BEUqBHMJfPEBxtS36nVHvvQjutx3Mf5gLFmpceexm",
}