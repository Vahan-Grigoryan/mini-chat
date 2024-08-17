import {UserMiniInfo} from "../types/user"


interface CommonFields {
    id?: number
}
interface MessageImage extends CommonFields {
    path: string
    desc?: string
}
interface Message extends CommonFields {
    text?: string
    linking_message?: Message
    author?: UserMiniInfo // this field is not db column, it may be func on server that receive
    // group message id of that message for showing author name of linking message
    images?: MessageImage[]
}
interface GroupMessage extends CommonFields {
    author: UserMiniInfo
    messages: Message[]
}
interface Conversation extends CommonFields {
    group_messages: GroupMessage[]
}


export type {
    Message,
    MessageImage,
    GroupMessage,
    Conversation,
}
