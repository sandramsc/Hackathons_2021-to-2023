import { ContainerX } from "@/common/layout/Container";
import _ from "lodash";
import { FrequentAskedQuestions } from "./sections/FrequentAskedQuestions";
import { Hero } from "./sections/Hero";
import { ProductDescription } from "./sections/ProductDescription";
import { Team } from "./sections/Team";

export const Home = () => {
    return <ContainerX>
        <Hero />
        <ProductDescription />
        <Team />
        <FrequentAskedQuestions />
    </ContainerX>
}