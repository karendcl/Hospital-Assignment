import LinkComponent from "./LinkComponent"

export default function BtnComponent({isVisible, day, name, children, isInFront}){
    return(
        <>
            {isVisible && <LinkComponent day={day} name={name} isInFront={isInFront}>{children}</LinkComponent>}
        </>
    )
}