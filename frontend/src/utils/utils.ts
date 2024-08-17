/*
There are functions that decrease code repeatition
*/


function close_viewer(e: Event, flag: boolean){
    // Close image viewer if clicked on el itself(not ascendant)
    if(e.target === e.currentTarget){
        return false
    }
}


export {
    close_viewer,
}
