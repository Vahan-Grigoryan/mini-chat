import CenteredContent from "./UI/CenteredContent.vue"
import OkButton from "./UI/OkButton.vue"
import Input from "./UI/Input.vue"
import Contact from "./UI/Contact.vue"
import GroupMessage from "./UI/GroupMessage.vue"
import UserThumbnail from "./UI/UserThumbnail.vue"
import ImageViewer from "./UI/ImageViewer.vue"
import LinkingMessage from "./UI/LinkingMessage.vue"
import MessagesViewer from "./UI/MessagesViewer.vue"
import MessageViewer from "./UI/MessageViewer.vue"


export default [
    {...CenteredContent, name: "ui-centered-content"},
    {...OkButton, name: "ui-ok-button"},
    {...Input, name: "ui-input"},
    {...Contact, name: "ui-contact"},
    {...GroupMessage, name: "ui-group-message"},
    {...UserThumbnail, name: "ui-user-thumbnail"},
    {...ImageViewer, name: "ui-image-viewer"},
    {...LinkingMessage, name: "ui-linking-message"},
    {...MessagesViewer, name: "ui-messages-viewer"},
    {...MessageViewer, name: "ui-message-viewer"},
]
