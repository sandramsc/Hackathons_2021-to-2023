import { Container, ContainerX } from "@/common/layout/Container";
import { Footer } from "@/common/layout/Footer";
import { NavBar } from "@/common/layout/NavBar";
import ClientRehydration from "@/common/utils/ClientRehydration";
import { Home } from "@/modules/home";

export default function HomePage() {
  return (
    <ClientRehydration>
        <ContainerX><NavBar showNavigation={true} /></ContainerX>
        <Home />
        <ContainerX><Footer /></ContainerX>
    </ClientRehydration>
  )
}