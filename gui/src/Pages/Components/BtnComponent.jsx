import LinkComponent from "./LinkComponent"

export default function BtnComponent({isVisible, day, name, children, isInFront}){
    return(
        <div className=" flex flex-col items-center justify-center  w-2/12 h-screen ">
            {isVisible && <LinkComponent day={day} name={name} isInFront={isInFront}>{children}</LinkComponent>}
        </div>
    )
}