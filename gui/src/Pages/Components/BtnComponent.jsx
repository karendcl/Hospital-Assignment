import LinkComponent from "./LinkComponent"

export default function BtnComponent({isVisible, day, name, children}){
    return(
        <div className=" flex flex-col items-center justify-center  w-2/12 h-screen ">
            {children}
            {isVisible && <LinkComponent day={day} name={name}/>}
        </div>
    )
}