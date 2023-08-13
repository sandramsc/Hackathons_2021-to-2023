import { Footer } from "./Footer"
import { NavBar } from "./NavBar"

export const Container = ({ children }: { children: React.ReactNode }) => {
    return <>
        <ContainerX><NavBar /></ContainerX>
        {children}
        <ContainerX><Footer /></ContainerX>
    </>
}

export const ContainerX = ({ children }: { children: React.ReactNode }) => {
    return <div className="max-w-7xl mx-auto">
        {children}
    </div>
}